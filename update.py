#!/usr/bin/env python3
#import funct
import os, http.cookies
import cgi
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates/'))
template = env.get_template('update.html')
form = cgi.FieldStorage()
 	
print('Content-type: text/html\n')
if form.getvalue('last_ver'):
	import glob
	import os
	list_of_files = glob.glob('/var/www/repo.haproxy-wi/el7/haproxy-wi-3*')
	latest_file = max(list_of_files, key=os.path.getctime)
	latest_file = latest_file.split('/')[-1]
	latest_file = latest_file.split('noarch')[0]
	latest_file_ver = latest_file.split('-')[2]
	latest_file_rel = latest_file.split('-')[3]
	version = latest_file_ver+'.'+latest_file_rel
	version = (version[::-1].replace('.'[::-1],''[::-1], 1))[::-1]
	#print('3.6.5.1')	

	print(version)										
									
