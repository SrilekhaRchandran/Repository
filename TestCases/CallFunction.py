from login import Login
from NewsFeed import NewsFeed

login_instance = Login()
login_instance.login("965252690", "a123456")

news_instance = NewsFeed(login_instance.driver)
news_instance.newsFeed()