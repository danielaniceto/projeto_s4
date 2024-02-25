from flask.views import MethodView
from flask import request, render_template, redirect
from conectio_db import mysql

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
            cursor_banco.execute("INSERT INTO produtos (id, nome, descricao, quantidade) VALUES (%s, %s, %s, %s)", (id, nome, descricao, quantidade))
            cursor_banco.connection.commit()
            return redirect("/")
        
class DeleteProdutosController(MethodView):
    def post(self, id):
        with mysql.cursor() as cursor_banco:
            cursor_banco.execute("DELETE FROM produtos WHERE id = %s", (id))
            cursor_banco.connection.commit()
            return redirect("/")

class UpdateProdutosController(MethodView):
    def post(self, id):
        with mysql.cursor() as cursor_banco:
            cursor_banco.execute("SELECT * FROM produtos WHERE id = %s", (id))
            produto = cursor_banco.fetchone()
            return render_template("public/update.html", produto = produto)
        
    def post(self, id):
        id_produto = request.form["id"]
        nome = request.form["nome"]
        descricao = request.form["descicao"]
        quantidade = request.form["quantidade"]

        with mysql.cursor() as cursor_banco:
            cursor_banco.execute("UPDATE produtos SET id = %s, nome = %s, descricao = %s, quantidade = %s WHERE" (id_produto, nome, descricao, quantidade, id))
            cursor_banco.commit()
            return redirect("/")

class ReadProdutosController(MethodView):
    def get(self):
        with mysql.cursor() as cursor_banco:
            cursor_banco.execute("SELECT FROM * produtos")
            data = cursor_banco.fetchall
        return render_template("public/read.html", data = data)
