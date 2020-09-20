import numpy as np
from eemotion import emotionR

def emotion_30(text_list):
    emotion_list1 = []
    emotion_list2 = []
    emotion_list3 = []
    emotion_list4 = []
    emotion_list5 = []
    
    for idx in range(0, len(text_list)):
        if idx>=0 and idx<6:
            emotion_list1.append(emotionR(text_list[idx]))
        if idx>=6 and idx<12:
            emotion_list2.append(emotionR(text_list[idx]))
        if idx>=12 and idx<18:
            emotion_list3.append(emotionR(text_list[idx]))
        if idx>=18 and idx<24:
            emotion_list4.append(emotionR(text_list[idx]))
        if idx>=24 and idx<30:
            emotion_list5.append(emotionR(text_list[idx]))

    emotion_list=[emotion_list1, emotion_list2, emotion_list3, emotion_list4, emotion_list5]
    return emotion_list

def Max_Emotion(emotion_list):
    newlist = sum(emotion_list, [])
    # print("newlist:", newlist)
    em1 = newlist.count(1)
    em2 = newlist.count(2)
    em3 = newlist.count(3)
    em4 = newlist.count(4)
    em5 = newlist.count(5)
    em6 = newlist.count(6)
    # anger fear joy love sadness surprise
    a = [em1, em2, em3, em4, em5, em6]
    b = sorted(a) # [1, 2, 3, 4, 5, 6] 개수대로 정렬
    emotion3 = []
    percent3 = []
    for idx in range(1, 4):
        value = a.index(b[-idx])
        emotion3.append(value + 1)
        percent3.append(round(b[-idx]/30*100, 2))
        a[value] = 0

    # print("emotion3 " , emotion3)
    # print("percen3: ", percent3)
    return emotion3, percent3