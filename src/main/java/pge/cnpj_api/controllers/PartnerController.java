package pge.cnpj_api.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import pge.cnpj_api.entities.Partner;
import pge.cnpj_api.repositories.PartnerRepository;

import java.util.List;

@RestController
@RequestMapping("/partners")
public class PartnerController {
    private final PartnerRepository partnerRepository;

    public PartnerController(PartnerRepository partnerRepository) {
        this.partnerRepository = partnerRepository;
    }

    @GetMapping
    public List<Partner> findByBasicCnpj(@RequestParam("basicCnpj") String basicCnpj) {
        return partnerRepository.findByBasicCnpj(basicCnpj);
    }
}
