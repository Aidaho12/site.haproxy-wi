#!/usr/bin/env python3
#import funct
import cgi
import os, http.cookies
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates/'))


form = cgi.FieldStorage()
print('Content-type: text/html\n')

if form.getvalue('description') == 'servers':
	template = env.get_template('servers.html')
	template = template.render(h2 = 1,
							title = 'The "Adding servers" description')
elif form.getvalue('description') == 'creds':
	template = env.get_template('cred.html')
	template = template.render(h2 = 1,
							title = 'The "Credentials" description')
elif form.getvalue('description') == 'checker':
	template = env.get_template('checker.html')
	template = template.render(h2 = 1,
							title = 'The "Checker" description')
elif form.getvalue('description') == 'runtimeapi':
	template = env.get_template('runtimeapi.html')
	template = template.render(h2 = 1,
							title = 'The "Run Time API commands" descriptions')
elif form.getvalue('description') == 'logs':
	template = env.get_template('logs.html')
	template = template.render(h2 = 1,
							title = 'The "Internal logs" descriptions')
elif form.getvalue('description') == 'saved':
	template = env.get_template('saved.html')
	template = template.render(h2 = 1,
							title = 'Pre saved options and servers')
elif form.getvalue('description') == 'setup':
	template = env.get_template('setup.html')
	template = template.render(h2 = 1,
							title = 'How to setup servers, group and SSH credentials')
elif form.getvalue('description') == 'userlist':
	template = env.get_template('userlist.html')
	template = template.render(h2 = 1,
							title = 'About userlists')
elif form.getvalue('description') == 'api':
	template = env.get_template('api.html')
	template = template.render(h2 = 1,
							title = 'About userlists')
elif form.getvalue('description') == 'backup':
	template = env.get_template('backup.html')
	template = template.render(h2 = 1,
							title = 'Backup HAProxy`s configs')
elif form.getvalue('description') == 'nginx_status':
	template = env.get_template('nginx_status.html')
	template = template.render(h2 = 1,
							title = 'Nginx status page description')
else:
	template = env.get_template('description.html')
	template = template.render(h2 = 1,
							title = "Descriptions")
print(template)											
