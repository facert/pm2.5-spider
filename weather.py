# coding=utf-8
import os
import types
import urllib2
import json
import csv
import time
LOCAL_DATA_PATH = "/home/yuki/weather/json_data/"
LOCAL_HTML_ALL_PATH = '/home/yuki/weather/html/all/'
LOCAL_HTML_RANK_PATH = '/home/yuki/weather/html/rank/'
#利用urllib2获取网络数据
def registerUrl():
    try:
        url_all ="http://www.pm25.in/api/querys/all_cities.json?token=**********"
        url_rank = "http://www.pm25.in/api/querys/aqi_ranking.json?token=************"
        url = "file:///home/zcr/weather/aqi_ranking.json"
        data_all = urllib2.urlopen(url_all).read()
        data_rank = urllib2.urlopen(url_rank).read()
        localtime   = time.localtime()
        timestring = time.strftime("%Y-%m-%d-%H", localtime)
        html_all = open((LOCAL_HTML_ALL_PATH+timestring), 'w')
        html_rank = open((LOCAL_HTML_RANK_PATH+timestring), 'w')
        html_all.write(data_all)
        html_rank.write(data_rank)
        #print data_rank
        return data_rank
    except Exception,e:
        print e

def write_csv_file(data, area):
	writer=csv.writer(open((LOCAL_DATA_PATH+area)+'.csv', 'ab'))
	writer.writerow(data)
   # writer.writerow(['time_point', 'aqi','co', 'co_24h', 'no2', 'no2_24h',\
  #                    'o3', 'o3_24h', 'o3_8h', 'o3_8h_24h', 'pm10', 'pm10_24h',\
 #                     'pm2_5', 'pm2_5_24h', 'so2', 'so2_24h'])

#解析从网络上获取的JSON数据
def praserJsonFile(jsonData):
    value = json.loads(jsonData)
    for detail in value:
        # print detail
        data = [detail['time_point'], detail['aqi'], detail['co'], detail['co_24h'], \
                detail['no2'], detail['no2_24h'], detail['o3'], detail['o3_24h'], detail['o3_8h'], \
                detail['o3_8h_24h'], detail['pm10'], detail['pm10_24h'], detail['pm2_5'], detail['pm2_5_24h'], \
                detail['so2'], detail['so2_24h']]
        #print data
        write_csv_file(data, detail['area'])

def convert_to_windows():
	import shutil
	from city_json import *
	OLD_PATH = '/home/yuki/weather/json_data/'
	NEW_PATH = '/home/yuki/weather/windows_data/'
#	os.mkdir('/home/python/weather/oo')

	for file in os.listdir(OLD_PATH):
		#print file
		#print file.split('.')[0].decode('utf-8').decode('gb2312')
		#print file.split('.')[0]
		new_file = "%s%s" %(city[file.split('.')[0]],'.csv')
		#print new_file
		shutil.copy2(OLD_PATH+file, NEW_PATH+new_file)

if __name__ == "__main__":  
    data = registerUrl()  
    # jsonFile(data)  
    praserJsonFile(data)
    convert_to_windows()
