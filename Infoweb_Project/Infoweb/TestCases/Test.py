import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class News:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def newsFeed(self):
        try:
            self.driver.maximize_window()
            url = "http://sit.infoweb-website.kk-exchange.com:4010/"
            self.driver.get(url)

            while True:
                try:
                    wait = WebDriverWait(self.driver, 20)
                    news = wait.until(
                        EC.element_to_be_clickable((By.XPATH, "//*[@class='MuiGrid-root css-rfnosa']/div/nav/ul/li[3]/a/div")))

                    try:
                        news.click()
                    except Exception as e:
                        print(f"First click attempt failed: {e}")
                        self.driver.execute_script("arguments[0].click();", news)

                    # Switch to the iframe
                    iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "child-iframe")))

                    # Click the next button inside the iframe
                    self.next_news()

                    # Switch back to the default content
                    self.driver.switch_to.default_content()

                    # Wait for 2 seconds to read the news
                    time.sleep(2)

                except Exception as e:
                    print(f"An error occurred: {e}")
                    break


        finally:
            time.sleep(5)
            self.driver.quit()

    def next_news(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'MuiButton-textPrimary')]")))
            next_button.click()

        except Exception as e:
            print(f"Error during next news action: {e}")

# Instantiate and run the News class
news_instance = News()
news_instance.newsFeed()
