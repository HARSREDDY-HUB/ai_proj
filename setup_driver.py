from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

def setup_chrome_driver():
    """Setup and return ChromeDriver using webdriver_manager"""
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    return webdriver.Chrome(service=service, options=options)
