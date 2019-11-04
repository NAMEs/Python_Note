#!/usr/bin/env python3

from wsgiref.simple_server import make_server


def simple_wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)

    return ['Hello world'.encode()]

httpd = make_server('', 8000, simple_wsgi_app)
print('Started app serving on port 8000...')
httpd.serve_forever()