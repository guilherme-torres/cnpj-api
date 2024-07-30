package pge.cnpj_api.dto;

import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;

public class ApiErrorResponseDTO {
    private String message;
    private HttpStatus status;

    public ApiErrorResponseDTO(String message, HttpStatus status) {
        this.message = message;
        this.status = status;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public HttpStatus getStatus() {
        return status;
    }

    public void setStatus(HttpStatus status) {
        this.status = status;
    }
}
