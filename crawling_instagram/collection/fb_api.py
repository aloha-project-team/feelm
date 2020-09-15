from urllib.parse import urlencode
from collection import json_request as jr

BASE_URL_FB_API = 'https://graph.facebook.com/v8.0'
ACCESS_TOKEN = 'access token'

# 여러 파라미터에 대하여, url을 생성
def fb_generate_url(base = BASE_URL_FB_API, node = '', **param):
    return '%s/%s/?%s' % (base, node, urlencode(param))

# API me > instagram id
def fb_name_to_ig_id(pagename):
    url = fb_generate_url(node = pagename, fields='id, name, accounts', access_token = ACCESS_TOKEN)
    json_result = jr.json_request(url)
    page_id=json_result['accounts']['data'][0]['id'] #페이스북 페이지 아이디

    url=fb_generate_url(node=page_id, fields='instagram_business_account', access_token = ACCESS_TOKEN)
    json_result = jr.json_request(url)
    return json_result['instagram_business_account']['id'] #인스타그램 아이디 리턴

# API instagram id > instagram url
def ig_basic_info(pagename, since, until):
    url = fb_generate_url(
        node = pagename,
        fields = 'biography,followers_count,follows_count,ig_id,id,media_count,name,profile_picture_url,username,recently_searched_hashtags,stories,tags',
        since = since,  # 시작 날짜
        until = until,  # 끝 날짜
        limit = 30,     # 개수
        access_token = ACCESS_TOKEN
    )

    json_result = jr.json_request(url)
    return json_result
    

# instagram url > media id
def ig_media_list(pagename, since, until):
    url = fb_generate_url(
        node = pagename,
        fields = 'media',
        since = since,  # 시작 날짜
        until = until,  # 끝 날짜
        limit = 30,     # 개수
        access_token = ACCESS_TOKEN
    )

    isnext = True
    while isnext is True:
        json_result = jr.json_request(url)
        try:
            paging = None if json_result is None else json_result['media']['paging']
            url = paging['next']
        except KeyError:
            url = None
        isnext = url is not None
        posts = None if json_result is None else json_result['media']['data']
        # generator를 사용해서 fb_fetch_post(...) 함수를 for 푸르안에서 사용 가능하도록 수정한다.
        yield posts

def ig_media(id):
    url = fb_generate_url(
        node = id,
        fields = 'id,caption,comments_count,like_count,media_type,media_url,owner,permalink,shortcode,timestamp,username,children,comments',
        access_token = ACCESS_TOKEN
    )

    json_result = jr.json_request(url)
    return json_result