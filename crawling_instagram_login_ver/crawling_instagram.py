from datetime import datetime, timedelta
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
import json
import os

# 0. html에서 버튼 눌러 로그인 하면 url 매개변수로 > Authorization_Code 를 받는다
# 1. Authorization_Code 로 Access_Token과 instagram_id를 받는다
# 2. instagram_id와 Access_Token으로 사용자의 프로필과 게시글을 받는다.

RESULT_DIRECTORY = 'resultes'
BASE_URL_FB_API = 'https://graph.facebook.com/v8.0'

# 현재 OS에 매개변수로 받은 이름의 디렉터리가 없다면 디렉터리를 생성하라.
if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)

# 0.
Authorization_Code='AQDe7fNMRbzv2872NWOra7uBnORtRi-C86JtCPKhiGNciZ4NURSH34XpSM6JxVR3koSdaB7JmtmRU07BoN7nQMiqm76sLgPix1_7MbqJljoW0hakDdGf63VJmSKIWygTcAt3CchaRh2vJpoPFedQQFLQ6ZTNMbyANBYsjbdZYP_KU6IuA-j2rr_2BcDfvqQ8En1tlmaefKueTseJeuwf7wYjrtajvlsoUmgumMewyKzJaw'


# 1. Authorization_Code 로 Access_Token과 instagram_id를 받는다
# 1. access_token 과 id 가 담긴 json 파일 리턴
def code_to_token(Authorization_Code):
    print('generate ACCESS_TOKEN by Authorization_Code...')
    files = {
        'client_id': (None, '783139315754863'),
        'client_secret': (None, '0f3f5f749cbfbbf54c8ad1e980ff5293'),
        'grant_type': (None, 'authorization_code'),
        'redirect_uri': (None, 'https://127.0.0.1:8000/result/'),
        'code': (None, Authorization_Code),
    }
    response = requests.post('https://api.instagram.com/oauth/access_token', files=files)
    json_result=json.loads(response.text)
    print('Success to generate ACCESS_TOKEN!')
    return json_result

# 여러 파라미터에 대하여, url을 생성
def fb_generate_url(base = BASE_URL_FB_API, node = '', **param):
    return '%s/%s/?%s' % (base, node, urlencode(param))

# API instagram id > instagram url
def ig_basic_info(id, access_token):
    response = requests.get('https://graph.instagram.com/'+str(id)+'?fields=id,account_type,media_count,username&access_token='+access_token)
    json_result=json.loads(response.text)
    print('\n------------basic info result------------')
    print(json_result)
    print('\n')
    return json_result

def ig_media_list(id, access_token, since, until):
    isnext = True
    while isnext is True:
        response = requests.get('https://graph.instagram.com/'+str(id)+'?fields=media&access_token='+access_token)
        json_result=json.loads(response.text)
        try:
            paging = None if json_result is None else json_result['media']['paging']
            url = paging['next']
        except KeyError:
            url = None
        isnext = url is not None
        posts = None if json_result is None else json_result['media']['data']
        yield posts

def ig_media(id, access_token):
    # url = fb_generate_url(
    #     node = id,
    #     fields = 'id,caption,comments_count,like_count,media_type,media_url,owner,permalink,shortcode,timestamp,username,children,comments',
    #     access_token = access_token
    # )

    # json_result = jr.json_request(url)
    response = requests.get('https://graph.instagram.com/'+str(id)+'?fields=id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username,children&access_token='+access_token)
    json_result=json.loads(response.text)
    return json_result

# 전처리
def pre_precess(media):
    # timestamp UTC + 9 > KST
    kst = datetime.strptime(media['timestamp'], '%Y-%m-%dT%H:%M:%S+0000')
    kst = kst + timedelta(hours=+9)
    media['timestamp'] = kst.strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    print("__main__.py is running...")
    until=datetime.now()
    since=until-timedelta(days=30)

    since=since.strftime("%Y-%m-%d")
    until=until.strftime("%Y-%m-%d")

    json_result=code_to_token(Authorization_Code)
    # json_result={'access_token': 'IGQVJYXzVUZAEVfalBDdkxZAYWdxcV9VMjlBVjJBTmx2ZADd1VGFKdEo0TFBqVHdzZAmN3V1JveGs5eXhCb1JEQ2ctck5LRWlQTzhqczQzUEpQXzRtSkxZAYTNNOWlHRThJdS1GNnlSWldRTjYxUzVxcTk1YjRsOEwzRUtGRWhB', 'user_id': 17841441334423750}
    user_id=json_result['user_id']
    access_token=json_result['access_token']
    print('ACCESS_TOKEN : '+access_token+'\n')
    
    # print("ACCESS_TOKEN : "+access_token)
    ig_media_list(user_id, access_token, since, until)

    #file name
    info_filename = '%s/ig_info_%s.json' % (RESULT_DIRECTORY, user_id)
    media_filename = '%s/ig_media_%s.json' % (RESULT_DIRECTORY, user_id)

    #instagram basic info crawling
    print("crawling id "+str(user_id)+" basic information...")
    ig_basic_info=ig_basic_info(user_id, access_token)

    print("writing id "+str(user_id)+" basic information as outfile...")
    with open(info_filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(ig_basic_info, indent=4, sort_keys=True, ensure_ascii=False )
        outfile.write(json_string)
    print("id "+str(user_id)+" basic information was saved as "+info_filename+'\n')

    #instagram media id list crawling
    print("crawling id "+str(user_id)+" media...")
    result = []
    for posts in ig_media_list(user_id, access_token, since, until):
        for post in posts:
            result.append(ig_media(post['id'], access_token))
    
    print("pre-processing... (UTC > KST)")
    for media in result:
        pre_precess(media)
    
    print("writing id "+str(user_id)+" media as outfile...")
    with open(media_filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False )
        outfile.write(json_string)
    print("id "+str(user_id)+" media was saved as "+media_filename)

