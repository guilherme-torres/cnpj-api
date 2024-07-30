package pge.cnpj_api.entities;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "identificacaosocio")
public class PartnerIdentifier {
    @Id
    @Column(name = "codigo")
    private Short code;

    @Column(name = "descricao")
    private String description;

    public Short getCode() {
        return code;
    }

    public void setCode(Short code) {
        this.code = code;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
}
