from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# import pandas as pd

service = Service('/home/eytan/Selenium')
driver = webdriver.Chrome(service=service)

driver.get("https://www.elal.com")

titles = driver.find_elements(By.CLASS_NAME, 'article-title')
for title in titles:
    print(title.text)

driver.close()