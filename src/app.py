from flask import Flask
from src.routers.routes import *

app = Flask(__name__)

app.add_url_rule(routes["index_route"], view_func=routes["index_controller"])

app.register_error_handler(routes["not_found_route"], routes["NotFoundController"])

app.add_url_rule(routes["delete_route"], view_func=routes["delete_controller"])

app.add_url_rule(routes["update_route"], view_func=routes["update_controller"])

app.add_url_rule(routes["read_route"], view_func=routes["read_controller"])
