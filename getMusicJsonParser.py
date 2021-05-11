#-*- coding:utf-8 -*-

import json
import requests
import urllib.request
import os
import re

def getData():
	
	type_arr = ['kpop','retro','trot','classic','theme','show']
	s3_url = "https://static.kbs.co.kr/music/"
	
	dup_check = []
	data_arr = []
	item_count = 0
	for music_type in type_arr:
		json_url = s3_url + music_type + '.json'
 
		with urllib.request.urlopen(json_url) as url:
			data = url.read().decode('utf-8')
			# json 데이터로 j 변수에 담기
			json_data = json.loads(data)

		
		
	###
	# 데이터 형식
	# 1 : 키값
	
	###
		# print(json_data.keys())
	
		
		json_key_list = list(json_data.keys())
		print(json_key_list)
		for i, key in enumerate(json_key_list):
		
			# output_item = {}
			print(key)
			item = json_data[key]
			
			items = item['items']
			
			for video_item in items:	
				
				## 중복체크
				if video_item['snippet']['resourceId']['videoId'] in dup_check:
					continue
							
				if 'maxres' in (video_item['snippet']['thumbnails']):
					image_w = video_item['snippet']['thumbnails']['maxres']['url']
				elif 'standard' in (video_item['snippet']['thumbnails']):
					image_w = video_item['snippet']['thumbnails']['standard']['url']
				elif 'high' in (video_item['snippet']['thumbnails']):
					image_w = video_item['snippet']['thumbnails']['high']['url']
				elif 'medium' in (video_item['snippet']['thumbnails']):
					image_w = video_item['snippet']['thumbnails']['medium']['url']
				else:
					image_w = video_item['snippet']['thumbnails']['default']['url']
					
				publishedAt = re.sub('-', '' , video_item['snippet']['publishedAt'])[0:8]
				output_item = { 
					'title' : video_item['snippet']['title'],
					'description' : video_item['snippet']['description'],
					'image_w' : image_w,
					'title' : video_item['snippet']['title'],
					'channelTitle' : video_item['snippet']['channelTitle'],
					'playlistId' : video_item['snippet']['playlistId'],
					'videoId' : video_item['snippet']['resourceId']['videoId'],
					'channelTitle' : video_item['snippet']['videoOwnerChannelTitle'],
					'channelId' : video_item['snippet']['videoOwnerChannelId'],
					'type' : music_type,
					'publishedAt' : publishedAt,
		
				}		
				item_count = item_count + 1
				data_arr.append(output_item)
				dup_check.append(video_item['snippet']['resourceId']['videoId'])
	
	output = dict()
	output['total_count'] = item_count
	output['data'] = data_arr
	filename = './music_items.json'
	# output2=json.dumps(output,ensure_ascii=False,indent=3)
	os.makedirs(os.path.dirname(filename),exist_ok=True)
	with open(filename, 'w', encoding='utf-8') as make_file:
		json.dump(output,make_file, ensure_ascii=False,indent=3)
				# json.dump(j, make_file, ensure_ascii=False,indent="\t")
		# print(output2)
	


if __name__ == "__main__":
	getData()