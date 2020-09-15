import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import tag_live_preprocess
import time


keyword_dict={
    'anger': ['분노', '화남', '짜증'],
    'fear':['공포', '두려움'],
    'joy':['행복', '기쁨', '즐거움'],
    'love':['사랑', '사랑해'],
    'neutral':['일상','심심해','지루해'],
    'sadness':['우울','슬픔','눈물','울적'],
    'surprise':['놀람','깜짝']
    }

driver = webdriver.Chrome('C:/Users/dain8/Downloads/chromedriver_win32/chromedriver')
driver.implicitly_wait(5)

with open('tag_live.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(['keyword', 'tag', 'text'])

for keyword in keyword_dict:
    print('crawling '+keyword+'...')
    for tag in keyword_dict[keyword]:
        URL='https://www.taglive.net/tag/'+tag
        driver.get(URL)
        time.sleep(3)
        print('driver get request [URL : '+URL+']')
        result = driver.page_source
        soup = BeautifulSoup(result, 'html.parser')
        fennec = soup.select('#fennec')[0]
        articles_list=fennec.find_all('article')

        print(keyword+' '+tag+' preprocessing...')
        for article in articles_list:
            text=tag_live_preprocess.preprocess(article)

            print('append to tag_live.csv \n'+keyword+' '+tag+' '+text)
            with open('tag_live.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csvwriter=csv.writer(csvfile)
                csvwriter.writerow([keyword, tag, text])

driver.quit()