#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus

print('다운로드 시작')

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

# 식물 이름에 해당하는 폴더가 경로내에 있어야 한다.
plusUrl = input('검색어 : ')
tag = input('식물 이름 : ')
# 한글 검색 자동 변환

url = baseUrl + quote_plus(plusUrl)
html = urlopen(url)
soup = bs(html, "html.parser")
img = soup.find_all(class_= '_img', limit=50)

save_path = './flower/' + tag + "/"
n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open(save_path + plusUrl + str(n)+'.jpg','wb') as h:
            img = f.read()
            h.write(img)
    n+=1
    
print('다운로드 완료')
