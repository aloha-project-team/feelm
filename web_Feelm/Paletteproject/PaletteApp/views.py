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
    code=request.GET.get('code')
    if code :
        is_exist = True
    else:
        is_exist = False

    user_id = crawling_insta(code)
    context={}
    ### 프로필 가져오기
    # follow, follower, img_url, profile_name ,introduce= InstaProfile(user_id)
    media_count, username= InstaProfile(user_id)
    
    context['info']={
        'is_exist':is_exist,
        # 'follow': follow,
        # 'follower' : follower,
        # 'introduce':introduce,
        # 'img_url':img_url,
        # 'profile_name':profile_name,
        'media_count': media_count,
        'username':username,
    }
    ### 감정팔레트 표시하기

    palette1 = [4, 2, 3, 6, 5, 1]
    palette2 = [2, 2, 2, 5, 4, 2]
    palette3 = [1, 1, 5, 5, 2, 3]
    palette4 = [5, 6, 2, 1, 3, 4]
    palette5 = [1, 2, 3, 2, 4, 5]
    palette = [palette1, palette2, palette3, palette4, palette5]
    # palette = emotion_30( InstaText() )
    context['palette'] = palette
    # 1:anger 2:fear 3:joy 4:love 5:neutral 6:sadness 7:surprise
    maxemotion, percent = Max_Emotion(palette)
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
