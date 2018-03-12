import requests
from bs4 import BeautifulSoup

headers = {
    'Referer' : 'http://music.163.com/',
    'Host' : 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

list_url = 'http://music.163.com/playlist?id=777580435'

r = requests.session()
s = BeautifulSoup(r.get(list_url,headers = headers).content,"html.parser")
main = s.find('ul',{'class' :'f-hide'})

for i in main.find_all('a'):
    print('{} : {}'.format(i.text,i['href']))
