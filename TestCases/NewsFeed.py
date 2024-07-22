import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class NewsFeed:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_news_page(self):
        wait = WebDriverWait(self.driver, 20)
        news = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='MuiGrid-root css-rfnosa']/div/nav/ul/li[3]/a/div"))
        )
        news.click()

    def navigate_next_news(self):
        iframe = self.switch_to_news_iframe()
        self.click_next_button()
        self.driver.switch_to.default_content()
        time.sleep(2)

    def switch_to_news_iframe(self):
        wait = WebDriverWait(self.driver, 20)
        iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "child-iframe")))
        return iframe

    def click_next_button(self):
        wait = WebDriverWait(self.driver, 20)
        try:
            next_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'MuiButton-textPrimary') and contains(text(), 'Next')]")))
            next_button.click()
        except TimeoutException:
            raise NoSuchElementException("Next button not found")

    def newsFeed(self):
        self.navigate_to_news_page()

        try:
            while True:
                self.navigate_next_news()
        except NoSuchElementException:
            print("No more news articles. Exiting..")
        finally:
            time.sleep(5)
            self.driver.quit()
