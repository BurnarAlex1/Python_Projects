import requests
from requests import *
from bs4 import BeautifulSoup


user_date=input('Give me a time in the past(format YYYY-MM-DD):')

my_url='https://www.billboard.com/charts/hot-100/'+user_date+'/'

response=requests.get(url=my_url)
soup=BeautifulSoup(response.text,"html.parser")
song_tags=soup.find_all(name='h3',id='title-of-a-story')



file=open(file='MovieFile.txt',mode='w')

for tag in song_tags:
    print(tag.getText())
    file.write(tag.getText())

