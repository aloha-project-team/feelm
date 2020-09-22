from django.shortcuts import render
from .models import Report
from MaxEmotion import Max_Emotion, emotion_30
from ProfileLoad import InstaProfile, InstaText
from crawling_instagram import crawling_insta

# Create your views here.

def home(request):
    instagram_app_id='783139315754863'
    redirect_uri='https://127.0.0.1:8000/result/'
    scope='user_profile,user_media'
    url=f'https://api.instagram.com/oauth/authorize?client_id={instagram_app_id}&redirect_uri={redirect_uri}&scope={scope}&response_type=code'
    context={
        'IG_URL':url
    }
    return render(request, 'home.html', context)

def result(request):
    context={}
    #로그인된 사용자의 code를 가져온다.
    code = request.GET.get('code')
    if code :
        is_exist = True
    else:
        is_exist = False
    #사용자의 인스타그램 정보들을 크롤링한뒤 저장된 파일을 찾기위한 user_id값을 반환한다.
    user_id = crawling_insta(code)
    # user_id값을 통해 사용자의 basic_info중 게시물 수 와 이름을 가져온다.
    media_count, username= InstaProfile(user_id)
    
    context['info']={
        'is_exist':is_exist,
        'media_count': media_count,
        'username':username,
    }
    # instaText(user_id)를 통해 저장된 게시물텍스트를 불러오고
    # emotion_30을 통해 bert모델을 통과시킨 감정리스트 값을 가져온다. 
    # [게시물1, 게시물2, ..., 게시물30] > [1, 3, 4, 5, ..., 2]
    # 1:anger 2:fear 3:joy 4:love 5:sadness 6:surprise
    palette = emotion_30( InstaText(user_id) ) 
    context['palette'] = palette

    # Max_emotion함수를 통해 가장많이 나온 상위 3개 감정과 비율을 받아온다
    # [1(anger), 3(joy), 5(sadness)], [23.33, 23.33, 3.33]
    maxemotion, percent = Max_Emotion(palette)

    # 해당 감정에 해당하는 report객체를 가져온다.
    emotion=[]
    for p in maxemotion:
            emotion.append(Report.objects.get(pk=p))

    context['emotion'] = {
            'first':emotion[0],
            'second':emotion[1],
            'third':emotion[2],
            }

    context['percent'] =  {
            'first' : percent[0],
            'second' : percent[1],
            'third' : percent[2]
            }

    return render(request, 'result.html', context)
