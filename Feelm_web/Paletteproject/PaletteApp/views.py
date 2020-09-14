from django.shortcuts import render
from .models import Report
from MaxEmotion import Max_Emotion
# Create your views here.

def home(request):
    return render(request, 'home.html')

def test(request):
    palette1 = [1, 2, 3, 4, 5, 1]
    palette2 = [2, 2, 2, 5, 4, 2]
    palette3 = [1, 1, 5, 3, 2, 3]
    palette4 = [5, 4, 2, 1, 3, 4]
    palette5 = [1, 2, 3, 5, 4, 5]
    palette = [palette1, palette2, palette3, palette4, palette5]
    context={'palette' : palette}
    return render(request,'test.html', context)

def result(request):
    account = request.POST['account']
    if account :
        is_exist = True
    else:
        is_exist = False
    
    palette1 = [7, 2, 3, 6, 5, 1]
    palette2 = [2, 2, 2, 5, 4, 2]
    palette3 = [1, 1, 5, 3, 2, 3]
    palette4 = [5, 6, 2, 1, 3, 4]
    palette5 = [1, 2, 3, 7, 4, 5]
    palette = [palette1, palette2, palette3, palette4, palette5]

    #1:anger 2:fear 3:joy 4:love 5:neutral 6:sadness 7:surprise
    # 제일많은 감정 번호 > 리포트아이디찾기
    maxemotion, percent = Max_Emotion(palette)
    # 리포트 아이디의 내용 가져와서 출력해주기
    emotion = Report.objects.get(pk = maxemotion)

    context = {
        'account' : account,
        'is_exist':is_exist,
        'palette' : palette,
        'emotion' : emotion,
        'percent' : percent,
        }
    return render(request, 'result.html', context)

