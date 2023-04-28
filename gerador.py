import faker
import random
import datetime
import uteis

def gerar_user():
    fake = faker.Faker('pt_BR')
    nome = fake.name()
    dtnascimento = fake.date_of_birth()
    tipo = random.choice(['aluno', 'professor'])

    if tipo =='aluno':
        curso = random.choice(['Banco de Dados', 'Análise e Desenvolvimento de Sistemas', 'Desenvolvimento Web'])
    elif tipo == 'professor':
        curso = random.choice(['Banco de Dados', 'Análise e Desenvolvimento de Sistemas', 'Desenvolvimento Web',])

    else:
        curso = None

    return nome, dtnascimento, tipo, curso

def gerar_livro():
    fake = faker.Faker('pt_BR')
    isbn = fake.isbn13()
    isbn = str(isbn)
    area_de_conhecimento = random.choice(['Banco de Dados', 'Análise e Desenvolvimento de Sistemas', 'Desenvolvimento Web'])
    titulo = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    ano_de_publicacao = fake.year()

    return isbn, titulo, ano_de_publicacao, area_de_conhecimento

def gerar_emprestimo():
    fake = faker.Faker('pt_BR')
    hora_emprestimo = fake.time(pattern='%H:%M:%S', end_datetime=None)
    data_emprestimo = datetime.date.today() + datetime.timedelta(days=random.randint(1, 30))
    horario_devolucao = fake.time(pattern='%H:%M:%S', end_datetime=None)
    data_devolucao = data_emprestimo + datetime.timedelta(days=random.randint(1, 30))
    id_livros = random.randint(1, 400)
    id_usuario = random.randint(1, 600)

    return hora_emprestimo, data_emprestimo, horario_devolucao, data_devolucao, id_livros, id_usuario