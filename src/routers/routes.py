from src.controllers.controller import *
from src.controllers.erros import *


routes = {
    "index_route":"/", "index_controller": Controller.as_view("Index"),
    "not_found_route":"/404", "NotFoundController": NotFoundController.as_view("Not_Found"),
    }