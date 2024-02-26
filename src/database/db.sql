CREATE DATABASE produtosDB;

USE produtosDB;

CREATE TABLE [IF NOT EXISTS] produtos (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL, 
    descricao VARCHAR(5000), 
    preco DECIMAL DOUBLE NOT NULL,
    quantidade INT NOT NULL,
);

ALTER TABLE produtos ADD FOREIGN KEY(id_produto) REFERENCES produtos(id)
