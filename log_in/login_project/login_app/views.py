from django.shortcuts import render

# Create your views here.
def home(request):
    instagram_app_id='783139315754863'
    redirect_uri='https://127.0.0.1:8000/result/'
    scope='user_profile,user_media'
    url=f'https://api.instagram.com/oauth/authorize?client_id={instagram_app_id}&redirect_uri={redirect_uri}&scope={scope}&response_type=code'
    content={
        'IG_URL':url
    }
    print(url)
    return render(request, 'home.html', content)

def result(request, code):
    content={
        'code':code
    }
    return render(request, 'result.html', content)