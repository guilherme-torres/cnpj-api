import logging
import os
import csv
import sqlite3


logger = logging.getLogger(__name__)

class FeedDatabase:
    def __init__(self):
        self.IMPORT_PLAN = [
            ("PAISCSV", "paises"),
            ("MUNICCSV", "municipios"),
            ("QUALSCSV", "qualificacoes_socios"),
            ("NATJUCSV", "naturezas_juridicas"),
            ("CNAECSV", "cnaes"),
            ("MOTICSV", "motivos"),
            ("EMPRECSV", "empresas"),
            ("ESTABELE", "estabelecimentos"),
            ("SIMPLES.CSV", "simples"),
            ("SOCIOCSV", "socios"),
        ]
        self.DATABASE_FILE = "cnpj.db"
        self.TABLES_FILE = "tables.sql"
        self.INDEXES_FILE = "indexes.sql"
        self.BATCH_SIZE = 10_000
        self.DATA_DIR = "data"
        self.QUERIES = {
            "paises": {
                "query": '''INSERT OR IGNORE INTO paises (codigo, descricao) VALUES (?, ?)''',
                "expected_cols": 2
            },
            "municipios": {
                "query": '''INSERT OR IGNORE INTO municipios (codigo, descricao) VALUES (?, ?)''',
                "expected_cols": 2
            },
            "qualificacoes_socios": {
                "query": '''INSERT OR IGNORE INTO qualificacoes_socios (codigo, descricao) VALUES (?, ?)''',
                "expected_cols": 2
            },
            "naturezas_juridicas": {
                "query": '''INSERT OR IGNORE INTO naturezas_juridicas (codigo, descricao) VALUES (?, ?)''',
                "expected_cols": 2
            },
            "cnaes": {
                "query": '''INSERT OR IGNORE INTO cnaes (codigo, descricao) VALUES (?, ?)''',
                "expected_cols": 2
            },
            "motivos": {
                "query": '''INSERT OR IGNORE INTO motivos (codigo, descricao) VALUES (?, ?)''',
                "expected_cols": 2
            },
            "empresas": {
                "query": '''INSERT OR IGNORE INTO empresas (cnpj_basico, razao_social_nome_empresarial, natureza_juridica, qualificacao_do_responsavel, capital_social_da_empresa, porte_da_empresa, ente_federativo_responsavel) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                "expected_cols": 7
            },
            "estabelecimentos": {
                "query": '''INSERT OR IGNORE INTO estabelecimentos (cnpj_basico, cnpj_ordem, cnpj_dv, identificador_matriz_filial, nome_fantasia, situacao_cadastral, data_situacao_cadastral, motivo_situacao_cadastral, nome_da_cidade_no_exterior, pais, data_de_inicio_atividade, cnae_fiscal_principal, cnae_fiscal_secundaria, tipo_de_logradouro, logradouro, numero, complemento, bairro, cep, uf, municipio, ddd_1, telefone_1, ddd_2, telefone_2, ddd_do_fax, fax, correio_eletronico, situacao_especial, data_da_situacao_especial) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                "expected_cols": 30
            },
            "simples": {
                "query": '''INSERT OR IGNORE INTO simples (cnpj_basico, opcao_pelo_simples, data_de_opcao_pelo_simples, data_de_exclusao_do_simples, opcao_pelo_mei, data_de_opcao_pelo_mei, data_de_exclusao_do_mei) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                "expected_cols": 7
            },
            "socios": {
                "query": '''INSERT INTO socios (cnpj_basico, identificador_de_socio, nome_do_socio_ou_razao_social, cnpj_cpf_do_socio, qualificacao_do_socio, data_de_entrada_sociedade, pais, representante_legal, nome_do_representante, qualificacao_do_representante_legal, faixa_etaria) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                "expected_cols": 11
            },
        }

    def _get_db_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.DATABASE_FILE)

    def _create_tables(self):
        with open(self.TABLES_FILE) as tables_file:
            sql = tables_file.read()
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("PRAGMA journal_mode=WAL")
                cursor.execute("PRAGMA synchronous=NORMAL")
                cursor.executescript(sql)
                conn.commit()

    def _import_data(self, filename: str, tablename: str):
        # abrir arquivo csv
        filepath = os.path.join(self.DATA_DIR, filename)
        if not os.path.exists(filepath):
            logger.info(f"file {filepath} not exists")
            return
        
        query_info = self.QUERIES.get(tablename)
        if not query_info:
            logger.info(f"table {tablename} not found in QUERIES property")
            return

        logger.info(f"importing data from {filepath}...")

        with open(filepath, newline="", encoding="ISO-8859-1") as csvfile:
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                csv_reader = csv.reader(csvfile, delimiter=";")
                batch = []
                for row in csv_reader:
                    if len(row) != query_info["expected_cols"]:
                        logger.info(f"malformed row in {filepath}: {row}")
                        continue
                    row = [None if cell == "" else cell for cell in row]
                    if tablename == "empresas":
                        row[4] = row[4].replace(".", "").replace(",", ".")
                    batch.append(row)
                    if len(batch) >= self.BATCH_SIZE:
                        try:
                            cursor.executemany(query_info["query"], batch)
                            conn.commit()
                        except sqlite3.Error as e:
                            logger.info(f"error inserting batch in {tablename}: {e}")
                        batch.clear()
                if len(batch) > 0:
                    cursor.executemany(query_info["query"], batch)
                    conn.commit()

    def _create_indexes(self):
        logger.info("creating indexes...")
        with open(self.INDEXES_FILE) as indexes_file:
            sql = indexes_file.read()
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.executescript(sql)
                conn.commit()

    def execute(self):
        self._create_tables()

        for (filekey, tablename) in self.IMPORT_PLAN:
            files = os.listdir(self.DATA_DIR)
            for filename in files:
                if filekey in filename:
                    self._import_data(filename, tablename)
        
        self._create_indexes()
