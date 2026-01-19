import pytest
from ui_tests.pages.login_page import LoginPage
from ui_tests.pages.products_page import ProductsPage
from ui_tests.utils.test_data import TestData

@pytest.mark.ui
class TestProducts:
    """Ürünler sayfası test class'ı"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Her test öncesi login işlemi"""
        login_page = LoginPage(driver)
        login_page.open(base_url)
        login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        self.products_page = ProductsPage(driver)
    
    @pytest.mark.smoke
    def test_products_page_loads_successfully(self, driver):
        """TC008: Products sayfasının başarıyla yüklendiği testi"""
        assert self.products_page.is_products_page_displayed(), "Products sayfası görüntülenemedi"
        assert self.products_page.get_products_count() > 0, "Hiç ürün görüntülenmiyor"
    
    @pytest.mark.regression
    def test_all_products_displayed(self, driver):
        """TC009: Tüm ürünlerin görüntülendiği testi"""
        products_count = self.products_page.get_products_count()
        assert products_count == 6, f"Beklenen 6 ürün, görüntülenen {products_count}"
        
        product_names = self.products_page.get_product_names()
        assert len(product_names) == 6, "Ürün isimleri tam yüklenmedi"
        
        product_prices = self.products_page.get_product_prices()
        assert len(product_prices) == 6, "Ürün fiyatları tam yüklenmedi"
    
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_add_single_product_to_cart(self, driver):
        """TC010: Tek ürün sepete ekleme testi"""
        initial_count = self.products_page.get_cart_badge_count()
        assert initial_count == 0, "Sepet başlangıçta boş olmalı"
        
        self.products_page.add_product_to_cart_by_index(0)
        
        badge_count = self.products_page.get_cart_badge_count()
        assert badge_count == 1, f"Sepet badge beklenen 1, görünen {badge_count}"
    
    @pytest.mark.regression
    def test_add_multiple_products_to_cart(self, driver):
        """TC011: Birden fazla ürün sepete ekleme testi"""
        self.products_page.add_product_to_cart_by_index(0)
        self.products_page.add_product_to_cart_by_index(1)
        self.products_page.add_product_to_cart_by_index(2)
        
        badge_count = self.products_page.get_cart_badge_count()
        assert badge_count == 3, f"Sepet badge beklenen 3, görünen {badge_count}"
    
    @pytest.mark.regression
    def test_add_all_products_to_cart(self, driver):
        """TC012: Tüm ürünleri sepete ekleme testi"""
        self.products_page.add_all_products_to_cart()
        
        badge_count = self.products_page.get_cart_badge_count()
        assert badge_count == 6, f"Tüm ürünler eklenmedi, badge count: {badge_count}"
    
    @pytest.mark.regression
    def test_remove_product_from_products_page(self, driver):
        """TC013: Products sayfasından ürün çıkarma testi"""
        self.products_page.add_product_to_cart_by_index(0)
        assert self.products_page.get_cart_badge_count() == 1, "Ürün eklenemedi"
        
        self.products_page.remove_product_from_cart_by_index(0)
        
        badge_count = self.products_page.get_cart_badge_count()
        assert badge_count == 0, "Ürün çıkarılamadı"
    
    @pytest.mark.smoke
    def test_navigate_to_cart_from_products_page(self, driver):
        """TC014: Products sayfasından cart'a geçiş testi"""
        self.products_page.add_product_to_cart_by_index(0)
        self.products_page.go_to_cart()
        
        assert "cart.html" in self.products_page.get_current_url(), "Cart sayfasına geçilemedi"
    
    @pytest.mark.regression
    def test_product_names_are_displayed(self, driver):
        """TC015: Ürün isimlerinin görüntülendiği testi"""
        product_names = self.products_page.get_product_names()
        
        assert len(product_names) > 0, "Ürün isimleri görüntülenmiyor"
        for name in product_names:
            assert name != "", "Boş ürün ismi var"
    
    @pytest.mark.regression
    def test_product_prices_are_displayed(self, driver):
        """TC016: Ürün fiyatlarının görüntülendiği testi"""
        product_prices = self.products_page.get_product_prices()
        
        assert len(product_prices) > 0, "Ürün fiyatları görüntülenmiyor"
        for price in product_prices:
            assert "$" in price, "Fiyat formatı yanlış"
            assert price != "$", "Boş fiyat var"
