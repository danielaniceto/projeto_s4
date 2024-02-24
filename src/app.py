from flask import Flask
from src.routers.routes import *

app = Flask(__name__)

app.add_url_rule(routes["index_route"], view_func=routes["index_controller"])
app.register_error_handler(routes["not_found_route"], routes["NotFoundController"])
