import selenium.webdriver as webdriverffrom selenium.webdriver.chrome.service 
import service
import time

def scrape_website(website):
    print("launching chrome browser...")

    chrome_driver_path=r"D:\OneDrive\Desktop\web scraper code\chromedriver.exe"
    
    options= webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=chrome_driver_path,options=options)

    try:
        driver.get(website)
        print("page loaded...")
        html=driver.page_source
r.page_source
r.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()