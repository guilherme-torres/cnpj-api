package pge.cnpj_api.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import pge.cnpj_api.entities.Company;

public interface CompanyRepository extends JpaRepository<Company, String> {
}
