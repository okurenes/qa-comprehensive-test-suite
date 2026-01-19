from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BasePage:
    """Tüm page object'lerin inherit edeceği gelişmiş base class"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
    
    def find_element(self, locator, timeout=10):
        """Element bulur ve döner"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            logger.info(f"Element bulundu: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Element bulunamadı: {locator}")
            raise
    
    def find_elements(self, locator, timeout=10):
        """Birden fazla element bulur"""
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            logger.info(f"{len(elements)} element bulundu: {locator}")
            return elements
        except TimeoutException:
            logger.error(f"Elementler bulunamadı: {locator}")
            return []
    
    def click(self, locator, timeout=10):
        """Element'e tıklar"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            logger.info(f"Element'e tıklandı: {locator}")
        except Exception as e:
            logger.error(f"Tıklama hatası: {locator}, Hata: {str(e)}")
            raise
    
    def type(self, locator, text, timeout=10):
        """Element'e text yazar"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        logger.info(f"Text yazıldı: {locator}")
    
    def get_text(self, locator, timeout=10):
        """Element'in text'ini döner"""
        element = self.find_element(locator, timeout)
        text = element.text
        logger.info(f"Text alındı: {text}")
        return text
    
    def is_element_visible(self, locator, timeout=10):
        """Element görünür mü kontrol eder"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def is_element_present(self, locator):
        """Element DOM'da var mı kontrol eder"""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
    
    def wait_for_element_to_disappear(self, locator, timeout=10):
        """Element kaybolana kadar bekler"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            logger.info(f"Element kayboldu: {locator}")
            return True
        except TimeoutException:
            logger.warning(f"Element hala görünür: {locator}")
            return False
    
    def hover(self, locator, timeout=10):
        """Element üzerine hover yapar"""
        element = self.find_element(locator, timeout)
        self.actions.move_to_element(element).perform()
        logger.info(f"Element'e hover yapıldı: {locator}")
    
    def scroll_to_element(self, locator, timeout=10):
        """Element'e scroll yapar"""
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        logger.info(f"Element'e scroll yapıldı: {locator}")
    
    def get_current_url(self):
        """Mevcut URL'i döner"""
        return self.driver.current_url
    
    def get_page_title(self):
        """Sayfa başlığını döner"""
        return self.driver.title
    
    def take_screenshot(self, filename):
        """Screenshot alır"""
        self.driver.save_screenshot(f"reports/{filename}.png")
        logger.info(f"Screenshot alındı: {filename}")
