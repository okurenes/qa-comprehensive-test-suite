import pytest
from api_tests.utils.api_client import APIClient
from api_tests.utils.response_validator import ResponseValidator

@pytest.mark.api
class TestAuthAPI:
    """Authentication API testleri"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Her test öncesi API client oluştur"""
        self.client = APIClient()
        self.validator = ResponseValidator()
        yield
        self.client.close()
    
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_successful_registration(self):
        """TC043: Başarılı kayıt testi"""
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        
        response = self.client.post("/register", json=payload)
        
        self.validator.validate_status_code(response, 200)
        self.validator.validate_response_time(response, 3000)
        
        json_data = response.json()
        assert "id" in json_data, "User ID oluşturulmadı"
        assert "token" in json_data, "Token oluşturulmadı"
        assert json_data["token"] != "", "Token boş"
    
    @pytest.mark.regression
    def test_registration_without_password(self):
        """TC044: Şifresiz kayıt testi"""
        payload = {
            "email": "sydney@fife"
        }
        
        response = self.client.post("/register", json=payload)
        
        self.validator.validate_status_code(response, 400)
        
        json_data = response.json()
        assert "error" in json_data, "Error mesajı yok"
    
    @pytest.mark.regression
    def test_registration_without_email(self):
        """TC045: Email'siz kayıt testi"""
        payload = {
            "password": "testpassword"
        }
        
        response = self.client.post("/register", json=payload)
        
        self.validator.validate_status_code(response, 400)
    
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_successful_login(self):
        """TC046: Başarılı login testi"""
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        
        response = self.client.post("/login", json=payload)
        
        self.validator.validate_status_code(response, 200)
        self.validator.validate_response_time(response, 3000)
        
        json_data = response.json()
        assert "token" in json_data, "Token oluşturulmadı"
        assert len(json_data["token"]) > 0, "Token boş"
    
    @pytest.mark.regression
    def test_login_without_password(self):
        """TC047: Şifresiz login testi"""
        payload = {
            "email": "peter@klaven"
        }
        
        response = self.client.post("/login", json=payload)
        
        self.validator.validate_status_code(response, 400)
        
        json_data = response.json()
        assert "error" in json_data, "Error mesajı yok"
        assert "Missing password" in json_data["error"], "Error mesajı yanlış"
    
    @pytest.mark.regression
    def test_login_with_invalid_credentials(self):
        """TC048: Geçersiz credentials ile login testi"""
        payload = {
            "email": "invalid@test.com",
            "password": "wrongpassword"
        }
        
        response = self.client.post("/login", json=payload)
        
        self.validator.validate_status_code(response, 400)
    
    @pytest.mark.regression
    def test_login_with_empty_payload(self):
        """TC049: Boş payload ile login testi"""
        payload = {}
        
        response = self.client.post("/login", json=payload)
        
        self.validator.validate_status_code(response, 400)
