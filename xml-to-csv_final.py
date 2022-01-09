# xml file to csv

# xml을 바로 csv로 바꿀때 tree를 이용한 etree.element가 많이쓰이지만,
# 이는 무겁고 쓰기도 어렵다. 간단하게 dict,json,dataframe등으로 변환하는 방식은 가볍고 편하다.

# xmltodict를 import해 xml파일을 dict로 변환해주었다.
# doc의 자료형을 찍어보니 ordered된 dict데이터였다.
# 구글에 OrderedDict to csv를 찍어서
# https://pretagteam.com/question/write-python-ordereddict-to-csv # 이 답변을 참고했다.
# https://stackoverflow.com/questions/40902200/write-python-ordereddict-to-csv

# 이를 데이터프레임화 한 후 to_csv로 했는데 파일 끝에 complete란 프린트문을 쳐놨는데
# 파일이 0kb로 생성 된 후 프로그램 실행이 다 끝나지 않고 멈춰버리고 끝났다.
# 이에 # soda = {'상품명': ['콜라', '사이다'], '가격': [2700, 2000]} 로 쳐보니 들어가더라.
# 원인은 대용량 파일의 메모리 터짐이 원인이였다.
# 결국 새로 작은 파일로 쪼개진 파일을 찾아서 돌리니까 되었다. 끝.

# 위키 데이터 구성
# wiki_rows = ['page_id', 'title', 'timestamp', 'text']


import xmltodict
import os
import time
import csv
import pandas as pd

# 내 경로 확인
# Get the current working directory (cwd)
currentPath = os.getcwd()
# print path
print(currentPath)

# 한글위키_1 read
read_file ='./_data/simple-wikipedia-xml-to-csv-master/kowiki-latest-pages-articles1.xml'

startTime1 = time.time()

# read file을 dict로.
with open(read_file, 'rt', encoding="utf8") as f:
	# dict 모양으로 변환
    doc = xmltodict.parse(f.read())


# 시간체크
startTime2 = time.time()

df = pd.DataFrame.from_dict(doc)

# 한글위키_1 write
out_file1 ='./_data/simple-wikipedia-xml-to-csv-master/kowiki111.csv'

# 없으면 만들어서 입력 있으면 있는것에 덧붙여서 입력
if not os.path.exists(out_file1):
    df.to_csv(out_file1, index = False, mode='w',encoding="utf-8-sig")
else:
    df.to_csv(out_file1, index = False, mode='a',encoding="utf-8-sig",header=False)
print("write complete")

   
endTime2 = time.time() - startTime2
print(endTime2)
print(" all complete ")













# 참고
# pandas 결과값을 csv 파일 형식으로 누적해서 저장하기: to_csv
# https://hogni.tistory.com/10

# When saving large dataframe
# https://stackoverflow.com/questions/40660331/pandas-to-csv-slow-saving-large-dataframe

# 파이썬에서 CSV(Comma Separated Values) 파일 읽기/쓰기
# https://psychoria.tistory.com/746

# python dictionary 를 json 으로 변환
# https://bluese05.tistory.com/37

# ★★★★Python에서 XML을 dict 형식으로 초간단 변환하기
# https://pparkst.tistory.com/33
# https://www.jungyin.com/123

# [Python] xml 다루기 via ElementTree #1
# http://egloos.zum.com/sweeper/v/3045370
