import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Set the path to the webdriver executable file
driver_path = "chromedriver.exe"

# Create a Service object
service = Service(driver_path)

# Create an instance of the webdriver
driver = webdriver.Chrome(service=service)


zillow_url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.97303236914063%2C%22east%22%3A-121.89362563085938%2C%22south%22%3A37.46037903522778%2C%22north%22%3A38.08886818258379%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"

driver.get(zillow_url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.prettify)

y = 1000
for n in range(5):
    driver.execute_script(f"window.scrollTo(0, {y});")
    y += 800
    time.sleep(0.5)


# bs4
# selecting using the attribute value
# retrieving the prices
all_price_elements = soup.select('span[data-test="property-card-price"]')
prices = [i.text.split('+')[0] for i in all_price_elements]

# retrieving addresses
all_addr_elements = soup.select(
    selector='address[data-test="property-card-addr"]')
addresses = [i.text for i in all_addr_elements]

# retrieving rental links using css selector by attribute and value
all_link_elements = soup.select('a[data-test="property-card-link"]')
links = []
for i in all_link_elements[::2]:
    links.append(f"https://www.zillow.com{i.get('href')}")


df = pd.DataFrame({'Price': prices,
                   'Address': addresses,
                   'Link':  links
                   })

# form_drive.close()
print(df)
