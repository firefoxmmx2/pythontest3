'''
Created on Apr 9, 2011

@author: hooxin
'''

def rename(prefix,lastfix,extname):
	filenamelist=[]
	
	for i in range(1,prefix+1):
		for j in range(lastfix):
			filenamelist.append(str(i)+'-'+str(j)+'.'+extname)

	return filenamelist


if __name__ == '__main__':
	print(rename(10,4,'jpg'))
	