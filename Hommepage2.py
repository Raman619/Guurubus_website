from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()

driver.get("https://gurubus.com.np/sign-in")

wait = WebDriverWait(driver, 10)

# Wait for email field
email = wait.until(
    EC.visibility_of_element_located((By.NAME, "email"))
)
email.send_keys("shrestharaman041@gmail.com")

# Wait for password field
password = wait.until(
    EC.visibility_of_element_located((By.NAME, "password"))
)
password.send_keys("RamaN619@")

# Wait for login button and click
login_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
login_button.click()

# Wait for login/navigation to complete
wait.until(EC.url_changes("https://gurubus.com.np/sign-in"))

time.sleep(30)
search = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type = 'text'])[1]"))
)
search.send_keys("kathmandu")

search = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type = 'text'])[2]"))
)
search.send_keys("pokhara")



time.sleep(30)
driver.quit
