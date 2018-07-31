import bottle
import time
from bottle import route, run

@route('/hello/<name>')
def hello(name):
    time.sleep(10)
    return '<h1>Hello Bottle!</h1>'

print "Intialization Succefull-------------------------------"
app = bottle.default_app()

#run(host='localhost', port=8080)
