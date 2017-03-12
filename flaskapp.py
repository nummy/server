from flask import Flask
from flask import Response

flaskapp = Flask("flaskapp")

@flaskapp.route("/hello")
def hello():
	return Response("Hello, world from Flask!", mimetype="text/plain")

app = flaskapp.wsgi_app