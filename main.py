import subprocess
import webbrowser
import datetime

today = datetime.datetime.now().strftime('%Y%m%d')

def run_shell(cmd):
    # execute cmd command. If success，return (0, 'xxx')；if fail，return (1, 'xxx')
    result = subprocess.getstatusoutput(cmd)
    return result

# fetch webpage from '北京本地宝': 'http://bj.bendibao.com/news/20211022/301984.shtm'
print("fetch webpage from '北京本地宝': 'http://bj.bendibao.com/news/20211022/301984.shtm'")
cmd1 = 'python fetch_webpage.py'
st,res = run_shell(cmd1)
print(st,res)

# extract text from the fetched webpage, and save it to BJFK_{today}_addr.xlsx
print(f"extract text from the fetched webpage, and save it to BJFK_{today}_addr.xlsx")
cmd2 = 'python extractLocs.py'
st,res = run_shell(cmd2)
print(st,res)

# query the langtitude and latitude of the address in BJFK_{today}_locs.xlsx
print(f"query the langtitude and latitude of the address in BJFK_{today}_locs.xlsx")
cmd3 = 'python poi2loc.py'
st,res = run_shell(cmd3)
if st==1:
    print(f"query failed, please open this webpage to manually get the location of address, using BJFK_{today}_addr.xlsx")
    webbrowser.open('https://maplocation.sjfkai.com/')

# open Gaode map to upload the BJFK_{today}_locs.xlsx, and update the scatter map for Beijing Pandemic
print(f"open Gaode map to upload the BJFK_{today}_locs.xlsx, and update the scatter map for Beijing Pandemic")
webbrowser.open('https://maplab.amap.com/dev/mapdata')

print(f'The share link for the generated map is: maplab.amap.com/share/mapv/272589e85e2eb5c8861ad9a4f7e08075')
webbrowser.open('https://maplab.amap.com/share/mapv/272589e85e2eb5c8861ad9a4f7e08075')