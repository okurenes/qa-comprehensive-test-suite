import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Merkezi konfigürasyon class'ı"""
    
    # Application URLs
    BASE_URL = os.getenv('BASE_URL', 'https://www.saucedemo.com')
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://reqres.in/api')
    
    # Browser Configuration
    BROWSER = os.getenv('BROWSER', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
    TIMEOUT = int(os.getenv('TIMEOUT', '10'))
    
    # Database Configuration
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = int(os.getenv('DB_PORT', '5432'))
    DB_NAME = os.getenv('DB_NAME', 'test_db')
    DB_USER = os.getenv('DB_USER', 'test_user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'test_password')
    
    # API Configuration
    API_TIMEOUT = int(os.getenv('API_TIMEOUT', '30'))
    
    # Test Data
    VALID_USERNAME = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    
    @classmethod
    def get_db_connection_string(cls):
        """Database connection string döner"""
        return f"postgresql://{cls.DB_USER}:{cls.DB_PASSWORD}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"
