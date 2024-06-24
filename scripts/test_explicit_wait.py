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

driver.get('https://e-s-tunis.com/fr')

prev_icon = driver.find_element(By.CLASS_NAME, "icon-page-prev")

WebDriverWait(driver, 120).until(
    EC.url_changes("https://e-s-tunis.com/fr")
)

print("success")

driver.quit()