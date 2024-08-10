package pge.cnpj_api.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import pge.cnpj_api.entities.Partner;

import java.util.List;

public interface PartnerRepository extends JpaRepository<Partner, Long> {
    List<Partner> findByBasicCnpj(String basicCnpj);
    List<Partner> findByPartnerNameAndPartnerDocument(String partnerName, String partnerDocument);
}
