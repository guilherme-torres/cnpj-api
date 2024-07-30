package pge.cnpj_api.controllers;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import pge.cnpj_api.entities.Company;
import pge.cnpj_api.exceptions.CompanyNotFoundException;
import pge.cnpj_api.repositories.CompanyRepository;

import java.util.List;

@RestController
@RequestMapping("/companies")
public class CompanyController {

    private final CompanyRepository companyRepository;

    public CompanyController(CompanyRepository companyRepository) {
        this.companyRepository = companyRepository;
    }

    @GetMapping("/{basicCnpj}")
    public ResponseEntity<Company> findByBasicCnpj(@PathVariable("basicCnpj") String basicCnpj) throws CompanyNotFoundException {
        Company company = companyRepository.findById(basicCnpj).orElseThrow(() -> new CompanyNotFoundException("Company not found."));
        return ResponseEntity.ok().body(company);
    }
}
