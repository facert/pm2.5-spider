# -*- coding: utf-8 -*- 
import re
import urllib
import os 
def download_music(name):
    domain = 'http://www.rui123.com/audio/'
    source_path = './source1/' +name+'.mp3'
    url = domain + name + '.mp3'
    urllib.urlretrieve(url,source_path,Schedule)    

def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per

if __name__ == '__main__':
	for mon in xrange(1,13):
		print '%02d'%mon
		# name = '2013' +'%02d'%mon
		for day in xrange(1,31):
			print '%02d'%day
			# name=name+'%02d'%day
			for list1 in xrange(1,11):
				# name = name+'-'+str(list1)
				# name = ''
				download_music('2013'+'%02d'%mon+'%02d'%day+'-'+str(list1))
	# download_music