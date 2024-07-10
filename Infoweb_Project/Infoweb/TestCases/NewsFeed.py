import time
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewsFeed:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_news_page(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            news = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[@class='MuiGrid-root css-rfnosa']/div/nav/ul/li[3]/a/div"))
            )

            try:
                news.click()
            except ElementClickInterceptedException as e:
                print(f"First click attempt failed: {e}")
                self.driver.execute_script("arguments[0].click();", news)
        except TimeoutException as e:
            print(f"Timeout while waiting for the news element: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def navigate_next_news(self):
        try:
            # Switch to the iframe
            iframe = self.switch_to_news_iframe()

            # Click the next button inside the iframe
            self.click_next_button()

            # Switch back to the default content
            self.driver.switch_to.default_content()

            # Wait for 2 seconds to read the news
            time.sleep(2)

        except Exception as e:
            print(f"Error during next news action: {e}")

    def switch_to_news_iframe(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "child-iframe")))
            return iframe
        except Exception as e:
            print(f"Error while switching to iframe: {e}")

    def click_next_button(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'MuiButton-textPrimary')]")))
            next_button.click()
        except Exception as e:
            print(f"Error clicking next button: {e}")

    def newsFeed(self):
        try:
            self.navigate_to_news_page()

            while True:
                self.navigate_next_news()

                #Acting as infinite while loop because, As per the development, The news keep on looping

        finally:
            time.sleep(5)
