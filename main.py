import faker
import mysql.connector
import uteis
import gerador



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
    opcoes = input('Digite 1 para gerar dados, 2 para consultar dados, 3 para quantidade de dados, 4 para sair: ')

    if opcoes == '1':
        opcao = input('Digite 1 para gerar dados de usuário, 2 para gerar dados de livro, 3 para gerar dados de empréstimo: ')

        if opcao == '1':
            quantidade = int(input('Digite a quantidade de usuários que deseja gerar: '))
            print('Gerando dados de usuário...')

            for i in range(quantidade):
                usuario = gerador.gerar_user()
                cursor.execute("INSERT INTO usuario (nome, dtnascimento, tipo, curso) VALUES (%s, %s, %s, %s)", usuario)
                conn.commit()

        elif opcao == '2':
            quantidade = int(input('Digite a quantidade de livros que deseja gerar: '))
            print('Gerando dados de livro...')

            for i in range(quantidade):
                livro = gerador.gerar_livro()
                cursor.execute("INSERT INTO livros (isbn, titulo, ano_de_publicacao, area_de_conhecimento) VALUES (%s, %s, %s, %s)", livro)
                conn.commit()

        elif opcao == '3':
            quantidade = int(input('Digite a quantidade de empréstimos que quer fazer: '))
            print('Gerando dados de empréstimo...')

            for i in range(quantidade):
                emprestimo = gerador.gerar_emprestimo()
                cursor.execute("INSERT INTO emprestimo1 (id_livros, id_usuario, data_emprestimo, hora_emprestimo, data_devolucao, horario_devolucao) VALUES (%s, %s, %s, %s, %s, %s)", emprestimo)
                conn.commit()

    elif opcoes == '2':
        opcao = input('Digite 1 para consultar dados de usuário, 2 para consultar dados de livro, 3 para consultar dados de empréstimo: ')

        if opcao == '1':
            cursor.execute("SELECT * FROM usuario")
            uteis.select(cursor)

        elif opcao == '2':
            cursor.execute("SELECT * FROM livros")
            uteis.select(cursor)

        elif opcao == '3':
            cursor.execute("SELECT * FROM emprestimo1")
            uteis.select(cursor)

    elif opcoes == '3':
        opcao = input('Digite 1 para consultar quantidade de usuários, 2 para consultar quantidade de livros, 3 para consultar quantidade de empréstimos: ')

        if opcao == '1':
            cursor.execute("SELECT * FROM usuario")
            uteis.returned_data(cursor)

        elif opcao == '2':
            cursor.execute("SELECT * FROM livro")
            uteis.returned_data(cursor)

        elif opcao == '3':
            cursor.execute("SELECT * FROM emprestimos")
            uteis.returned_data(cursor)

    elif opcoes == '4':
        break

    else:
        print('Opção inválida')

cursor.close()
