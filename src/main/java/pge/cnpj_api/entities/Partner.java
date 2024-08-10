package pge.cnpj_api.entities;

import jakarta.persistence.*;

@Entity
@Table(name = "socios")
public class Partner {
    @Id
    @Column(name = "id")
    private Integer id;

    @Column(name = "cnpj_basico")
    private String basicCnpj;

    @ManyToOne
    @JoinColumn(name = "identificador_de_socio")
    private PartnerIdentifier partnerIdentifier;

    @Column(name = "nome_do_socio_razao_social")
    private String partnerName;

    @Column(name = "cnpj_cpf_do_socio")
    private String partnerDocument;

    @ManyToOne
    @JoinColumn(name = "qualificacao_do_socio")
    private Qualification partnerQualification;

    @Column(name = "data_de_entrada_sociedade")
    private String entryDate;

    @ManyToOne
    @JoinColumn(name = "pais")
    private Country country;

    @Column(name = "representante_legal")
    private String legalRepresentative;

    @Column(name = "nome_do_representante")
    private String representativeName;

    @ManyToOne
    @JoinColumn(name = "qualificacao_do_representante_legal")
    private Qualification legalRepresentativeQualification;

    @ManyToOne
    @JoinColumn(name = "faixa_etaria")
    private AgeGroup ageGroup;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getBasicCnpj() {
        return basicCnpj;
    }

    public void setBasicCnpj(String basicCnpj) {
        this.basicCnpj = basicCnpj;
    }

    public PartnerIdentifier getPartnerIdentifier() {
        return partnerIdentifier;
    }

    public void setPartnerIdentifier(PartnerIdentifier partnerIdentifier) {
        this.partnerIdentifier = partnerIdentifier;
    }

    public String getPartnerName() {
        return partnerName;
    }

    public void setPartnerName(String partnerName) {
        this.partnerName = partnerName;
    }

    public String getPartnerDocument() {
        return partnerDocument;
    }

    public void setPartnerDocument(String partnerDocument) {
        this.partnerDocument = partnerDocument;
    }

    public Qualification getPartnerQualification() {
        return partnerQualification;
    }

    public void setPartnerQualification(Qualification partnerQualification) {
        this.partnerQualification = partnerQualification;
    }

    public String getEntryDate() {
        return entryDate;
    }

    public void setEntryDate(String entryDate) {
        this.entryDate = entryDate;
    }

    public Country getCountry() {
        return country;
    }

    public void setCountry(Country country) {
        this.country = country;
    }

    public String getLegalRepresentative() {
        return legalRepresentative;
    }

    public void setLegalRepresentative(String legalRepresentative) {
        this.legalRepresentative = legalRepresentative;
    }

    public String getRepresentativeName() {
        return representativeName;
    }

    public void setRepresentativeName(String representativeName) {
        this.representativeName = representativeName;
    }

    public Qualification getLegalRepresentativeQualification() {
        return legalRepresentativeQualification;
    }

    public void setLegalRepresentativeQualification(Qualification legalRepresentativeQualification) {
        this.legalRepresentativeQualification = legalRepresentativeQualification;
    }

    public AgeGroup getAgeGroup() {
        return ageGroup;
    }

    public void setAgeGroup(AgeGroup ageGroup) {
        this.ageGroup = ageGroup;
    }
}
