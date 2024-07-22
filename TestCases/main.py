import unittest
from selenium import webdriver
from login import Login
from NewsFeed import NewsFeed

class TestMain(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_and_news_feed(self):
        login_instance = Login(self.driver)
        login_success = login_instance.login("965252690", "a123456")
        self.assertTrue(login_success, "Login failed")

        if login_success:
            news_instance = NewsFeed(self.driver)
            news_instance.newsFeed()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
