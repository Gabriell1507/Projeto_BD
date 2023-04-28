import mysql.connector
from faker import Faker
import random
import datetime

config =config = {
        'user': 'root',
        'password': 'gabriel',
        'host': 'localhost',
        'database': 'bibliotecabd',}

conn = mysql.connector.connect(**config)

cursor = conn.cursor()

criar_tabela_usuario = """
CREATE TABLE usuario (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(255),
  dtnascimento DATE,
  tipo VARCHAR(255),
  curso VARCHAR(255)
)
"""

criar_tabela_livros ="""
CREATE TABLE livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(255),
    titulo VARCHAR(255),
    ano_de_publicacao INT,
    area_de_conhecimento VARCHAR(255)
)
"""
