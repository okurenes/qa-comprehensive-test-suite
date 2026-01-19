import requests
import logging
from config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APIClient:
    """API istekleri için base client class"""
    
    def __init__(self, base_url=None):
        self.base_url = base_url or Config.API_BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def get(self, endpoint, params=None, **kwargs):
        """GET request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET Request: {url}")
        
        response = self.session.get(url, params=params, timeout=Config.API_TIMEOUT, **kwargs)
        
        logger.info(f"Response Status: {response.status_code}")
        return response
    
    def post(self, endpoint, data=None, json=None, **kwargs):
        """POST request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST Request: {url}")
        
        response = self.session.post(url, data=data, json=json, timeout=Config.API_TIMEOUT, **kwargs)
        
        logger.info(f"Response Status: {response.status_code}")
        return response
    
    def put(self, endpoint, data=None, json=None, **kwargs):
        """PUT request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT Request: {url}")
        
        response = self.session.put(url, data=data, json=json, timeout=Config.API_TIMEOUT, **kwargs)
        
        logger.info(f"Response Status: {response.status_code}")
        return response
    
    def patch(self, endpoint, data=None, json=None, **kwargs):
        """PATCH request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PATCH Request: {url}")
        
        response = self.session.patch(url, data=data, json=json, timeout=Config.API_TIMEOUT, **kwargs)
        
        logger.info(f"Response Status: {response.status_code}")
        return response
    
    def delete(self, endpoint, **kwargs):
        """DELETE request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE Request: {url}")
        
        response = self.session.delete(url, timeout=Config.API_TIMEOUT, **kwargs)
        
        logger.info(f"Response Status: {response.status_code}")
        return response
    
    def set_auth_token(self, token):
        """Authorization token ekler"""
        self.session.headers.update({
            'Authorization': f'Bearer {token}'
        })
        logger.info("Authorization token eklendi")
    
    def close(self):
        """Session'ı kapatır"""
        self.session.close()
