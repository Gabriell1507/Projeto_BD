import mysql.connector
import gerador


def select(cursor):
    for row in cursor:
        print(row, '\n')


def returned_data(cursor):
    count = 0
    for row in cursor:
        count += 1
    print(count, 'registros retornados')


config = {
        'user': 'root',
        'password': 'gabriel',
        'host': 'localhost',
        'database': 'trabalhobd',}

conn = mysql.connector.connect(**config)

cursor = conn.cursor()

if conn.is_connected():
    db_info = conn.get_server_info()
    print('Conectado ao servidor MySQL versão', db_info)
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print('Conectado ao banco de dados', linha)
else:
    print('Não foi possível conectar ao banco de dados')

while True:
    opcoes = input('Digite 1 para gerar dados\n2 para consultar dados\n3 para quantidade de dados\n4 para sair:\n ')

    if opcoes == '1':
        opcao = input('Digite 1 para gerar dados de usuário\n2 para gerar dados de livro\n3 para gerar dados de empréstimo:\n ')

        if opcao == '1':
            quantidade = int(input('Digite a quantidade de usuários que deseja gerar: '))
            print('Gerando dados de usuário...')

            for i in range(quantidade):
                usuario = gerador.gerar_user()
                cursor.execute("INSERT INTO usuarios (nome, dtnascimento, tipo, curso) VALUES (%s, %s, %s, %s)", usuario)
                conn.commit()

        elif opcao == '2':
            quantidade = int(input('Digite a quantidade de livros que deseja gerar: '))
            print('Gerando dados de livro...')

            for i in range(quantidade):
                livro = gerador.gerar_livro()
                cursor.execute("INSERT INTO livros (isbn, titulo, ano_publicacao, area) VALUES (%s, %s, %s, %s)", livro)
                conn.commit()

        elif opcao == '3':
            quantidade = int(input('Digite a quantidade de empréstimos que quer fazer: '))
            print('Gerando dados de empréstimo...')

            for i in range(quantidade):
                emprestimo = gerador.gerar_emprestimo()
                cursor.execute("INSERT INTO emprestimos (id_livro, id_usuario, dtemprestimo, hremprestimo , dtdevolucao, hrdevolucao) VALUES (%s, %s, %s, %s, %s, %s)", emprestimo)
                conn.commit()

    elif opcoes == '2':
        opcao = input('Digite 1 para consultar usuários\n2 para consultar livros\n3 para consultar empréstimos:\n ')

        if opcao == '1':
            cursor.execute("SELECT * FROM usuarios")
            select(cursor)

        elif opcao == '2':
            cursor.execute("SELECT * FROM livros")
            select(cursor)

        elif opcao == '3':
            cursor.execute("SELECT * FROM emprestimos")
            select(cursor)

    elif opcoes == '3':
        opcao = input('Digite 1 para consultar quantidade de usuários\n2 para consultar quantidade de livros\n3 para consultar quantidade de empréstimos:\n ')

        if opcao == '1':
            cursor.execute("SELECT * FROM usuarios")
            returned_data(cursor)

        elif opcao == '2':
            cursor.execute("SELECT * FROM livros")
            returned_data(cursor)

        elif opcao == '3':
            cursor.execute("SELECT * FROM emprestimos")
            returned_data(cursor)

    elif opcoes == '4':
        break

    else:
        print('Opção inválida')

cursor.close()
