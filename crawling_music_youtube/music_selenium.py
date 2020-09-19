import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import time


driver = webdriver.Chrome('C:/Users/husky/Documents/워밍업/code/feelm/crawling_taglive/chromedriver')
driver.implicitly_wait(5)

with open('happiness2_music_list.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(['music', 'singer'])

tag = "우울"

for idx in range(1, 400, 50):
    URL=f'https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=476035128#params%5BplylstSeq%5D=429411613&po=pageObj&startIndex={idx}'
    driver.get(URL)
    time.sleep(3)
    print('driver get request [URL : '+URL+']')
    result = driver.page_source
    soup = BeautifulSoup(result, 'html.parser')
    td_list = soup.select('#frm > div > table > tbody > tr')

    for td in td_list:
        music = td.select_one("td:nth-of-type(5) > div > div > div.ellipsis.rank01 > span > a").text
        singer = td.select_one("td:nth-of-type(5) > div > div > div.ellipsis.rank02 > a").text
        
        # print(music)

        with open('joy_music_list.csv', 'a', newline='', encoding='utf-8') as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow([music, singer])

driver.quit()