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
time.sleep(1)


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)


driver.execute_script("window.scrollBy(0, -150)")
time.sleep(1)
main_window = driver.current_window_handle
Facebook = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@aria-label='Facebook']") )
)

Facebook.click()
time.sleep(1)

for window in driver.window_handles:
    if window != main_window:
        driver.switch_to.window(window)
        break

print("Facebook:", driver.current_url)

# Close Facebook tab
driver.close()

# Switch back to GuruBus
driver.switch_to.window(main_window)

time.sleep(1)


# =========================
# TWITTER
# =========================

Twitter = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@aria-label='Twitter']")
    )
)

Twitter.click()

time.sleep(1)

# Switch to new Twitter tab
for window in driver.window_handles:
    if window != main_window:
        driver.switch_to.window(window)
        break

print("Twitter:", driver.current_url)

# Close Twitter tab
driver.close()

# Switch back to GuruBus
driver.switch_to.window(main_window)

time.sleep(1)
Instagram = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@aria-label='Instagram']")
    )
)
Instagram.click()

# Switch to Instagram new tab
for window in driver.window_handles:
    if window != main_window:
        driver.switch_to.window(window)
        break

print("Instagram:", driver.current_url)


time.sleep(1)
# Close Instagram tab
driver.close()

# Switch back to GuruBus
driver.switch_to.window(main_window)

time.sleep(1)

Explore_section = wait.until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Explore Trips"))
)
Explore_section.click()


time.sleep(4)

driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)


driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, 200);")

time.sleep(2)
driver.back()
driver.refresh()

time.sleep(2)


Blogs_section = wait.until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Blogs"))
)
Blogs_section.click()


time.sleep(4)

driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)


driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, 200);")

time.sleep(2)
driver.back()
driver.refresh()

time.sleep(2)


Contact_section = wait.until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Contact"))
)
Contact_section.click()


time.sleep(4)

driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)


driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, 200);")

time.sleep(2)

driver.back()
driver.refresh()

time.sleep(2)

Myticket_section = wait.until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "My Tickets"))
)
Myticket_section.click()


time.sleep(4)

driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)


driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, 200);")

time.sleep(2)

driver.back()
driver.refresh()

MyRefund_section = wait.until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "My Refunds"))
)
MyRefund_section.click()


time.sleep(4)

driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)


driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)
driver.execute_script("window.scrollBy(0, 200);")

time.sleep(2)

driver.back()
driver.refresh()

time.sleep(2)

Googleplay_button = wait .until(
    EC.element_to_be_clickable ((By.XPATH, "//a[@href='https://play.google.com/store/search?q=gurubus&c=apps']"))
)
Googleplay_button.click()
time.sleep(2)

driver.back()
driver.refresh()

time.sleep(2)
driver.quit()
