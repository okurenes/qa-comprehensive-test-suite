import pytest
from api_tests.utils.api_client import APIClient
from api_tests.utils.response_validator import ResponseValidator

@pytest.mark.api
@pytest.mark.regression
class TestSchemaValidation:
    """API response schema validation testleri"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Her test öncesi API client oluştur"""
        self.client = APIClient()
        self.validator = ResponseValidator()
        yield
        self.client.close()
    
    def test_users_list_schema(self):
        """TC050: Users list response schema testi"""
        response = self.client.get("/users?page=1")
        
        schema = {
            "type": "object",
            "properties": {
                "page": {"type": "number"},
                "per_page": {"type": "number"},
                "total": {"type": "number"},
                "total_pages": {"type": "number"},
                "data": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "number"},
                            "email": {"type": "string"},
                            "first_name": {"type": "string"},
                            "last_name": {"type": "string"},
                            "avatar": {"type": "string"}
                        },
                        "required": ["id", "email", "first_name", "last_name"]
                    }
                }
            },
            "required": ["page", "per_page", "total", "data"]
        }
        
        self.validator.validate_json_schema(response, schema)
    
    def test_single_user_schema(self):
        """TC051: Single user response schema testi"""
        response = self.client.get("/users/2")
        
        schema = {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "email": {"type": "string"},
                        "first_name": {"type": "string"},
                        "last_name": {"type": "string"},
                        "avatar": {"type": "string"}
                    },
                    "required": ["id", "email", "first_name", "last_name"]
                }
            },
            "required": ["data"]
        }
        
        self.validator.validate_json_schema(response, schema)
    
    def test_create_user_schema(self):
        """TC052: Create user response schema testi"""
        payload = {
            "name": "Test User",
            "job": "Tester"
        }
        
        response = self.client.post("/users", json=payload)
        
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "job": {"type": "string"},
                "id": {"type": "string"},
                "createdAt": {"type": "string"}
            },
            "required": ["name", "job", "id", "createdAt"]
        }
        
        self.validator.validate_json_schema(response, schema)
    
    def test_login_response_schema(self):
        """TC053: Login response schema testi"""
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        
        response = self.client.post("/login", json=payload)
        
        schema = {
            "type": "object",
            "properties": {
                "token": {"type": "string"}
            },
            "required": ["token"]
        }
        
        self.validator.validate_json_schema(response, schema)
