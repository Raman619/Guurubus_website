from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://gurubus.com.np/sign-in")

wait = WebDriverWait(driver, 15)

# Login
email = wait.until(
    EC.visibility_of_element_located((By.NAME, "email"))
)
email.send_keys("shrestharaman041@gmail.com")

password = wait.until(
    EC.visibility_of_element_located((By.NAME, "password"))
)
password.send_keys("RamaN619@")

login_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
login_button.click()

# Wait for page after login
time.sleep(5)

rent_vehicle = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, 'Rent Vehicles'))
)
rent_vehicle.click()

time.sleep(5)
viewdetails_button = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, 'View Details'))
)
viewdetails_button.click()

time.sleep(5)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

driver.execute_script("window.scrollBy(0, -1000);")
time.sleep(4)



time.sleep(5)
rentvehicle1_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/section[2]/div/div[1]/div[2]/button[1]"))
)
rentvehicle1_button.click()


time.sleep(5)
Fullname = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='John Doe']"))
)
Fullname.send_keys("Raman Shrestha")

time.sleep(2)

Phonenumber = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='9800000000']")
    )
)
Phonenumber.send_keys("9769366977")


time.sleep(5)
driver.quit()