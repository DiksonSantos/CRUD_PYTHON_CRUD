from utils import menu


if __name__ == '__main__':
    menu()

"""
# Usado no Bando de Dados:

create database pmysql;
use pmysql;

CREATE TABLE produtos(
id INT primary KEY auto_increment,
NOME varcharacter(50) NOT NULL,
PRECO DECIMAL(8,2) NOT NULL,
ESTOQUE INT NOT NULL
);

select * from produtos;
"""
