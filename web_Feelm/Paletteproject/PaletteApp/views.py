from django.shortcuts import render
from .models import Report
from MaxEmotion import Max_Emotion, emotion_30
from ProfileLoad import InstaProfile, InstaText
# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    context={}
    ### 프로필 가져오기
    account = request.POST['account']
    if account :
        is_exist = True
    else:
        is_exist = False

    follow, follower, img_url, profile_name ,introduce= InstaProfile()
    
    context['info']={
        'account':account,
        'is_exist':is_exist,
        'follow': follow,
        'follower' : follower,
        'introduce':introduce,
        'img_url':img_url,
        'profile_name':profile_name,
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

    # context = {
    #     'account' : account,
    #     'is_exist':is_exist,
    #     'palette' : palette,
    #     'emotion' : {
    #         'first':emotion[0],
    #         'second':emotion[1],
    #         'third':emotion[2],
    #         },
    #     'percent' : {
    #         'first' : percent[0],
    #         'second' : percent[1],
    #         'third' : percent[2]
    #         },
    #     }
    return render(request, 'result.html', context)

