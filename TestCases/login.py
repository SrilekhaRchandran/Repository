import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Login:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self, phone, password):
        try:
            self.driver.maximize_window()
            url = "http://sit.infoweb-website.kk-exchange.com:4010/"
            self.driver.get(url)

            wait = WebDriverWait(self.driver, 20)

            # Wait for the login button to be clickable
            try:
                login_button = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//button[./p[text()='Login']]")))
                login_button.click()

            except TimeoutException:
                print("TimeoutException: Unable to locate login button")
                print(self.driver.page_source)
                return

            # PhoneNumber
            phone_field = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='__next']/div/main/div/div/div[2]/div[2]/div[2]/div[1]/form/div[2]/div/div/div[2]/input")))
            phone_field.send_keys(phone)

            # Password
            password_field= wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input#outlined-adornment-password")))
            password_field.send_keys(password)

            # Submit button
            submit = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='__next']/div/main/div/div/div[2]/div[2]/div[2]/div[1]/form/div[5]/div[2]/button")))
            submit.click()

            time.sleep(5)

        finally:
            self.driver.quit()







