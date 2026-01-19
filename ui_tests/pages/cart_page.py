from selenium.webdriver.common.by import By
from ui_tests.pages.base_page import BasePage

class CartPage(BasePage):
    """Sepet sayfası için Page Object"""
    
    # Locators
    CART_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CART_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[id^='remove']")
    CART_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_cart_page_displayed(self):
        """Sepet sayfası açıldı mı kontrol eder"""
        return self.is_element_visible(self.CART_TITLE)
    
    def get_cart_items_count(self):
        """Sepetteki ürün sayısını döner"""
        return len(self.find_elements(self.CART_ITEMS))
    
    def get_cart_item_names(self):
        """Sepetteki ürün isimlerini liste olarak döner"""
        elements = self.find_elements(self.CART_ITEM_NAME)
        return [element.text for element in elements]
    
    def get_cart_item_prices(self):
        """Sepetteki ürün fiyatlarını liste olarak döner"""
        elements = self.find_elements(self.CART_ITEM_PRICE)
        return [element.text for element in elements]
    
    def proceed_to_checkout(self):
        """Checkout sayfasına ilerler"""
        self.click(self.CHECKOUT_BUTTON)
    
    def continue_shopping(self):
        """Alışverişe devam et"""
        self.click(self.CONTINUE_SHOPPING)
    
    def remove_item_by_index(self, index=0):
        """Index numarasına göre ürünü sepetten çıkarır"""
        buttons = self.find_elements(self.REMOVE_BUTTONS)
        if buttons and len(buttons) > index:
            buttons[index].click()
    
    def remove_all_items(self):
        """Sepetteki tüm ürünleri çıkarır"""
        while self.get_cart_items_count() > 0:
            self.remove_item_by_index(0)
    
    def is_cart_empty(self):
        """Sepet boş mu kontrol eder"""
        return self.get_cart_items_count() == 0
