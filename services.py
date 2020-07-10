#!/usr/bin/env python3
import cgi
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates/'))

form = cgi.FieldStorage()
print('Content-type: text/html\n')

if form.getvalue('service') == 'grafana':
    template = env.get_template('services/grafana.html')
    template = template.render(h2=1,
                               title='About Grafana and Prometheus servers')
elif form.getvalue('service') == 'checker':
    template = env.get_template('services/checker.html')
    template = template.render(h2=1,
                               title='The "Checker" service description')
elif form.getvalue('service') == 'auto_start':
    template = env.get_template('services/auto_start.html')
    template = template.render(h2=1,
                               title='The "Auto start" service description')
elif form.getvalue('service') == 'fail2ban':
    template = env.get_template('services/fail2ban.html')
    template = template.render(h2=1,
                               title='The "Fail2ban" service description')
elif form.getvalue('service') == 'smon':
    template = env.get_template('services/smon.html')
    template = template.render(h2=1,
                               title='The "Simple monitoring network ports" service description')
else:
    template = env.get_template('services/services.html')
    template = template.render(h2=1,
                               title="About HAProxy-WI services")
print(template)
