
import sys
import json

from bottle import Bottle, static_file, response, request

def get_handler(name):
    print 'Get: {}'.format(name)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps({ 'name': name })

def put_handler(name):
    print 'Put: {}'.format(name)
    try:
        data = json.load(request.body)
        print data
    except:
        response.status = 400

    response.headers['Content-Type'] = 'application/json'

def main():
    app = Bottle()
    app.route('/', method='GET', callback=lambda: static_file('index.html', root='appname/views/'))
    app.route('/media/<name>', method='GET', callback=lambda name: static_file('media/' + name, root='appname/views/'))
    app.route('/api/<name>', method='GET', callback=get_handler)
    app.route('/api/<name>', method='PUT', callback=put_handler)
    app.run(host='localhost', port=8080)

if __name__ == '__main__':
    sys.exit(main())
