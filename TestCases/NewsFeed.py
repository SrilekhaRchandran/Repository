from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewsFeed:
    def __init__(self, driver):
        self.driver = driver

    def newsFeed(self):
        try:
            # Wait for the button to be visible and clickable
            wait = WebDriverWait(self.driver, 10)

            news = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='__next']//main//div[1]//div[@class='MuiBox-root css-144ebsl']//nav//a//span")))
            news.click()

        #     # Check if the dialog/overlay is present
        #     dialog = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.MuiDialog-container")))
        #     if dialog.is_displayed():
        #         # If the dialog is present, try to click the button again
        #         button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.MuiButtonBase-root.MuiButton-root")))
        #         if button.is_enabled():
        #             button.click()
        #             print("Clicked on the news section")
        #         else:
        #             print("Button is not clickable")
        #     else:
        #         print("Dialog/overlay not found")
        #
        # except Exception as e:
        #     print(f"Error accessing news section: {e}")

        finally:
            self.driver.quit()