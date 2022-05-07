import requests
import json
import pandas as pd
import datetime
from chinacoordtran import bd09togcj02

APIKEY = open('APIKEY.txt').read().strip()
today = datetime.datetime.now().strftime('%Y%m%d')

raw_dir = './data/raw/'
proceed_dir = './data/proceed/'

def query_addr(addr='',city='北京',key=APIKEY):
    query = f'https://api.map.baidu.com/geocoder?address={addr}&output=json&key={key}&city={city}'
    resp = requests.get(query)
    # output: {'status': 'OK', 'result': {'location': {'lng': 116.360362, 'lat': 40.007486}, 'precise': 1, 'confidence': 75, 'level': '商务大厦'}}
    try:
        jobj = json.loads(resp.text)
    except:
        exit(1)
    return jobj

addr_df = pd.read_excel(proceed_dir+f'BJFK_{today}_addr.xlsx',sheet_name='Sheet1')
addr_lst = addr_df[['状态','区县','地名']].values.tolist()

recs = []

coordTrobj = bd09togcj02()
for status,dist,addr in addr_lst:
    resp = query_addr(addr)
    print('resp: ',resp)
    if resp['status'] == 'OK':
        res = resp['result']
        if len(res)==0:
            continue
        loc = res['location']
        bdlng, bdlat = loc['lng'], loc['lat']
        gcj_coord = coordTrobj.CoordTran(bdlng, bdlat)
        gclng,gclat = gcj_coord.X,gcj_coord.Y
        rec = {'经纬度':str(gclng)+','+str(gclat),'地名':addr,'可信度':res['confidence'],'是否精确':res['precise'],'地址类型':res['level']}
    else:
        rec = {'地名':addr,'可信度':0,'是否精确':0,'地址类型':'未知','经纬度':None}
    rec['状态'] = status
    rec['区县'] = dist
    recs.append(rec)
    print(rec)


df = pd.DataFrame(recs)
df.to_excel(proceed_dir+f'BJFK_{today}_locs.xlsx',index=False)
#df.to_csv(proceed_dir+'BJFK_today_bdloc.csv',index=None,encoding='utf-8')
