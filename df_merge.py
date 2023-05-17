#!/usr/bin/env python
# coding: utf-8

# # 데이터 다루기 _ 총정리 ##
# - 데이터 수집
# - 데이터 읽어들이기
# - 기준년도 컬럼추가 (2019년 1월 ~ 2022년 1월)
# - 국적명 추가
# - 행단위 추가

# In[ ]:

#기준년도 리스트 만들기
date_temp = []
for y in ['2019', '2020', '2021']:
    for m in range(1,13):
        date_temp.append(y+'-'+str(m).zfill(2))
date_temp = date_temp + ['2022-01']

#데이터 읽어들이고 합치기
path = 'C:/edu_busan_202305/02_데이터처리/08_day/files2/'
df_all2 = pd.DataFrame()
df_code = pd.read_excel('sample_codemaster.xlsx')

for i, date in zip(range(0,37), date_temp):
    df = pd.read_excel(path+'sample_1('+str(i)+').xlsx',
                       header=1, skipfooter=2, usecols="A:C")
    df['기준년도']= date
    df = df.merge(df_code, how='left', on='국적코드')
    df_all2 = pd.concat([df_all2, df])
    df = []
    
df_all2 = df_all2.reset_index(drop=True)
df_all2

