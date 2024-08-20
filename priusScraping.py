from bs4 import BeautifulSoup
import requests

#load page
URL = "https://www.tampahybrids.com/listings"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

links = soup.find_all('a')
for link in links:

    #links doubled
    #get rid of vflyer
    url = link.get('href')
    print(url)

"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument(f'--user-agent={custom_user_agent}')
#options.add_argument('--headless')


driver = webdriver.Chrome(
    options=options,
)

# visit the desired page
driver.get("https://www.nuvoautosales.com/details/used-2012-lexus-ct-200h/106032994")

user_agent_info = driver.find_element(By.CLASS_NAME, "vdp-info-block__info-item-description js-vin-message").text


print(user_agent_info)

driver.quit()"""