from locust import HttpUser, task, between
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EcommerceUser(HttpUser):
    """E-commerce sitesi için load test user class"""
    
    # Kullanıcılar arası bekleme süresi (saniye)
    wait_time = between(1, 3)
    
    # Base URL (locust komut satırından verilebilir)
    host = "https://www.saucedemo.com"
    
    def on_start(self):
        """Her kullanıcı başladığında çalışır - Login"""
        logger.info("Kullanıcı login oluyor...")
        
        self.client.get("/")
        
        login_payload = {
            "user-name": "standard_user",
            "password": "secret_sauce"
        }
        
        # Login POST request
        with self.client.post("/", data=login_payload, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                logger.info("Login başarılı")
            else:
                response.failure(f"Login failed: {response.status_code}")
    
    @task(3)
    def view_products(self):
        """Ürünler sayfasını görüntüleme - En sık yapılan işlem"""
        with self.client.get("/inventory.html", catch_response=True, name="View Products") as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed to load products: {response.status_code}")
    
    @task(2)
    def add_to_cart(self):
        """Sepete ürün ekleme"""
        # JavaScript ile ekleme olduğu için simüle edildi
        logger.info("Ürün sepete ekleniyor (simulated)")
    
    @task(1)
    def view_cart(self):
        """Sepeti görüntüleme"""
        with self.client.get("/cart.html", catch_response=True, name="View Cart") as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed to load cart: {response.status_code}")
    
    @task(1)
    def checkout_step_one(self):
        """Checkout adım 1"""
        with self.client.get("/checkout-step-one.html", catch_response=True, name="Checkout Step 1") as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed checkout step 1: {response.status_code}")

class APIUser(HttpUser):
    """API load test için user class"""
    
    wait_time = between(1, 2)
    host = "https://reqres.in/api"
    
    @task(5)
    def get_users_list(self):
        """Kullanıcı listesi GET"""
        with self.client.get("/users?page=1", catch_response=True, name="Get Users List") as response:
            if response.status_code == 200 and "data" in response.json():
                response.success()
            else:
                response.failure("Failed to get users")
    
    @task(3)
    def get_single_user(self):
        """Tek kullanıcı GET"""
        with self.client.get("/users/2", catch_response=True, name="Get Single User") as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to get user")
    
    @task(2)
    def create_user(self):
        """Kullanıcı oluşturma POST"""
        payload = {
            "name": "Load Test User",
            "job": "Tester"
        }
        
        with self.client.post("/users", json=payload, catch_response=True, name="Create User") as response:
            if response.status_code == 201:
                response.success()
            else:
                response.failure("Failed to create user")
    
    @task(1)
    def login(self):
        """Login POST"""
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        
        with self.client.post("/login", json=payload, catch_response=True, name="Login") as response:
            if response.status_code == 200 and "token" in response.json():
                response.success()
            else:
                response.failure("Login failed")
