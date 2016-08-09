from flask import Flask 
from flask import render_template
from arduinohandler import arduinoHandler

app = Flask(__name__)
handler = arduinoHandler()

@app.route('/')
def index():
	return render_template('action.html')

@app.route('/left', methods = ["POST"])
def left():
	print "left"
	handler.left(1)
	return "ok"

@app.route('/right', methods = ["POST"])
def right():
	print "right"
	handler.right(1)
	return "ok"

@app.route('/up', methods = ["POST"])
def up():
	print "up"
	handler.up(1)
	return "ok"

@app.route('/down', methods = ["POST"])
def down():
	print "down"
	handler.down(1)
	return "ok"
app.debug = True

if (__name__) == '__main__':
	app.run(host = '0.0.0.0', threaded=True)