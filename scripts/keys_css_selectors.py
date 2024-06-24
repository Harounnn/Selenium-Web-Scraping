import time

from selenium import webdriver
from selenium.webdriver.chrome import service

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

webdriver_service = service.Service(r"D:\Scraping\Drivers\operadriver_win64\operadriver.exe")
webdriver_service.start()

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Users\Harou\AppData\Local\Programs\Opera GX\opera.exe"
options.add_experimental_option('w3c', True)

driver = webdriver.Remote(webdriver_service.service_url, options=options)

driver.get('https://www.youtube.com')

driver.implicitly_wait(60)

search_input = driver.find_element(By.XPATH, '//input[@id="search"]')
search_input.click()
search_input.send_keys("ML course")

time.sleep(5)

search_btn = driver.find_element(By.CSS_SELECTOR, 'button[id="search-icon-legacy"]')
search_btn.click()

time.sleep(10)
