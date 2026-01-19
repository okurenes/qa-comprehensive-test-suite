from selenium.webdriver.common.by import By
from ui_tests.pages.base_page import BasePage

class ProductsPage(BasePage):
    """Ürünler sayfası için Page Object"""
    
    # Locators
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[id^='remove']")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_products_page_displayed(self):
        """Ürünler sayfası açıldı mı kontrol eder"""
        return self.is_element_visible(self.PRODUCTS_TITLE)
    
    def get_products_count(self):
        """Sayfadaki ürün sayısını döner"""
        return len(self.find_elements(self.INVENTORY_ITEMS))
    
    def get_product_names(self):
        """Tüm ürün isimlerini liste olarak döner"""
        elements = self.find_elements(self.INVENTORY_ITEM_NAME)
        return [element.text for element in elements]
    
    def get_product_prices(self):
        """Tüm ürün fiyatlarını liste olarak döner"""
        elements = self.find_elements(self.INVENTORY_ITEM_PRICE)
        return [element.text for element in elements]
    
    def add_product_to_cart_by_index(self, index=0):
        """Index numarasına göre ürünü sepete ekler"""
        buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        if buttons and len(buttons) > index:
            buttons[index].click()
    
    def add_all_products_to_cart(self):
        """Tüm ürünleri sepete ekler"""
        buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        for button in buttons:
            button.click()
    
    def remove_product_from_cart_by_index(self, index=0):
        """Index numarasına göre ürünü sepetten çıkarır"""
        buttons = self.find_elements(self.REMOVE_BUTTONS)
        if buttons and len(buttons) > index:
            buttons[index].click()
    
    def get_cart_badge_count(self):
        """Sepet badge'indeki sayıyı döner"""
        try:
            return int(self.get_text(self.SHOPPING_CART_BADGE))
        except:
            return 0
    
    def go_to_cart(self):
        """Sepet sayfasına gider"""
        self.click(self.SHOPPING_CART_LINK)
    
    def logout(self):
        """Logout yapar"""
        self.click(self.BURGER_MENU)
        self.click(self.LOGOUT_LINK)
