#!/usr/bin/env python3
#filename: pbaidubaike.py

import urllib ,re
import sys
from urllib.request import urlopen
def getHtml(url,time=10):
	response = urlopen(url,timeout=time)
	html = response.read()
	response.close()
	return html

def clearBlank(html):
	if len(html) == 0: return ''
	html = re.sub('\r|\n|\t','',html)
	while html.find('   ') != -1 or html.find('&nbsp;') != -1:
		html = html.replace('&nbsp;',' ').replace('  ',' ')
	return html

if __name__ == '__main__':
	html = getHtml('http://baike.baidu.com/view/994462.htm',10)
	html = html.decode('gb2312','replace').encode('utf8')

	title_reg = r'<h1 class="title" id="[\d]+">(.*?)</h1>'
	content_reg = r'<div class="card-summary-content">(.*?)</p>'

	title = re.compile(title_reg).findall(html)
	content = re.compile(content_reg).findall(html)

	title[0] = re.sub(r'<[^>]*?>','',title[0])
	content[0] = re.sub(r'<[^>]*?>','',content[0])

	print(title[0])
	print('#' * 20)
	print(content[0])
	