import jsonschema
from jsonschema import validate
import logging

logger = logging.getLogger(__name__)

class ResponseValidator:
    """API response doğrulama utility class"""
    
    @staticmethod
    def validate_status_code(response, expected_status):
        """Status code doğrular"""
        actual_status = response.status_code
        assert actual_status == expected_status, \
            f"Status code uyuşmuyor. Beklenen: {expected_status}, Gelen: {actual_status}"
        logger.info(f"Status code doğrulandı: {actual_status}")
    
    @staticmethod
    def validate_response_time(response, max_time_ms):
        """Response time doğrular"""
        response_time = response.elapsed.total_seconds() * 1000
        assert response_time < max_time_ms, \
            f"Response time çok yüksek. Maksimum: {max_time_ms}ms, Gelen: {response_time}ms"
        logger.info(f"Response time doğrulandı: {response_time}ms")
    
    @staticmethod
    def validate_json_schema(response, schema):
        """JSON schema doğrular"""
        try:
            validate(instance=response.json(), schema=schema)
            logger.info("JSON schema doğrulandı")
        except jsonschema.exceptions.ValidationError as e:
            raise AssertionError(f"JSON schema validation hatası: {e.message}")
    
    @staticmethod
    def validate_header_exists(response, header_name):
        """Header varlığını doğrular"""
        assert header_name in response.headers, \
            f"Header bulunamadı: {header_name}"
        logger.info(f"Header doğrulandı: {header_name}")
    
    @staticmethod
    def validate_json_field(response, field_name, expected_value=None):
        """JSON field doğrular"""
        json_data = response.json()
        assert field_name in json_data, \
            f"Field bulunamadı: {field_name}"
        
        if expected_value is not None:
            actual_value = json_data[field_name]
            assert actual_value == expected_value, \
                f"Field değeri uyuşmuyor. Beklenen: {expected_value}, Gelen: {actual_value}"
        
        logger.info(f"Field doğrulandı: {field_name}")
    
    @staticmethod
    def validate_not_empty(response, field_name):
        """Field'ın boş olmadığını doğrular"""
        json_data = response.json()
        assert field_name in json_data, f"Field bulunamadı: {field_name}"
        assert json_data[field_name], f"Field boş: {field_name}"
        logger.info(f"Field boş değil: {field_name}")
