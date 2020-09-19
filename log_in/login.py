import requests
from bs4 import BeautifulSoup
from selenium import webdriver

instagram_app_id='783139315754863'
redirect_uri='http://127.0.0.1:8000/'
scope='user_profile'
url=f'https://api.instagram.com/oauth/authorize?client_id={instagram_app_id}&redirect_uri={redirect_uri}&scope={scope}&response_type=code'

driver = webdriver.Chrome('C:/Users/dain8/Downloads/chromedriver_win32/chromedriver')
driver.implicitly_wait(5)

driver.get(url)

response=requests.post(url)
print(url)