#!/usr/bin/python
# Author: Schaden Philipp

# Description:
# A minimal Webcrawler to get all exisitng downloadlinks for libraries
# from https://github/adafruit and add it to the repo.cvs as Downloadsource-File
# for the ardlib.py by Sebastian Plamauer


import requests
import re
import csv
import urllib2
import itertools

def get_page(url, x):
    r = requests.get(url)
    #print r.status_code
    content = r.text.encode('utf-8', 'ignore')
    return content
    #with open("test"+x+".html", "w") as fp:
        #fp.write(content)

		
        
        
if __name__ == "__main__":
	#url = 'https://github.com/adafruit'
	#get_page(url,str(1))            

	for x in range(1,12):
   		url = 'https://github.com/adafruit?page='+str(x)
		content = get_page(url, str(x))
		#content = content.replace("\n",'')
		content_pattern_url = re.compile(r'/adafruit/[^/|"]*')
		resulturl = re.findall(content_pattern_url, content)
		
		content_pattern_name = re.compile(r"[^/ , \[ \]]*(?=\')")
		resultname=re.findall(content_pattern_name, str(resulturl))
		resulturl = set(resulturl)
		resultname = set(resultname)
		for url in resulturl:
			print url
		for name in resultname:		
			print name
			
		

		with open("test.csv","a") as csvfile:
			for url in resulturl:
				for name in resultname:
					if name != '':
						if name in url:
							url = 'https://github.com'+url+'/archive/master.zip'
							csvfile.write(name+','+url+','+'\n')		
		
		csvfile.close()

	          
