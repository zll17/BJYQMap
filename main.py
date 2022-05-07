import webbrowser
import datetime
import os
import time

today = datetime.datetime.now().strftime('%Y%m%d')


# fetch webpage from '北京本地宝': 'http://bj.bendibao.com/news/20211022/301984.shtm'
print("fetch webpage from '北京本地宝': 'http://bj.bendibao.com/news/20211022/301984.shtm'")
cmd1 = 'python fetch_webpage.py'
st = os.system(cmd1)
print(st)

# extract text from the fetched webpage, and save it to BJFK_{today}_addr.xlsx
print(f"extract text from the fetched webpage, and save it to BJFK_{today}_addr.xlsx")
cmd2 = 'python extractLocs.py'
st = os.system(cmd2)
print(st)

# query the langtitude and latitude of the address in BJFK_{today}_locs.xlsx
print(f"query the langtitude and latitude of the address in BJFK_{today}_locs.xlsx")
cmd3 = 'python poi2loc.py'
st = os.system(cmd3)
if st==1:
    print(f"query failed, please open this webpage to manually get the location of address, using BJFK_{today}_addr.xlsx")
    time.sleep(3)
    webbrowser.open('https://maplocation.sjfkai.com/')

# open Gaode map to upload the BJFK_{today}_locs.xlsx, and update the scatter map for Beijing Pandemic
print(f"\n\nopen Gaode map to upload the BJFK_{today}_locs.xlsx, and update the scatter map for Beijing Pandemic\n\n")
time.sleep(2)
print(f'\n\nThe share link for the generated map is: maplab.amap.com/share/mapv/272589e85e2eb5c8861ad9a4f7e08075')
time.sleep(2)

webbrowser.open('https://maplab.amap.com/dev/mapdata')
webbrowser.open('https://maplab.amap.com/share/mapv/272589e85e2eb5c8861ad9a4f7e08075')
