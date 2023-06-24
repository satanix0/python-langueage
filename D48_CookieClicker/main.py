import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Set the path to the webdriver executable file
driver_path = "chromedriver.exe"

# Create a Service object
service = Service(driver_path)

# Create an instance of the webdriver
driver = webdriver.Chrome(service=service)

# Navigate to the webpage
url = 'http://orteil.dashnet.org/experiments/cookie/'
driver.get(url)

while True:
    driver.find_element(by=By.ID, value="cookie").click()

# Close the webdriver
time.sleep(5)

# driver.close() # -- this only closes the current window
driver.quit()  # -- this only closes all the windows
