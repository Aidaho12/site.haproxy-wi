#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import http.cookies
import sql
import datetime
import uuid
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates/'), autoescape=True)
template = env.get_template('login.html')
import cgi
	
form = cgi.FieldStorage()

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
user_id = cookie.get('uuid')
ref = form.getvalue('ref')
login = form.getvalue('login')
password = form.getvalue('pass')
error_log = ""
error = ""

def send_cookie(login):
	session_ttl = int()
	session_ttl = 2
	expires = datetime.datetime.utcnow() + datetime.timedelta(days=session_ttl) 
	user_uuid = str(uuid.uuid4())
	user_token = str(uuid.uuid4())
	sql.write_user_uuid(login, user_uuid)
	
	id = sql.get_user_id_by_uuid(user_uuid)

	c = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
	c["uuid"] = user_uuid
	c["uuid"]["path"] = "/"
	c["uuid"]["expires"] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")

	print(c)
	print("Content-type: text/html\n")			
	print('ok')
	sys.exit()	
	
	
def ban():
	c = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
	expires = datetime.datetime.utcnow() + datetime.timedelta(seconds=10)
	c["ban"] = 1
	c["ban"]["path"] = "/"
	c["ban"]["expires"] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
	print(c)
	print("Content-type: text/html\n")			
	print('ban')
	
	
if ref is None:
	ref = "/cabinet.py"	
	
if form.getvalue('error'):
	error_log = '<div class="alert alert-danger">Somthing wrong :( I\'m sad about this, but try again!</div><br /><br />'

	
if form.getvalue('logout'):
	try:
		sql.delete_uuid(user_id.value)
	except:
		pass
	print("Set-cookie: uuid=; expires=Wed, May 18 03:33:20 2003; path=/; httponly")
	print("Content-type: text/html\n")
	print('<meta http-equiv="refresh" content="0; url=/">')
	sys.exit()

if login is not None and password is not None:
	import bcrypt
	USERS = sql.select_users(user=login)
			
	for users in USERS:	
		if login in users[1] and bcrypt.checkpw(password.encode('utf-8'), users[3].encode('utf-8')):
			send_cookie(login)
			break
		else:
			ban()
			sys.exit()
	else:
		ban()
		sys.exit()
	print("Content-type: text/html\n")	
	
	
if login is None:
	print("Content-type: text/html\n")	
	

output_from_parsed_template = template.render(h2 = 0, title = "Login page",										
													error_log = error_log,
													error = error,
													ref = ref)											
print(output_from_parsed_template)
