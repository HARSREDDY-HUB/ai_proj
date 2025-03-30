from selenium import webdriver
import time
from setup_driver import setup_chrome_driver
from bs4 import BeautifulSoup
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

def extract_body_content(html_content):
    soup=BeautifulSoup(html_content,"html.parser")
    body_content=soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup= BeautifulSoup(body_content,"html.parser")

    for script_or_style in soup(["scripts","style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content="\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    return cleaned_content
def split_dom_content(dom_content,max_length=6000):
    return[dom_content[i: i + max_length]for i in range(0, len(dom_content),max_length)]
