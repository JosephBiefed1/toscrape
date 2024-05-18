from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import time

with open('valid_proxies.txt', 'r') as f:
    ip_addresses  = f.read().split("\n")

# define custom options for the Selenium driver
# free proxy server URL
i=0
while True:
    
    try:
        options = Options()

        proxy_server_url = ip_addresses[i]
        options.add_argument(f'--proxy-server={proxy_server_url}')
        options.add_argument('ignore-certificate-errors')
        # create the ChromeDriver instance with custom options
        options.add_argument('--disable-aia-fetching')
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        
        driver.get("https://quotes.toscrape.com/search.aspx")
        
        if "Quotes to Scrape" == driver.title:
            break

        

    
    except:
        print("Error, looking for another proxy")
        i+=1


def pagination():
    quotes = driver.find_elements(By. CLASS_NAME, "quote")
    for quote in quotes:
        soup = BeautifulSoup(quote.text, "html.parser")
        print(soup.prettify())
def tags():
    tags_name = driver.find_element(By. CLASS_NAME, "tags-box")
    tags = tags_name.find_elements(By.CLASS_NAME, "tag-item")
    for tag in tags:
        print(tag.find_element(By. TAG_NAME, "a").get_attribute("href"))

def infinitescroll():
    SCROLL_PAUSE_TIME = 5
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 5);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height    



def wait_js():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. CLASS_NAME, "quote")))
    loaded = driver.find_elements(By. CLASS_NAME, "quote")
    for load in loaded:
        print(load.text)

