#-*-coding:utf-8-*-
import requests
import re
import datetime
from bs4 import BeautifulSoup

raw_dir = './data/raw/'
today = datetime.datetime.now().strftime('%Y%m%d')

url = 'http://bj.bendibao.com/news/20211022/301984.shtm'

# fetch html from the given url
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
resp = requests.get(url,headers=header)
resp.encoding = 'utf-8'
#print(resp.text)
# parse html, and get the text content of a div element whose class='content' in the page
soup = BeautifulSoup(resp.text, 'lxml', from_encoding='utf-8')
content = soup.find('div', class_='content')
#print content.text in right encoding
#print(content.text)

normal_text = re.sub(r'【拓展阅读】.*', '', content.text)
normal_text = re.sub(r'^\s*.*?【', '【', normal_text)
normal_text = re.sub(r'[\u3010\u2022\u27a4]','\n\g<0>', normal_text)

with open(raw_dir+f'BJFK_{today}.md','w',encoding='utf-8') as wfp:
    wfp.write(normal_text)
