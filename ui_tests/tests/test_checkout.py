import pytest
from ui_tests.pages.login_page import LoginPage
from ui_tests.pages.products_page import ProductsPage
from ui_tests.pages.cart_page import CartPage
from ui_tests.pages.checkout_page import CheckoutPage
from ui_tests.utils.test_data import TestData

@pytest.mark.ui
class TestCheckout:
    """Checkout süreci test class'ı"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Her test öncesi ürün ekle ve checkout'a git"""
        login_page = LoginPage(driver)
        login_page.open(base_url)
        login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        
        products_page = ProductsPage(driver)
        products_page.add_product_to_cart_by_index(0)
        products_page.go_to_cart()
        
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()
        
        self.checkout_page = CheckoutPage(driver)
    
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_complete_checkout_process_end_to_end(self, driver):
        """TC025: Tam checkout süreci E2E testi"""
        # Step 1: Checkout bilgilerini doldur
        assert self.checkout_page.is_checkout_step_one_displayed(), "Checkout step 1 açılmadı"
        
        checkout_info = TestData.get_valid_checkout_info()
        self.checkout_page.fill_checkout_info(
            checkout_info["firstname"],
            checkout_info["lastname"],
            checkout_info["zipcode"]
        )
        
        # Step 2: Continue
        self.checkout_page.click_continue()
        assert self.checkout_page.is_checkout_step_two_displayed(), "Checkout step 2 açılmadı"
        
        # Step 3: Finish
        self.checkout_page.click_finish()
        
        # Step 4: Verify completion
        assert self.checkout_page.is_order_complete(), "Sipariş tamamlanamadı"
        assert "Thank you" in self.checkout_page.get_complete_message(), "Başarı mesajı yanlış"
    
    @pytest.mark.regression
    def test_checkout_with_empty_firstname(self, driver):
        """TC026: Boş firstname ile checkout testi"""
        self.checkout_page.fill_checkout_info("", "Okur", "06210")
        self.checkout_page.click_continue()
        
        assert self.checkout_page.is_error_displayed(), "Hata mesajı gösterilmedi"
        assert "First Name is required" in self.checkout_page.get_error_message()
    
    @pytest.mark.regression
    def test_checkout_with_empty_lastname(self, driver):
        """TC027: Boş lastname ile checkout testi"""
        self.checkout_page.fill_checkout_info("Enes", "", "06210")
        self.checkout_page.click_continue()
        
        assert self.checkout_page.is_error_displayed(), "Hata mesajı gösterilmedi"
        assert "Last Name is required" in self.checkout_page.get_error_message()
    
    @pytest.mark.regression
    def test_checkout_with_empty_zipcode(self, driver):
        """TC028: Boş zipcode ile checkout testi"""
        self.checkout_page.fill_checkout_info("Enes", "Okur", "")
        self.checkout_page.click_continue()
        
        assert self.checkout_page.is_error_displayed(), "Hata mesajı gösterilmedi"
        assert "Postal Code is required" in self.checkout_page.get_error_message()
    
    @pytest.mark.regression
    def test_checkout_with_all_empty_fields(self, driver):
        """TC029: Tüm alanlar boş checkout testi"""
        self.checkout_page.fill_checkout_info("", "", "")
        self.checkout_page.click_continue()
        
        assert self.checkout_page.is_error_displayed(), "Hata mesajı gösterilmedi"
    
    @pytest.mark.regression
    def test_checkout_cancel_button(self, driver):
        """TC030: Checkout cancel butonu testi"""
        self.checkout_page.click_cancel()
        
        assert "cart.html" in self.checkout_page.get_current_url(), "Cart sayfasına dönülmedi"
    
    @pytest.mark.smoke
    def test_checkout_overview_displays_correct_info(self, driver):
        """TC031: Checkout overview bilgilerinin doğru görüntülendiği testi"""
        checkout_info = TestData.get_valid_checkout_info()
        self.checkout_page.fill_checkout_info(
            checkout_info["firstname"],
            checkout_info["lastname"],
            checkout_info["zipcode"]
        )
        self.checkout_page.click_continue()
        
        # Overview sayfasında fiyat bilgilerini kontrol et
        subtotal = self.checkout_page.get_subtotal()
        tax = self.checkout_page.get_tax()
        total = self.checkout_page.get_total()
        
        assert subtotal != "0", "Subtotal gösterilmiyor"
        assert tax != "0", "Tax gösterilmiyor"
        assert total != "0", "Total gösterilmiyor"
        
        # Matematiksel kontrol
        expected_total = float(subtotal) + float(tax)
        assert float(total) == expected_total, "Total hesaplama yanlış"
    
    @pytest.mark.critical
    def test_checkout_with_random_user_data(self, driver):
        """TC032: Random kullanıcı verileri ile checkout testi"""
        random_info = TestData.generate_checkout_info()
        
        self.checkout_page.fill_checkout_info(
            random_info["firstname"],
            random_info["lastname"],
            random_info["zipcode"]
        )
        self.checkout_page.click_continue()
        
        assert self.checkout_page.is_checkout_step_two_displayed(), "Step 2'ye geçilemedi"
        
        self.checkout_page.click_finish()
        
        assert self.checkout_page.is_order_complete(), "Sipariş tamamlanamadı"
    
    @pytest.mark.regression
    def test_back_home_button_after_checkout(self, driver):
        """TC033: Checkout sonrası home'a dönüş testi"""
        checkout_info = TestData.get_valid_checkout_info()
        self.checkout_page.fill_checkout_info(
            checkout_info["firstname"],
            checkout_info["lastname"],
            checkout_info["zipcode"]
        )
        self.checkout_page.click_continue()
        self.checkout_page.click_finish()
        
        assert self.checkout_page.is_order_complete(), "Sipariş tamamlanamadı"
        
        self.checkout_page.back_to_home()
        
        assert "inventory.html" in self.checkout_page.get_current_url(), "Home'a dönülemedi"
