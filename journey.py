from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path="/usr/local/share/chrome_driver/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.selenium.dev/")

assert "Selenium" in driver.title