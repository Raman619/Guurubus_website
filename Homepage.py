from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://gurubus.com.np/sign-in")

wait = WebDriverWait(driver, 10)

driver.find_element(By.NAME,"email").send_keys("shrestharaman041@gmail.com")
driver.find_element(By.NAME,"password").send_keys("RamaN619@")
driver.find_element(By.XPATH,"//button[@ type='submit']").click()

wait = WebDriverWait(driver, 10)
