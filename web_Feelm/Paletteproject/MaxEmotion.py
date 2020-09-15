import numpy as np

def Max_Emotion(emotion_list):
    newlist = np.array(emotion_list).flatten().tolist()
    em1 = newlist.count(1)
    em2 = newlist.count(2)
    em3 = newlist.count(3)
    em4 = newlist.count(4)
    em5 = newlist.count(5)
    em6 = newlist.count(6)
    em7 = newlist.count(7)

    a = [em1, em2, em3, em4, em5, em6, em7]
    maxemotion = a.index(max(a)) + 1

    percent = round(max(a) / 30 * 100, 2)

    return maxemotion, percent