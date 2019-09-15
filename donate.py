#!/usr/bin/env python3
#import funct
import os, http.cookies
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates/'))
template = env.get_template('donate.html')
	
print('Content-type: text/html\n')

template = template.render(h2 = 1,
							title = "Support the project!")
print(template)											
