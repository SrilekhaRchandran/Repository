import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self, phone, password):
        try:
            self.driver.maximize_window()
            url = "http://sit.infoweb-website.kk-exchange.com:4010/"
            self.driver.get(url)

            wait = WebDriverWait(self.driver, 20)

            login_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[./p[text()='Login']]")))
            login_button.click()

            try:
                login_button = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//button[./p[text()='Login']]")))
                login_button.click()
            except TimeoutException:
                print("TimeoutException: Unable to locate login button")
                self.debug_page_source("login_button_not_found")
                return False

            phone_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div/div/div[2]/div[2]/div[2]/div[1]/form/div[2]/div/div/div[2]/input")))
            phone_field.send_keys(phone)

            password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#outlined-adornment-password")))
            password_field.send_keys(password)

            submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div/div/div[2]/div[2]/div[2]/div[1]/form/div[5]/div[2]/button")))
            submit.click()

            # Adding an assertion to verify login success
            time.sleep(5)
            return True

        except Exception as e:
            print(f"An error occurred during login: {e}")
            # self.debug_page_source("login_exception")
            return False

    # def debug_page_source(self, name):
    #     with open(f"debug_page_source_{name}.html", "w", encoding="utf-8") as f:
    #         f.write(self.driver.page_source)
