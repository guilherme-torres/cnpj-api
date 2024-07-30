package pge.cnpj_api.entities;

import jakarta.persistence.*;

@Entity
@Table(name = "empresas")
public class Company {

    @Id
    @Column(name = "cnpj_basico")
    private String basicCnpj;

    @Column(name = "razao_social")
    private String companyName;

    @ManyToOne
    @JoinColumn(name = "natureza_juridica")
    private LegalNature legalNature;

    @ManyToOne
    @JoinColumn(name = "qualificacao_do_responsavel")
    private Qualification responsibleQualification;

    @Column(name = "capital_social_da_empresa")
    private String CompanyShareCapital;

    @ManyToOne
    @JoinColumn(name = "porte_da_empresa")
    private CompanySize companySize;

    @Column(name = "ente_federativo_responsavel")
    private String federativeEntityResponsible;

    public String getBasicCnpj() {
        return basicCnpj;
    }

    public void setBasicCnpj(String basicCnpj) {
        this.basicCnpj = basicCnpj;
    }

    public String getCompanyName() {
        return companyName;
    }

    public void setCompanyName(String companyName) {
        this.companyName = companyName;
    }

    public LegalNature getLegalNature() {
        return legalNature;
    }

    public void setLegalNature(LegalNature legalNature) {
        this.legalNature = legalNature;
    }

    public Qualification getResponsibleQualification() {
        return responsibleQualification;
    }

    public void setResponsibleQualification(Qualification responsibleQualification) {
        this.responsibleQualification = responsibleQualification;
    }

    public String getCompanyShareCapital() {
        return CompanyShareCapital;
    }

    public void setCompanyShareCapital(String companyShareCapital) {
        CompanyShareCapital = companyShareCapital;
    }

    public CompanySize getCompanySize() {
        return companySize;
    }

    public void setCompanySize(CompanySize companySize) {
        this.companySize = companySize;
    }

    public String getFederativeEntityResponsible() {
        return federativeEntityResponsible;
    }

    public void setFederativeEntityResponsible(String federativeEntityResponsible) {
        this.federativeEntityResponsible = federativeEntityResponsible;
    }
}
