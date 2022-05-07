import re
import pandas as pd 
import datetime

today = datetime.datetime.now().strftime('%Y%m%d')
#today = '20220506'

raw_dir = './data/raw/'
proceed_dir = './data/proceed/'

with open(raw_dir+f'BJFK_{today}.md','r',encoding='utf-8') as rfp:
    recs = []
    area = None
    dist = None
    lines = [line.strip('\n') for line in rfp.readlines()]
    for line in lines:
        if re.sub(r'[ \n]',r'',line) == '':
            continue
        if re.search(r'【',line):
            area = re.search(r'【(.*?)】',line).group(1)
        elif re.search(r'➤',line):
            dist = re.sub(r'➤',r'',re.search(r'(.*?)：',line).group(1)).strip()
            dist = re.sub(r'\(.*?\)',r'',dist)
        else:
            line = re.sub(r'•',r'',line).strip()
            clline = re.sub(r'[ \t]+',r' ',re.sub(r'（.*?）',r'',re.sub(r'\(.*?\)',r'',line)))
            if '、' in clline:
                try:
                    prefix = re.search(r'(.*?)\d+号楼?、',clline).group(1)
                    recs.append({'状态':area,'区县':dist,'小区':line,'地名':dist+clline.split('、')[0]})
                    for i in range(1,len(clline.split('、'))):
                        recs.append({'状态':area,'区县':dist,'小区':line,'地名':dist+prefix+clline.split('、')[i]})
                except:
                    recs.append({'状态':area,'区县':dist,'小区':line,'地名':dist+clline})
            else:
                recs.append({'状态':area,'区县':dist,'小区':line,'地名':dist+clline})
    df = pd.DataFrame(recs)
    df[df['状态']=='封控区'].to_excel(proceed_dir+f'BJFK_{today}_addr.xlsx',index=False)
