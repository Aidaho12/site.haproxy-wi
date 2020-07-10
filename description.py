#!/usr/bin/env python3
#import funct
import cgi
import os, http.cookies
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates/'))


form = cgi.FieldStorage()
print('Content-type: text/html\n')

if form.getvalue('description') == 'servers':
	template = env.get_template('description/servers.html')
	template = template.render(h2 = 1,
							title = 'The "Adding servers" description',
							description = 'The "Adding servers" description')
elif form.getvalue('description') == 'creds':
	template = env.get_template('description/cred.html')
	template = template.render(h2 = 1,
							title = 'The "Credentials" description',
							description = 'The "Credentials" description')
elif form.getvalue('description') == 'checker':
	print('<meta http-equiv="refresh" content="0; url=https://haproxy-wi.org/services.py?service=checker">')
elif form.getvalue('description') == 'runtimeapi':
	template = env.get_template('description/runtimeapi.html')
	template = template.render(h2 = 1,
							title = 'The "Run Time API commands" descriptions',
							description = 'The "Run Time API commands" descriptions')
elif form.getvalue('description') == 'logs':
	template = env.get_template('description/logs.html')
	template = template.render(h2 = 1,
							title = 'The "Internal logs" descriptions',
							description = 'The "Internal logs" descriptions')
elif form.getvalue('description') == 'saved':
	template = env.get_template('description/saved.html')
	template = template.render(h2 = 1,
							title = 'Pre saved options and servers',
							description = 'Pre saved options and servers')
elif form.getvalue('description') == 'setup':
	template = env.get_template('description/setup.html')
	template = template.render(h2 = 1,
							title = 'How to setup servers, group and SSH credentials',
							description = 'How to setup servers, group and SSH credentials')
elif form.getvalue('description') == 'userlist':
	template = env.get_template('description/userlist.html')
	template = template.render(h2 = 1,
							title = 'About userlists',
							description = 'About userlists')
elif form.getvalue('description') == 'api':
	template = env.get_template('description/api.html')
	template = template.render(h2 = 1,
							title = 'About userlists',
							description = 'About userlists')
elif form.getvalue('description') == 'backup':
	template = env.get_template('description/backup.html')
	template = template.render(h2 = 1,
							title = 'Backup HAProxy`s configs',
							description = 'Backup HAProxy`s configs')
elif form.getvalue('description') == 'nginx_status':
	template = env.get_template('description/nginx_status.html')
	template = template.render(h2 = 1,
							title = 'Nginx status page description',
							description = 'Nginx status page description')
elif form.getvalue('description') == 'waf':
	template = env.get_template('description/waf.html')
	template = template.render(h2 = 1,
							title = 'WAF',
							description = 'Web application firewall')
else:
	template = env.get_template('description/description.html')
	template = template.render(h2 = 1,
							title = "Descriptions",
							description = "Descriptions")
print(template)											
