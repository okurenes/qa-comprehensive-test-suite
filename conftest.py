import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import Config

def pytest_configure(config):
    """Pytest başlarken custom marker'ları kaydeder"""
    config.addinivalue_line("markers", "smoke: Smoke tests")
    config.addinivalue_line("markers", "regression: Regression tests")
    config.addinivalue_line("markers", "ui: UI tests")
    config.addinivalue_line("markers", "api: API tests")
    config.addinivalue_line("markers", "db: Database tests")
    config.addinivalue_line("markers", "critical: Critical path tests")

@pytest.fixture(scope="function")
def driver():
    """UI testleri için WebDriver fixture"""
    options = Options()

    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")

    if Config.HEADLESS:
        options.add_argument("--headless=new")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])

    # Selenium Manager (Selenium 4.6+) otomatik olarak uygun ChromeDriver'ı indirir
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(Config.TIMEOUT)

    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    """Base URL fixture"""
    return Config.BASE_URL

@pytest.fixture(scope="session")
def api_base_url():
    """API Base URL fixture"""
    return Config.API_BASE_URL
