# -*- coding: utf-8 -*- 
import re
import urllib
import os                                              
def getHtml(url):
    html = urllib.urlopen(url)
    scode = html.read()
    return scode


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


def getMusicHtml(source):
    match = r'onclick=\"location\.href=(.*)\"'
    #match = re.compile(r'\d+')
    music_url = re.compile(match)
    music = re.findall(music_url,source)
    return music

def get_download_url(source):
    # import pdb;pdb.set_trace()
    # match = r'MI_0: \[(.*)\]'
    match = r'{ name: \"[0-9]\. (.*)\", mp3'
    # match = r'<script(.*)'
    tmp = re.compile(match)
    text = re.findall(tmp,source)
    return text

def download_music(name):
    domain = 'http://www.rui123.com/audio/'
    source_path = './source/' +name+'.mp3'
    url = domain + name + '.mp3'
    urllib.urlretrieve(url,source_path,Schedule)    

def download_music_html(url):
    name = url.split('/')[-2]
    music_url = 'http://www.rui123.com/' + url.split('/')[-2]+'/'
    local = './music/' +name
    urllib.urlretrieve(music_url,local,Schedule)


if __name__ == '__main__':
    # url_list = []
    # url ="http://www.rui123.com/music/"
    # source =  getHtml(url)
    # url_list = getMusicHtml(source)
    # f= open('url.txt', 'w+')
    # for url in url_list:
    #     f.write(url+'\n')
    #     download_music_html(url)
    # f.close()
    # print url_list[0]
    for html in os.listdir('./music'):
        f = open('./music/'+html)
        names = get_download_url(f.read())
        # print names
        for name in names:
            name1=  name.replace(' ','-')
            download_music(name1)