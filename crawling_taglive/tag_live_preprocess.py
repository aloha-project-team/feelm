import re

def preprocess(text):
    print('load text...')
    origin=str(text)
    # print('-------- original text --------')
    # print(text)
    cleanr =re.compile('<.*?>')
    cleantext=re.sub(cleanr, '\n', origin)
    cleantext=cleantext.replace('\n', '')
    return cleantext

