#-*- coding:utf-8 -*-


import urllib.request
import json
import requests
import schedule
import time
import os
from datetime import datetime
from selenium import webdriver
from Screenshot import Screenshot_Clipping

# 반복될 작업을 함수로 정의
def scd():
    
	channel_code_list = ['21','22','23','24','25','26','I92']
	urls_list = list()
	today_date = datetime.today().strftime("%Y%m%d")
	
	for channel_code in channel_code_list:
		url = "https://static.api.kbs.co.kr/mediafactory/v1/schedule/weekly?rtype=json&channel_code=" + channel_code + "&program_planned_date_from=" + today_date+"&program_planned_date_to="+today_date+"&local_station_code=00"
		urls_list.append(url)	
	# API 링크 가져와서 data 변수에 담기
	
	for i,url_item in enumerate(urls_list):
	
		with urllib.request.urlopen(url_item) as url:
			data = url.read().decode('utf-8')
		# json 데이터로 j 변수에 담기
		j = json.loads(data)
		
		print(j)
		## file YYYY-MM-DD-HH-SS.json
		filename = "./output/" + datetime.today().strftime("%Y%m%d%H%M%S") + "/"+ channel_code_list[i] + ".json"
		
		#json 파일로 저장
		os.makedirs(os.path.dirname(filename),exist_ok=True)
		with open(filename, 'w', encoding='utf-8') as make_file:
			json.dump(j, make_file, ensure_ascii=False,indent="\t")

	
	# teleurl 변수에 텔레그램 botfather 한테 받은 자신의 API 넣기
	# teleurl = "https://api.telegram.org/bot511337000:AAG7gRmT3Ra8FYl22gekgckK_iwVwkJAAAA/sendMessage"
	
	# 로그 찍어보기(지워도 됨)

	# 챗 id 와 symbol : price 값을 텔레그램에 보내기
	# params = {'chat_id': '-1001243756825', 'text': j[0]["symbol"] + " : " + str(j[0]["price"])} 
	
	# 텔레그램으로 메시지 전송
	# res = requests.get(teleurl, params=params)

# 스케쥴 설정 매분마다 실행

def fullpage_screenshot():    
	# chrome_options = Options()
	# chrome_options.add_argument('--headless')
	# chrome_options.add_argument('--start-maximized')
	DRIVER = 'chromedriver'
	driver = webdriver.Chrome(DRIVER)
	driver.get('http://radio.kbs.co.kr')
	
	time.sleep(5)
	# print(str(required_width) + "  " + str(required_height))
	driver.set_window_size(1800,4500)
	ob=Screenshot_Clipping.Screenshot()
 
	filename = datetime.today().strftime("%m%d%H%M%S") + "screenshot.png"
	img_url=ob.full_Screenshot(driver,save_path=r'./output', image_name=filename)

	driver.close()
	driver.quit()

scd()
fullpage_screenshot()
schedule.every().minute.do(scd)
schedule.every().minute.do(fullpage_screenshot)



# while 문을 사용하여 스케쥴러 실행
while 1:
	schedule.run_pending()
	time.sleep(1200)