from flask.views import MethodView
from flask import request, render_template, redirect
from src.db import mysql

class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cursor_banco:
            cursor_banco.execute("SELECT * FROM produtos")
            data = cursor_banco.fetchall
        return render_template("public/index.html", data = data)
    
    def post(self):
        id = request.form["id"]
        nome = request.form["nome"]
        descricao = request.form["descicao"]
        quantidade = request.form["quantidade"]

        with mysql.cursor() as cursor_banco:
            cursor_banco.execute("INSERT INTO produtos values(%s, %s, %s, %s)", (id, nome, descricao, quantidade))
            cursor_banco.connection.commit()
            return redirect("/")
        
class DeleteProdutosController(MethodView):
    def get(self, id):
        return "Deletado com Sucesso"
        