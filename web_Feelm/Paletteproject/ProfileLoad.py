import json

def InstaProfile(user_id):
    #파일이름 ig_info_id
    file_dir=f"./resultes/ig_info_"+str(user_id)+".json"
    with open(file_dir) as json_file:
        json_data = json.load(json_file)

    # follow = json_data["follows_count"]
    # follower = json_data["followers_count"]
    # introduce = json_data["biography"]
    # img_url = json_data["profile_picture_url"]
    # profile_name = json_data["name"]
    # return follow, follower, img_url, profile_name, introduce
    
    media_count = json_data['media_count']
    username = json_data['username']
    # "media_count": 15,
    # "username": "aloha_ai_2020"
    return media_count, username

def InstaText():
    #json 파일 읽어오는 걸로 바꿔주기
    Dummy_text = [
    '열심히 일하고 만족을 미루는 것이 내가 할 수 있는 전부다!',
    '시작은 미약해도 그 끝은 창대할 수 있다.',
    '난 당신하구 결혼하면서 내 인생을 송두리째 포기한거야! 거기다 대고 뭘 양보했냐고?',
    '아버지가가방에들어가신다',
    '하기야, 육지에서는 나를 몰라보는 이가 없소이다마는, 용궁에까지 소문이 났다 하니 조금은 놀랍소.',
    '오예 오늘 휴강이다!!!',
    '감기에 걸려서 너무 아프다... 감기 조심!',
    '어젯밤에 누가 계속 따라오는 것 같았다. 너무 무서웠다.. 그래서 빨리 뛰었는데 그 사람도 따라 뛰었다.',
    '엥? 이거 과제라고? 진짜? 나 몰랐어!!',
    '헐 세훈이 재채기 소리 처음 들어봐 ㅠ',
    '오. 어어 신카이. 갑자기 말을 걸지 말라고. 깜짝 놀랐네… 너는 기척이 없군, 이렇게 간단히 주변에 남을 들인 건 오랜만이야.',
    '제발 제발 제발 이제 하고싶어도 200표 밖에 못해요 진짜 제발 우리 조금만 더 힘내요 #BTSBBMAs',
    '기득권은 착하든 나쁘든 그대로 기득권인데 소수자는 박탈당한 권리를 주장하려면 왜 착한 행동으로 "좋은 이미지"를 보여줘야 하나? 시혜적으로 베풀어 주는 거 주워 먹으라고?',
    '헉ㄱ 네넴~!!! 갈래요ㅠㅠㅜㅠㅠㅠ흑흑ㄱ 제가ㅏ 팅김왕이라서 자주자주 팅기기는하지만 애교로 바주시기,...',
    '이렇게나 멋진 은발에 간지 터지는 패션감각의 어른이 신임 외교부장관 내정자라는 게 실화냐 진짜. 외모패권주의라는 이번 정부의 정점 아니냐 정말.',
    '역시느 오늘도 살기 싫군',
    '오 클템도 같은말하네',
    '내가 이 때부터 이를 악물었지...',
    '종나 나랑 짱친할새럼이 없나',
    '헐리웃 리포터의 칸 영화제 portfolio 크리스틴 스튜어트 짱짱 #KristenStewart #Cannes2017',
    'Q. 프러포즈는? "친구들과 있는데 정변호사님이 와서 "택이 너 나랑 결혼할 거야, 말 거야? 빨리 말해!"라고 해서 깜짝 놀라 "알았어"라고 했다."',
    '현식 : 헐.. 실망이야...',
    '밸런타인데이처럼 크리스마스도 사람들에게 각양각색의 감정을 불러일으키는 날이 틀림없었다.사랑,증오,외로움,우울 같은...',
    '성운아 많이 많이 웃어 웃을 때 제일 멋져',
    '헐...이건또무슨....ㅜㅜ',
    '스치면 인연 스며들면 사랑',
    '오늘도 슬쩍슬쩍 바라만 보고 있네 벌써 몇번째인지 몰라 사랑에 빠진것 같아(사랑에빠져버렸어) #이찬',
    '그대 내게 행복을 주는 사람',
    '(거미한테 죽고싶다고했지 죽기싫단 얘기는 안했는데)',
    '"햄스터러러러러러러"는 더 싫어. 아니. 싫대.',
    ]
    return Dummy_text