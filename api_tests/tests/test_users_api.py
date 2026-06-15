import pytest
import responses as resp
from api_tests.utils.api_client import APIClient
from api_tests.utils.response_validator import ResponseValidator

BASE = "https://reqres.in/api"

_PAGE1_DATA = {
    "page": 1, "per_page": 6, "total": 12, "total_pages": 2,
    "data": [
        {"id": 1, "email": "george.bluth@reqres.in", "first_name": "George", "last_name": "Bluth", "avatar": "https://reqres.in/img/faces/1-image.jpg"},
        {"id": 2, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver", "avatar": "https://reqres.in/img/faces/2-image.jpg"},
        {"id": 3, "email": "emma.wong@reqres.in", "first_name": "Emma", "last_name": "Wong", "avatar": "https://reqres.in/img/faces/3-image.jpg"},
        {"id": 4, "email": "eve.holt@reqres.in", "first_name": "Eve", "last_name": "Holt", "avatar": "https://reqres.in/img/faces/4-image.jpg"},
        {"id": 5, "email": "charles.morris@reqres.in", "first_name": "Charles", "last_name": "Morris", "avatar": "https://reqres.in/img/faces/5-image.jpg"},
        {"id": 6, "email": "tracey.ramos@reqres.in", "first_name": "Tracey", "last_name": "Ramos", "avatar": "https://reqres.in/img/faces/6-image.jpg"},
    ]
}

_PAGE2_DATA = {
    "page": 2, "per_page": 6, "total": 12, "total_pages": 2,
    "data": [
        {"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson", "avatar": "https://reqres.in/img/faces/7-image.jpg"},
        {"id": 8, "email": "lindsay.ferguson@reqres.in", "first_name": "Lindsay", "last_name": "Ferguson", "avatar": "https://reqres.in/img/faces/8-image.jpg"},
        {"id": 9, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke", "avatar": "https://reqres.in/img/faces/9-image.jpg"},
        {"id": 10, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields", "avatar": "https://reqres.in/img/faces/10-image.jpg"},
        {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards", "avatar": "https://reqres.in/img/faces/11-image.jpg"},
        {"id": 12, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell", "avatar": "https://reqres.in/img/faces/12-image.jpg"},
    ]
}

_SINGLE_USER_DATA = {
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    }
}


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
    @resp.activate
    def test_get_users_list(self):
        """TC034: Kullanıcı listesi GET testi"""
        resp.add(resp.GET, f"{BASE}/users", json=_PAGE1_DATA, status=200)

        response = self.client.get("/users?page=1")

        self.validator.validate_status_code(response, 200)
        self.validator.validate_response_time(response, 3000)
        self.validator.validate_header_exists(response, "Content-Type")

        json_data = response.json()
        assert "data" in json_data, "Response'da data field yok"
        assert len(json_data["data"]) > 0, "Kullanıcı listesi boş"

    @pytest.mark.smoke
    @resp.activate
    def test_get_single_user(self):
        """TC035: Tek kullanıcı GET testi"""
        user_id = 2
        resp.add(resp.GET, f"{BASE}/users/{user_id}", json=_SINGLE_USER_DATA, status=200)

        response = self.client.get(f"/users/{user_id}")

        self.validator.validate_status_code(response, 200)
        self.validator.validate_response_time(response, 2000)

        json_data = response.json()
        assert "data" in json_data, "Response'da data field yok"
        assert json_data["data"]["id"] == user_id, "User ID uyuşmuyor"
        assert "email" in json_data["data"], "Email field yok"
        assert "first_name" in json_data["data"], "First name field yok"

    @pytest.mark.regression
    @resp.activate
    def test_get_nonexistent_user(self):
        """TC036: Olmayan kullanıcı GET testi"""
        resp.add(resp.GET, f"{BASE}/users/999999", json={}, status=404)

        response = self.client.get("/users/999999")

        self.validator.validate_status_code(response, 404)

    @pytest.mark.critical
    @resp.activate
    def test_create_user(self):
        """TC037: Kullanıcı oluşturma POST testi"""
        payload = {
            "name": "Enes Okur",
            "job": "QA Automation Engineer"
        }
        resp.add(
            resp.POST, f"{BASE}/users",
            json={"name": "Enes Okur", "job": "QA Automation Engineer", "id": "583", "createdAt": "2024-01-01T12:00:00.000Z"},
            status=201
        )

        response = self.client.post("/users", json=payload)

        self.validator.validate_status_code(response, 201)
        self.validator.validate_response_time(response, 3000)

        json_data = response.json()
        assert json_data["name"] == payload["name"], "Name uyuşmuyor"
        assert json_data["job"] == payload["job"], "Job uyuşmuyor"
        assert "id" in json_data, "ID oluşturulmadı"
        assert "createdAt" in json_data, "CreatedAt timestamp yok"

    @pytest.mark.regression
    @resp.activate
    def test_create_user_with_empty_payload(self):
        """TC038: Boş payload ile kullanıcı oluşturma testi"""
        resp.add(
            resp.POST, f"{BASE}/users",
            json={"id": "584", "createdAt": "2024-01-01T12:00:00.000Z"},
            status=201
        )

        response = self.client.post("/users", json={})

        assert response.status_code in [200, 201, 400], "Beklenmeyen status code"

    @pytest.mark.critical
    @resp.activate
    def test_update_user_put(self):
        """TC039: Kullanıcı güncelleme PUT testi"""
        user_id = 2
        payload = {
            "name": "Enes Updated",
            "job": "Senior QA Engineer"
        }
        resp.add(
            resp.PUT, f"{BASE}/users/{user_id}",
            json={"name": "Enes Updated", "job": "Senior QA Engineer", "updatedAt": "2024-01-01T12:00:00.000Z"},
            status=200
        )

        response = self.client.put(f"/users/{user_id}", json=payload)

        self.validator.validate_status_code(response, 200)
        self.validator.validate_response_time(response, 3000)

        json_data = response.json()
        assert json_data["name"] == payload["name"], "Name güncellenmedi"
        assert json_data["job"] == payload["job"], "Job güncellenmedi"
        assert "updatedAt" in json_data, "UpdatedAt timestamp yok"

    @pytest.mark.regression
    @resp.activate
    def test_update_user_patch(self):
        """TC040: Kullanıcı kısmi güncelleme PATCH testi"""
        user_id = 2
        payload = {"job": "Lead QA Engineer"}
        resp.add(
            resp.PATCH, f"{BASE}/users/{user_id}",
            json={"job": "Lead QA Engineer", "updatedAt": "2024-01-01T12:00:00.000Z"},
            status=200
        )

        response = self.client.patch(f"/users/{user_id}", json=payload)

        self.validator.validate_status_code(response, 200)

        json_data = response.json()
        assert json_data["job"] == payload["job"], "Job güncellenmedi"
        assert "updatedAt" in json_data, "UpdatedAt timestamp yok"

    @pytest.mark.critical
    @resp.activate
    def test_delete_user(self):
        """TC041: Kullanıcı silme DELETE testi"""
        user_id = 2
        resp.add(resp.DELETE, f"{BASE}/users/{user_id}", body=b"", status=204)

        response = self.client.delete(f"/users/{user_id}")

        self.validator.validate_status_code(response, 204)

    @pytest.mark.regression
    @resp.activate
    def test_users_pagination(self):
        """TC042: Kullanıcı pagination testi"""
        resp.add(resp.GET, f"{BASE}/users", json=_PAGE1_DATA, status=200)
        resp.add(resp.GET, f"{BASE}/users", json=_PAGE2_DATA, status=200)

        response_page1 = self.client.get("/users?page=1")
        response_page2 = self.client.get("/users?page=2")

        self.validator.validate_status_code(response_page1, 200)
        self.validator.validate_status_code(response_page2, 200)

        page1_data = response_page1.json()
        page2_data = response_page2.json()

        assert page1_data["page"] == 1, "Sayfa 1 değil"
        assert page2_data["page"] == 2, "Sayfa 2 değil"

        page1_ids = [user["id"] for user in page1_data["data"]]
        page2_ids = [user["id"] for user in page2_data["data"]]

        assert set(page1_ids).isdisjoint(set(page2_ids)), "Sayfalar aynı kullanıcıları içeriyor"
