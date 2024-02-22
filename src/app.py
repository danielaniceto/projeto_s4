from flask import Flask
from src.routers.routes import *

app = Flask(__name__)

app.add_url_rule(routes["ola_route"], view_func=routes["controller"])
