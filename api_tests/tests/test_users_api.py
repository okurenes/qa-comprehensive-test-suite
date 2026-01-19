import pytest
from api_tests.utils.api_client import APIClient
from api_tests.utils.response_validator import ResponseValidator

@pytest.mark.api
class TestUsersAPI:
    """User API testleri"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Her test öncesi API client oluştur"""
        self.client = APIClient()
        self.validator = ResponseValidator()
        yield
        self.client.close()
    
    @pytest.mark.smoke
    def test_get_users_list(self):
        """TC034: Kullanıcı listesi GET testi"""
        response = self.client.get("/users?page=1")
        
        self.validator.validate_status_code(response, 200)
        self.validator.validate_response_time(response, 3000)
        self.validator.validate_header_exists(response, "Content-Type")
        
        json_data = response.json()
        assert "data" in json_data, "Response'da data field yok"
        assert len(json_data["data"]) > 0, "Kullanıcı listesi boş"
    
    @pytest.mark.smoke
    def test_get_single_user(self):
        """TC035: Tek kullanıcı GET testi"""
        user_id = 2
        response = self.client.get(f"/users/{user_id}")
        
        self.validator.validate_status_code(response, 200)
        self.validator.validate_response_time(response, 2000)
        
        json_data = response.json()
        assert "data" in json_data, "Response'da data field yok"
        assert json_data["data"]["id"] == user_id, "User ID uyuşmuyor"
        assert "email" in json_data["data"], "Email field yok"
        assert "first_name" in json_data["data"], "First name field yok"
    
    @pytest.mark.regression
    def test_get_nonexistent_user(self):
        """TC036: Olmayan kullanıcı GET testi"""
        response = self.client.get("/users/999999")
        
        self.validator.validate_status_code(response, 404)
    
    @pytest.mark.critical
    def test_create_user(self):
        """TC037: Kullanıcı oluşturma POST testi"""
        payload = {
            "name": "Enes Okur",
            "job": "QA Automation Engineer"
        }
        
        response = self.client.post("/users", json=payload)
        
        self.validator.validate_status_code(response, 201)
        self.validator.validate_response_time(response, 3000)
        
        json_data = response.json()
        assert json_data["name"] == payload["name"], "Name uyuşmuyor"
        assert json_data["job"] == payload["job"], "Job uyuşmuyor"
        assert "id" in json_data, "ID oluşturulmadı"
        assert "createdAt" in json_data, "CreatedAt timestamp yok"
    
    @pytest.mark.regression
    def test_create_user_with_empty_payload(self):
        """TC038: Boş payload ile kullanıcı oluşturma testi"""
        payload = {}
        
        response = self.client.post("/users", json=payload)
        
        # API boş payload kabul ediyor ama response döner
        assert response.status_code in [200, 201, 400], "Beklenmeyen status code"
    
    @pytest.mark.critical
    def test_update_user_put(self):
        """TC039: Kullanıcı güncelleme PUT testi"""
        user_id = 2
        payload = {
            "name": "Enes Updated",
            "job": "Senior QA Engineer"
        }
        
        response = self.client.put(f"/users/{user_id}", json=payload)
        
        self.validator.validate_status_code(response, 200)
        self.validator.validate_response_time(response, 3000)
        
        json_data = response.json()
        assert json_data["name"] == payload["name"], "Name güncellenmedi"
        assert json_data["job"] == payload["job"], "Job güncellenmedi"
        assert "updatedAt" in json_data, "UpdatedAt timestamp yok"
    
    @pytest.mark.regression
    def test_update_user_patch(self):
        """TC040: Kullanıcı kısmi güncelleme PATCH testi"""
        user_id = 2
        payload = {
            "job": "Lead QA Engineer"
        }
        
        response = self.client.patch(f"/users/{user_id}", json=payload)
        
        self.validator.validate_status_code(response, 200)
        
        json_data = response.json()
        assert json_data["job"] == payload["job"], "Job güncellenmedi"
        assert "updatedAt" in json_data, "UpdatedAt timestamp yok"
    
    @pytest.mark.critical
    def test_delete_user(self):
        """TC041: Kullanıcı silme DELETE testi"""
        user_id = 2
        
        response = self.client.delete(f"/users/{user_id}")
        
        self.validator.validate_status_code(response, 204)
    
    @pytest.mark.regression
    def test_users_pagination(self):
        """TC042: Kullanıcı pagination testi"""
        response_page1 = self.client.get("/users?page=1")
        response_page2 = self.client.get("/users?page=2")
        
        self.validator.validate_status_code(response_page1, 200)
        self.validator.validate_status_code(response_page2, 200)
        
        page1_data = response_page1.json()
        page2_data = response_page2.json()
        
        assert page1_data["page"] == 1, "Sayfa 1 değil"
        assert page2_data["page"] == 2, "Sayfa 2 değil"
        
        # Her sayfada farklı kullanıcılar olmalı
        page1_ids = [user["id"] for user in page1_data["data"]]
        page2_ids = [user["id"] for user in page2_data["data"]]
        
        assert set(page1_ids).isdisjoint(set(page2_ids)), "Sayfalar aynı kullanıcıları içeriyor"
