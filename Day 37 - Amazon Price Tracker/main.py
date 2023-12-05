import requests
from bs4 import BeautifulSoup
from lxml import etree

response=requests.get(url='https://www.amazon.com/Instant-Pot-Duo-Mini-Programmable/dp/B06Y1YD5W7/ref=psdc_3117954011_t1_B075CYMYK6')



soup=BeautifulSoup(response.text,'lxml')
whole_price=soup.find_all('span' ,class_="a-price-whole")[1].get_text()
fraction_price=soup.find_all('span',class_='a-price-fraction')[1].get_text()
whole_price=whole_price.replace('.','')
amazon_price=float(whole_price)+float(fraction_price)/100

if(amazon_price<100.00):
    print("Product is on a sale!!")
    print('The product price is: '+str(amazon_price))
else:
    print("The product price is: "+str(amazon_price))
