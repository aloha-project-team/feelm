from datetime import datetime, timedelta
import json
import csv
import os
from collection import fb_api

RESULT_DIRECTORY = '__resultes__/crawling'

# 전처리
def pre_precess(media):
    # timestamp UTC + 9 > KST
    kst = datetime.strptime(media['timestamp'], '%Y-%m-%dT%H:%M:%S+0000')
    kst = kst + timedelta(hours=+9)
    media['timestamp'] = kst.strftime('%Y-%m-%d %H:%M:%S')

# 게시물 id 크롤링
def crawling(pagename, since, until):

    print("clawler.py is running...")

    #instagram id 가져오기
    instagram_id=fb_api.fb_name_to_ig_id(pagename)
    print("instagram_id : "+instagram_id)

    #file name
    info_filename = '%s/ig_info_%s.json' % (RESULT_DIRECTORY, instagram_id)
    media_filename = '%s/ig_media_%s.json' % (RESULT_DIRECTORY, instagram_id)

    #instagram basic info crawling
    print("crawling id "+instagram_id+" basic information...")
    ig_basic_info=fb_api.ig_basic_info(instagram_id, since, until)

    print("writing id "+instagram_id+" basic information as outfile...")
    with open(info_filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(ig_basic_info, indent=4, sort_keys=True, ensure_ascii=False )
        outfile.write(json_string)
    print("id "+instagram_id+" basic information was saved as "+info_filename)

    #instagram media id list crawling
    print("crawling id "+instagram_id+" media...")
    result = []
    for posts in fb_api.ig_media_list(instagram_id, since, until):
        for post in posts:
            result.append(fb_api.ig_media(post['id']))
    
    print("pre-processing... (UTC > KST)")
    for media in result:
        pre_precess(media)
    
    print("writing id "+instagram_id+" media as outfile...")
    with open(media_filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False )
        outfile.write(json_string)
    print("id "+instagram_id+" media was saved as "+media_filename)

# 현재 OS에 매개변수로 받은 이름의 디렉터리가 없다면 디렉터리를 생성하라.
if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)