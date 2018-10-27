import requests
import json
import operator
import time
from bs4 import BeautifulSoup as BS
urls=open('URLs.txt','r').read().split('\n')
File=open('Stats.txt','w', encoding="utf-8")
for l in urls:
    r=requests.get(l)
    page=r.content
    soup = BS(page, 'html.parser')
    Views=soup.find('div',class_='watch-view-count').text
    likebutton = soup.find('button', class_="like-button-renderer-like-button")
    Like=likebutton.find('span',class_ = 'yt-uix-button-content').text
    disbutton = soup.find('button',class_='like-button-renderer-dislike-button')
    Dis=disbutton.find('span',class_ = 'yt-uix-button-content').text
    Published=soup.find('strong',class_="watch-time-text").text[len('Published on ')-1:]
    
    Title=str(soup.find_all('h1')[1].text.strip('\n').strip('\t').strip(' ').strip('\n').encode("utf-8")).strip("'b").strip("'")
    
    File.write(Title+'\t'+Published+'\t'+Dis+'\t'+Like+'\t'+Views+'\t'+l+'\n')
    print(Title,Published,Dis,Like,Views,l)