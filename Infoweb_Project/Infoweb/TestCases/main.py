from selenium import webdriver
from login import Login
from NewsFeed import NewsFeed


def main():
    driver = webdriver.Chrome()

    try:
        # Perform login
        login_instance = Login(driver)
        login_instance.login("965252690", "a123456")

        # Navigate to the news page
        news_instance = NewsFeed(driver)
        news_instance.newsFeed()

    finally:
        # Close the driver after all actions are completed
        driver.quit()


if __name__ == "__main__":
    main()
