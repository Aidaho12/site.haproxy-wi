#!/usr/bin/env python3
#import funct
import os, http.cookies
import cgi
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates/'))
template = env.get_template('changelog.html')
	
print('Content-type: text/html\n')

template = template.render(h2 = 1,
							title = "Changelog",
							description = "Changelog/Roadmap")
print(template)												
									
