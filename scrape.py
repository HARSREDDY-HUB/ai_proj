from selenium import webdriver
import time
from setup_driver import setup_chrome_driver

def scrape_website(website):
    print("launching chrome browser...")
    
    driver = setup_chrome_driver()

    try:
        driver.get(website)
        print("page loaded...")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()