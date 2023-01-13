from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 
service = Service(executable_path="/usr/local/share/chrome_driver/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.selenium.dev/")

assert "Selenium" in driver.title
print("Test successful")