import pandas as pd
import numpy as np
import csv
import requests

from bs4 import BeautifulSoup
from selenium import webdriver

import time

driver = webdriver.Chrome('C:/Users/gmlrn/Desktop/hg/chromedriver')
driver.implicitly_wait(5)

df = pd.read_csv("./love_music_list.csv")

url = []

# print(df[:20])


for music in df["music"]:

    if "#" in music:
        music = music.replace("#", "")

    URL=f'https://www.youtube.com/results?search_query={music}'
    driver.get(URL)
    time.sleep(3)
    print('driver get request [URL : '+URL+']')
    result = driver.page_source
    soup = BeautifulSoup(result, 'html.parser')

    music_url = soup.select('#video-title')[0]["href"]

    music_url = str(music_url).replace("watch?v=", "embed/")

    url.append(music_url)


df["url"] = url

print(df["url"])

df.to_csv("./add_url.csv", sep=",", index=False, columns=["music", "singer", "url"])

driver.quit()