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
time.sleep(2)

# FROM field
from_city = wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]"))
)
from_city.send_keys("Kathmandu")

# TO field
to_city = wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[2]"))
)
to_city.send_keys("Pokhara")


tomorrow_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(., 'Tomorrow')]")
    )
)
tomorrow_button.click()

time.sleep(2)

SearchBuses_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
SearchBuses_button.click()

time.sleep(2)

date_button = wait.until(
    EC.element_to_be_clickable( (By.XPATH, "//button[.//span[normalize-space()='Thu'] and .//span[normalize-space()='10'] and .//span[normalize-space()='Sep']]") )
)

date_button.click()

time.sleep(1)
# Then Book Now
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

driver.execute_script("window.scrollBy(0, -500);")
time.sleep(1)


driver.execute_script("window.scrollBy(0, -500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, -500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, -500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, -200);")


time.sleep(1)# Wait for first Book Now button
# Wait for first Book Now button
book_button = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "(//button[normalize-space()='Book Now'])[1]")
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    book_button
)

time.sleep(1)

driver.execute_script(
    "arguments[0].click();",
    book_button
)
# Click Book Now


time.sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

driver.execute_script("window.scrollBy(0, -500);")
time.sleep(1)


driver.execute_script("window.scrollBy(0, -500);")
time.sleep(1)

driver.execute_script("window.scrollBy(0, -200);")



time.sleep(2)



seat_b1 = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[.//span[normalize-space()='B1']]")
    )
)

seat_b1.click()

time.sleep(1)

seat_b2= wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[.//span[normalize-space()='B2']]")
    )
)

seat_b2.click()
time.sleep(1)


seat_b3 = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[.//span[normalize-space()='B3']]"))
)

seat_b3.click()
time.sleep(1)

seat_b4 = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[.//span[normalize-space()='B4']]"))
)

seat_b4.click()

time.sleep(1)



driver.execute_script("window.scrollBy(0, 700);")

time.sleep(1)

Continue_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Continue to Passenger Details']")
    )
)

Continue_button.click()

time.sleep(1)

Fullname1 = wait.until(
    EC.visibility_of_element_located(
        (By.NAME, "passengerName"))
)
Fullname1.click()

time.sleep(1)

Enteremail1 = wait.until(
    EC.visibility_of_element_located(
        (By.NAME, "passengerEmail"))
)
Enteremail1.click()
time.sleep(1)


driver.execute_script("window.scrollBy(0, 200);")
time.sleep(1)


Phonenumber1 = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "(//input[@type='tel'])[1]"))
)
Phonenumber1.click()
time.sleep(1)



driver.execute_script("window.scrollBy(0, 200);")

time.sleep(1)
Contactnumber1 = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder= 'Enter your contact number']")
    )
)
Contactnumber1.send_keys("9769366977")

time.sleep(1)
Proceed_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//button[@type='submit'])[1]"))
)
Proceed_button.click()
time.sleep(3)



# Wait until booking page opens



driver.quit()

