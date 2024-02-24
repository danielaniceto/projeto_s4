from src.controllers.controller import *
from src.controllers.erros import *


routes = {
    "ola_route":"/", "controller": Controller.as_view("Ola"),
    "not_found_route":"/404", "NotFoundController": NotFoundController.as_view("Ola"),
    }