#-*- coding:utf-8 -*-

import os
import sys
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'
 
path = os.path.dirname(os.path.abspath(__file__)) + '/'
if path not in sys.path:
    sys.path.insert(1, path)
 
from django.core.handlers.wsgi import WSGIHandler



def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    body=["Welcome to Baidu Cloud!\n"]
    return body

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(WSGIHandler())
