import time

from selenium import webdriver
from selenium.webdriver.chrome import service

from selenium.webdriver.common.by import By

webdriver_service = service.Service(r"D:\Scraping\Drivers\operadriver_win64\operadriver.exe")
webdriver_service.start()

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Users\Harou\AppData\Local\Programs\Opera GX\opera.exe"
options.add_experimental_option('w3c', True)

driver = webdriver.Remote(webdriver_service.service_url, options=options)

driver.get('https://www.google.com/')

time.sleep(5)  
#driver.implicitly_wait(5)
driver.quit()