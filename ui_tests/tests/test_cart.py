import pytest
from ui_tests.pages.login_page import LoginPage
from ui_tests.pages.products_page import ProductsPage
from ui_tests.pages.cart_page import CartPage
from ui_tests.utils.test_data import TestData

@pytest.mark.ui
class TestCart:
    """Sepet fonksiyonalitesi test class'ı"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Her test öncesi login ve ürün ekleme"""
        login_page = LoginPage(driver)
        login_page.open(base_url)
        login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        
        self.products_page = ProductsPage(driver)
        self.products_page.add_product_to_cart_by_index(0)
        self.products_page.go_to_cart()
        
        self.cart_page = CartPage(driver)
    
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_cart_page_loads_successfully(self, driver):
        """TC017: Cart sayfasının başarıyla yüklendiği testi"""
        assert self.cart_page.is_cart_page_displayed(), "Cart sayfası yüklenemedi"
        assert "cart.html" in self.cart_page.get_current_url()
    
    @pytest.mark.smoke
    def test_added_product_appears_in_cart(self, driver):
        """TC018: Eklenen ürünün sepette görünmesi testi"""
        cart_items = self.cart_page.get_cart_items_count()
        assert cart_items == 1, f"Sepette beklenen 1 ürün, bulunan {cart_items}"
    
    @pytest.mark.regression
    def test_cart_item_details_displayed(self, driver):
        """TC019: Sepetteki ürün detaylarının görüntülendiği testi"""
        item_names = self.cart_page.get_cart_item_names()
        assert len(item_names) > 0, "Ürün isimleri görüntülenmiyor"
        
        item_prices = self.cart_page.get_cart_item_prices()
        assert len(item_prices) > 0, "Ürün fiyatları görüntülenmiyor"
        assert "$" in item_prices[0], "Fiyat formatı yanlış"
    
    @pytest.mark.regression
    def test_remove_product_from_cart(self, driver):
        """TC020: Sepetten ürün çıkarma testi"""
        import time
        self.cart_page.remove_item_by_index(0)
        time.sleep(1)
        
        cart_items = self.cart_page.get_cart_items_count()
        assert cart_items == 0, "Ürün sepetten çıkarılamadı"
    
    @pytest.mark.regression
    def test_multiple_products_in_cart(self, driver):
        """TC021: Birden fazla ürün sepet testi"""
        self.cart_page.continue_shopping()
        self.products_page.add_product_to_cart_by_index(1)
        self.products_page.add_product_to_cart_by_index(2)
        self.products_page.go_to_cart()
        
        cart_items = self.cart_page.get_cart_items_count()
        assert cart_items == 3, f"Sepette beklenen 3 ürün, bulunan {cart_items}"
    
    @pytest.mark.smoke
    def test_continue_shopping_from_cart(self, driver):
        """TC022: Sepetten alışverişe devam testi"""
        self.cart_page.continue_shopping()
        
        assert self.products_page.is_products_page_displayed(), "Products sayfasına dönülemedi"
        assert "inventory.html" in self.products_page.get_current_url()
    
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_proceed_to_checkout_from_cart(self, driver):
        """TC023: Sepetten checkout'a geçiş testi"""
        self.cart_page.proceed_to_checkout()
        
        assert "checkout-step-one" in self.cart_page.get_current_url(), "Checkout sayfasına geçilemedi"
    
    @pytest.mark.regression
    def test_empty_cart_displays_no_items(self, driver):
        """TC024: Boş sepet testi"""
        self.cart_page.remove_all_items()
        
        assert self.cart_page.is_cart_empty(), "Sepet boşaltılamadı"
        assert self.cart_page.get_cart_items_count() == 0, "Sepette hala ürün var"
