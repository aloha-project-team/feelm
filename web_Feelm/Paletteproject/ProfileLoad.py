import json

def InstaProfile(user_id):
    #파일이름 ig_info_user-id
    file_dir=f"./resultes/ig_info_"+str(user_id)+".json"
    with open(file_dir) as json_file:
        json_data = json.load(json_file)
    
    media_count = json_data['media_count']
    username = json_data['username']

    return media_count, username

def InstaText(user_id):
    file_dir=f"./resultes/ig_media_"+str(user_id)+".json"
    with open(file_dir, encoding='UTF8') as json_file:
        json_data = json.load(json_file)

    text_list =[]
    for day in json_data:
        text_list.append(day['caption'])

    #가장 최근 게시물이 첫번째에 위치하기 때문에 순서 반대로 바꿔주기
    text_list= text_list[::-1]
    return text_list
