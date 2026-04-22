CREATE TABLE IF NOT EXISTS paises (
    codigo TEXT PRIMARY KEY,
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS municipios (
    codigo TEXT PRIMARY KEY,
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS qualificacoes_socios (
    codigo TEXT PRIMARY KEY,
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS naturezas_juridicas (
    codigo TEXT PRIMARY KEY,
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS cnaes (
    codigo TEXT PRIMARY KEY,
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS motivos (
    codigo TEXT PRIMARY KEY,
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS empresas (
    cnpj_basico TEXT PRIMARY KEY,
    razao_social_nome_empresarial TEXT,
    natureza_juridica TEXT,
    qualificacao_do_responsavel TEXT,
    capital_social_da_empresa REAL,
    porte_da_empresa TEXT,
    ente_federativo_responsavel TEXT
);

CREATE TABLE IF NOT EXISTS estabelecimentos (
    cnpj_basico TEXT, 
    cnpj_ordem TEXT, 
    cnpj_dv TEXT, 
    identificador_matriz_filial TEXT, 
    nome_fantasia TEXT,
    situacao_cadastral TEXT,
    data_situacao_cadastral TEXT,
    motivo_situacao_cadastral TEXT,
    nome_da_cidade_no_exterior TEXT,
    pais TEXT,
    data_de_inicio_atividade TEXT,
    cnae_fiscal_principal TEXT,
    cnae_fiscal_secundaria TEXT,
    tipo_de_logradouro TEXT,
    logradouro TEXT,
    numero TEXT,
    complemento TEXT,
    bairro TEXT,
    cep TEXT,
    uf TEXT,
    municipio TEXT,
    ddd_1 TEXT,
    telefone_1 TEXT,
    ddd_2 TEXT,
    telefone_2 TEXT,
    ddd_do_fax TEXT,
    fax TEXT,
    correio_eletronico TEXT,
    situacao_especial TEXT,
    data_da_situacao_especial TEXT,
    PRIMARY KEY (cnpj_basico, cnpj_ordem, cnpj_dv)
);

CREATE TABLE IF NOT EXISTS simples (
    cnpj_basico TEXT PRIMARY KEY,
    opcao_pelo_simples TEXT,
    data_de_opcao_pelo_simples TEXT,
    data_de_exclusao_do_simples TEXT,
    opcao_pelo_mei TEXT,
    data_de_opcao_pelo_mei TEXT,
    data_de_exclusao_do_mei TEXT
);

CREATE TABLE IF NOT EXISTS socios (
    cnpj_basico TEXT,
    identificador_de_socio TEXT,
    nome_do_socio_ou_razao_social TEXT,
    cnpj_cpf_do_socio TEXT,
    qualificacao_do_socio TEXT,
    data_de_entrada_sociedade TEXT,
    pais TEXT,
    representante_legal TEXT,
    nome_do_representante TEXT,
    qualificacao_do_representante_legal TEXT,
    faixa_etaria TEXT,
    PRIMARY KEY (cnpj_basico, identificador_de_socio, cnpj_cpf_do_socio)
);