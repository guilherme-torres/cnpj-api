package pge.cnpj_api.controllers;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import pge.cnpj_api.entities.Partner;
import pge.cnpj_api.repositories.PartnerRepository;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/partners")
public class PartnerController {
    private final PartnerRepository partnerRepository;

    public PartnerController(PartnerRepository partnerRepository) {
        this.partnerRepository = partnerRepository;
    }

//    @GetMapping
//    public List<Partner> findByBasicCnpj(@RequestParam("basicCnpj") String basicCnpj) {
//        return partnerRepository.findByBasicCnpj(basicCnpj);
//    }

    @GetMapping
    public ResponseEntity find(@RequestParam Map<String, String> params) {
        String basicCnpj = params.get("basicCnpj");
        String partnerName = params.get("partnerName");
        String partnerDocument = params.get("partnerDocument");
        if (basicCnpj != null) {
            return ResponseEntity.ok(partnerRepository.findByBasicCnpj(basicCnpj));
        }
        if (partnerName != null && partnerDocument != null) {
            return ResponseEntity.ok(partnerRepository.findByPartnerNameAndPartnerDocument(partnerName, partnerDocument));
        }
        return ResponseEntity.badRequest().build();
    }
}
