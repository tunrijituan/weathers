from bs4 import BeautifulSoup
import requests,json
headers={
       "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36" 
        }
urls={
      "http://www.weather.com.cn/textFC/hb.shtml",
      "http://www.weather.com.cn/textFC/gat.shtml"
      }
weathers=[]
provice=''
for url in urls:  
    response=requests.get(url,headers=headers)
    text=response.content.decode('utf-8')
    soup=BeautifulSoup(text,'html5lib')
    conMintab=soup.find('div',class_='conMidtab')
    tables=conMintab.find_all('table')
    for table in tables:
        trs=table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds=tr.find_all('td')
            if index==0:
                city_td=tds[1]
                provice_td=tds[0]
                provice=list(provice_td.stripped_strings)[0]
            else:
                city_td=tds[0]
            city=list(city_td.stripped_strings)[0]
            temp_td=tds[-2]
            min_temp=list(temp_td.stripped_strings)[0]   
            weather={
                    "city":city,
                    "min_temp":min_temp
                    }
            weathers.append(weather)
        print json.dumps({provice:weathers},encoding='utf-8',ensure_ascii=False)
        weathers=[]
        provice=''