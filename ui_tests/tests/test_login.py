import pytest
from ui_tests.pages.login_page import LoginPage
from ui_tests.pages.products_page import ProductsPage
from ui_tests.utils.test_data import TestData

@pytest.mark.ui
@pytest.mark.smoke
class TestLogin:
    """Login fonksiyonalitesi test class'ı"""
    
    def test_successful_login_with_valid_credentials(self, driver, base_url):
        """TC001: Geçerli kullanıcı bilgileriyle başarılı login testi"""
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        
        login_page.open(base_url)
        assert login_page.is_login_page_loaded(), "Login sayfası yüklenemedi"
        
        login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        
        assert products_page.is_products_page_displayed(), "Products sayfası açılmadı"
        assert "inventory.html" in products_page.get_current_url(), "URL products sayfasına yönlenmedi"
    
    @pytest.mark.regression
    def test_login_with_invalid_username(self, driver, base_url):
        """TC002: Geçersiz kullanıcı adı ile login testi"""
        login_page = LoginPage(driver)
        
        login_page.open(base_url)
        login_page.login(TestData.INVALID_USERNAME, TestData.VALID_PASSWORD)
        
        assert login_page.is_error_displayed(), "Hata mesajı gösterilmedi"
        error_message = login_page.get_error_message()
        assert "Epic sadface" in error_message, "Hata mesajı beklenen formatta değil"
        assert "do not match" in error_message, "Hata mesajı içeriği yanlış"
    
    @pytest.mark.regression
    def test_login_with_invalid_password(self, driver, base_url):
        """TC003: Geçersiz şifre ile login testi"""
        login_page = LoginPage(driver)
        
        login_page.open(base_url)
        login_page.login(TestData.VALID_USERNAME, TestData.INVALID_PASSWORD)
        
        assert login_page.is_error_displayed(), "Hata mesajı gösterilmedi"
        assert "Epic sadface" in login_page.get_error_message()
    
    @pytest.mark.critical
    def test_login_with_locked_user(self, driver, base_url):
        """TC004: Kilitli kullanıcı ile login testi"""
        login_page = LoginPage(driver)
        
        login_page.open(base_url)
        login_page.login(TestData.LOCKED_USERNAME, TestData.VALID_PASSWORD)
        
        assert login_page.is_error_displayed(), "Locked user hata mesajı gösterilmedi"
        error_message = login_page.get_error_message()
        assert "locked out" in error_message.lower(), "Locked out mesajı yok"
    
    @pytest.mark.regression
    def test_login_with_empty_credentials(self, driver, base_url):
        """TC005: Boş credentials ile login testi"""
        login_page = LoginPage(driver)
        
        login_page.open(base_url)
        login_page.login("", "")
        
        assert login_page.is_error_displayed(), "Boş alan hata mesajı gösterilmedi"
        assert "Username is required" in login_page.get_error_message()
    
    @pytest.mark.regression
    def test_login_with_empty_password(self, driver, base_url):
        """TC006: Boş şifre ile login testi"""
        login_page = LoginPage(driver)
        
        login_page.open(base_url)
        login_page.login(TestData.VALID_USERNAME, "")
        
        assert login_page.is_error_displayed(), "Boş şifre hata mesajı gösterilmedi"
        assert "Password is required" in login_page.get_error_message()
    
    @pytest.mark.smoke
    def test_logout_functionality(self, driver, base_url):
        """TC007: Logout fonksiyonalitesi testi"""
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        
        login_page.open(base_url)
        login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        
        assert products_page.is_products_page_displayed(), "Login başarısız"
        
        products_page.logout()
        
        assert login_page.is_login_page_loaded(), "Logout başarısız, login sayfası açılmadı"
        assert base_url in login_page.get_current_url(), "URL login sayfasına dönmedi"
