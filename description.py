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
else:
	template = env.get_template('description.html')
	template = template.render(h2 = 1,
							title = "Descriptions")
print(template)											
