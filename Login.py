from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import time

CREDENTIALS_FILE = "gurubus_credentials.json"


def load_credentials():
    email = os.getenv("GURUBUS_EMAIL")
    password = os.getenv("GURUBUS_PASSWORD")

    if email and password:
        return email, password

    if os.path.exists(CREDENTIALS_FILE):
        try:
            with open(CREDENTIALS_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                email = data.get("email")
                password = data.get("password")
                if email and password:
                    return email, password
        except Exception:
            pass

    sample = {
        "email": "your_email@example.com",
        "password": "your_password"
    }

    with open(CREDENTIALS_FILE, "w", encoding="utf-8") as file:
        json.dump(sample, file, indent=4)

    raise RuntimeError(
        f"No saved Gurubus credentials found. Please update '{CREDENTIALS_FILE}' and run again."
    )


def login_to_gurubus(email: str, password: str):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)

    try:
        driver.get("https://gurubus.com.np/sign-in")

        email_field = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        email_field.clear()
        email_field.send_keys(email)

        password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        password_field.clear()
        password_field.send_keys(password)

        submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        submit_button.click()

        time.sleep(3)
        print("Login attempted successfully. Browser is open.")
        return driver

    except Exception as e:
        driver.quit()
        raise RuntimeError(f"Login failed: {e}")


if __name__ == "__main__":
    email, password = load_credentials()
    driver = login_to_gurubus(email, password)

    input("Press Enter to close the browser...")
    driver.quit()
