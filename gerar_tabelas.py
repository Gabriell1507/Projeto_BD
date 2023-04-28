import mysql.connector


config =config = {
        'user': 'root',
        'password': 'gabriel',
        'host': 'localhost',
        'database': 'bibliotecabd',}

conn = mysql.connector.connect(**config)

cursor = conn.cursor()

criar_tabela_usuario = """
CREATE TABLE usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome varchar(64),
    dtnascimento date,
    tipo varchar(30),
    curso varchar(100000)
)
"""

criar_tabela_livros = """
CREATE TABLE livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
titulo varchar(100),
    isbn integer,
    area varchar(30),
    ano_publicacao smallint
);"""

criar_tabela_emprestimo = """
CREATE TABLE emprestimos (
    id INT AUTO_INCREMENT PRIMARY KEY,
id_usuario integer NOT NULL,
    id_livro integer NOT NULL,
    dtemprestimo date,
    hremprestimo time,
    dtdevolucao date,
    hrdevolucao time,
    FOREIGN KEY (id_usuario) REFERENCES usuarios (id),
    FOREIGN KEY (id_livro) REFERENCES livros (id)
);"""