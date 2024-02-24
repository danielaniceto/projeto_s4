from flask.views import MethodView
from flask import request, render_template, redirect
from src.db import mysql

class Controller(MethodView):
    def get(self):
        return "Teste"
    
    def postr(self):
        id = request.form["id"]
        nome = request.form["nome"]
        descricao = request.form["descicao"]
        quantidade = request.form["quantidade"]
        