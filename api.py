from flask import Flask, jsonify, request
from app import *
from src.controllers.controller import *

#http://localhost:4000/

app.run(port=4000, host="localhost", debug= True)

@app.route("public/index", methods=["GET"])
def is_create_produtos():
    return jsonify(IndexController.get)

@app.route("/", methods=["POST"])
def is_delete_produtos():
    return jsonify(DeleteProdutosController.post)

@app.route("public/update", methods=["POST"])
def is_update_produtos():
    return jsonify(UpdateProdutosController.post)

@app.route("public/read", methods=["GET"])
def is_read_produtos():
    return jsonify(ReadProdutosController.get)
