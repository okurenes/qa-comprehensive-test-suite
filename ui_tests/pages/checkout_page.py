from selenium.webdriver.common.by import By
from ui_tests.pages.base_page import BasePage

class CheckoutPage(BasePage):
    """Checkout sayfası için Page Object"""
    
    # Locators
    CHECKOUT_TITLE = (By.CLASS_NAME, "title")
    FIRSTNAME_INPUT = (By.ID, "first-name")
    LASTNAME_INPUT = (By.ID, "last-name")
    ZIPCODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    SUMMARY_SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    SUMMARY_TAX = (By.CLASS_NAME, "summary_tax_label")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_checkout_step_one_displayed(self):
        """Checkout step one sayfası açıldı mı"""
        return "checkout-step-one" in self.get_current_url()
    
    def is_checkout_step_two_displayed(self):
        """Checkout step two sayfası açıldı mı"""
        return "checkout-step-two" in self.get_current_url()
    
    def fill_checkout_info(self, firstname, lastname, zipcode):
        """Checkout bilgilerini doldurur"""
        self.type(self.FIRSTNAME_INPUT, firstname)
        self.type(self.LASTNAME_INPUT, lastname)
        self.type(self.ZIPCODE_INPUT, zipcode)
    
    def click_continue(self):
        """Continue butonuna tıklar"""
        self.click(self.CONTINUE_BUTTON)
    
    def click_cancel(self):
        """Cancel butonuna tıklar"""
        self.click(self.CANCEL_BUTTON)
    
    def click_finish(self):
        """Finish butonuna tıklar"""
        self.click(self.FINISH_BUTTON)
    
    def is_order_complete(self):
        """Sipariş tamamlandı mı kontrol eder"""
        return self.is_element_visible(self.COMPLETE_HEADER)
    
    def get_complete_message(self):
        """Tamamlanma mesajını döner"""
        return self.get_text(self.COMPLETE_HEADER)
    
    def get_complete_text(self):
        """Tamamlanma alt metnini döner"""
        return self.get_text(self.COMPLETE_TEXT)
    
    def get_error_message(self):
        """Hata mesajını döner"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        """Hata mesajı görünür mü"""
        return self.is_element_visible(self.ERROR_MESSAGE)
    
    def get_subtotal(self):
        """Ara toplam değerini döner"""
        text = self.get_text(self.SUMMARY_SUBTOTAL)
        return text.split("$")[1] if "$" in text else "0"
    
    def get_tax(self):
        """Vergi değerini döner"""
        text = self.get_text(self.SUMMARY_TAX)
        return text.split("$")[1] if "$" in text else "0"
    
    def get_total(self):
        """Toplam değerini döner"""
        text = self.get_text(self.SUMMARY_TOTAL)
        return text.split("$")[1] if "$" in text else "0"
    
    def back_to_home(self):
        """Ana sayfaya dön"""
        self.click(self.BACK_HOME_BUTTON)
