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


url = "https://www.google.com/search?q=-+site:youtube.com+openinapp.co&rlz=1C1CHBF_enIN1036IN1036&sxsrf=APwXEdfAkfV4kM2RuR9l164BYoYQyD9hxA:1681541575293&ei=x0k6ZLPEEajv4-EPg6yb4A0&start=0&sa=N&ved=2ahUKEwjzw5TCpqv-AhWo9zgGHQPWBtw4KBDy0wN6BAgFEAQ&biw=1536&bih=746&dpr=1.25"

driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup.prettify)

# bs4
# selecting using the attribute value
# retrieving the prices


# retrieving rental links using css selector by attribute and value
all_link_elements = soup.select(selector=".MjjYud > a")
links = []
for i in all_link_elements:
    links.append(i.get('href'))

print(links)
