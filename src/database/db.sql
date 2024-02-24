CREATE DATABASE IF NOT EXISTS produtosDB;

USE produtosDB;

CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR,
    preco DECIMAL(10, 2) NOT NULL,
    quantidade INT NOT NULL
);


ALTER TABLE produtos ADD FOREIGN KEY (id_produto) REFERENCES produtos(id)