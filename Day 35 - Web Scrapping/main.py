from bs4 import BeautifulSoup
import requests

response=requests.get(url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')

file=open(file='Best Movies.txt',mode='w')

soup=BeautifulSoup(response.text,'html.parser')

film_tags=soup.find_all(name='h3',class_='title')
for tag in film_tags:
    print(tag.getText())
    try:
        file.write(tag.getText() + '\n')
    except:
        file.write("Something went wrong with the characters here\n")





