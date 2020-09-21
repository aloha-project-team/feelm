import pandas as pd
import numpy as np
import csv
import requests

from bs4 import BeautifulSoup
from selenium import webdriver

import time

# 변경된 url을 저장할 df 생성
df1= pd.DataFrame(columns = ['url'])
# 크롬드라이버 경로 설정
# driver = webdriver.Chrome('C:/Users/husky/Documents/워밍업/code/feelm/crawling_music_list/chromedriver')

driver = webdriver.Chrome('C:/Users/husky/Documents/워밍업/code/feelm/crawling_taglive/chromedriver')
# 암묵적으로 웹 자원 로드가 될때까지 기다려주는 시간
driver.implicitly_wait(5)
# pandas형태로 csv파일을 읽어옴
df = pd.read_csv("./sed_music_list.csv")

idx=0
for music in df["music"]:
    
    # -예외처리-
    # "#이 있는 음악은 전처리"
    if "#"  in music:
        music = music.replace("#", "")
    if "("  in music:
        music = music.replace("(", "")
    # 3글자 이하의 제목은 제외
    if len(music)<3:
        continue

    singer=df['singer'][idx]

    # URL 접근
    URL=f'https://www.youtube.com/results?search_query={music} {singer}'
    driver.get(URL)
    time.sleep(0.5)

    print('driver get request [URL : '+URL+']')

    # 검색된 내용 중 링크 텍스트에 "music" 이 포함된 것을 찾음
    continue_link = driver.find_element_by_partial_link_text(music[:2])
    # csv에 저장된 제목과 일치하지 않는 것도 있기에, 2글자와 같으면 클릭
    
    # 해당 링크를 클릭한다.
    continue_link.click()
    time.sleep(0.5)

    #크롬드라이버의 현재 url 저장
    music_url = driver.current_url # str타입
    
    # 웹에서 사용되게 url form을 바꿈
    music_url = music_url.replace("watch?v=","embed/")

    # 바꾼 url을 df1에 행 추가
    df1.loc[idx,'url'] = music_url
    idx+=1
    print(df1)
    if(idx==3):
        break
    # print(df1)

# csv로 저장
df1.to_csv("./sed_url.csv",index=False, mode='w')

driver.quit()

#변경된 유튜브 링크는 sum_csv.csv라는 파일에 감정별로 링크를 모아뒀어요