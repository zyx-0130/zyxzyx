import requests
from bs4 import BeautifulSoup
import multiprocessing as mp
import time

t1=time.time()
re=requests.get('https://m.ctrip.com/webapp/hotel/shanghai2/?ulat=0&ulon=0')

s=re.text

soup=BeautifulSoup(s,'html.parser')
page_div=soup.find('div',{'class':'page'})
cars=[]

def crawl_page(url):
    p_re=requests.get(url)
    p_s=p_r.text
    p_soup=BeautifulSoup(p_c,'html.parser')
    p_content=p_soup.find('div',{'class':'item js_single_hotel browse'})
    pageCar=[]

    for car in p_content:
        carDic={}
        carDic['picUrl']=car.find('div',{'class':'i-mod-img js_lazy_style'}).find('img')['src']
        carDic['name']=car.find('div',{'class':'c-mod-top'}).find('a').text
        try:
            carDic['score']=car.find('span',{'class':'c-fn'}).text
        except Exception as e:
            carDic['score']=''

            pageCar.append(carDic)
        return pageCar

pool=mp.Pool()
print(len(cars))        
t2=time.time()
print(t2-t1)
