import faker
import random
import datetime




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
    area = random.choice(['Banco de Dados', 'Análise e Desenvolvimento de Sistemas', 'Desenvolvimento Web'])
    titulo = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    ano_publicacao = fake.year()

    return isbn, titulo, ano_publicacao, area

def gerar_emprestimo():
    fake = faker.Faker('pt_BR')
    hremprestimo  = fake.time()
    dtemprestimo = datetime.date.today() + datetime.timedelta(days=random.randint(1, 30))
    hrdevolucao = fake.time()
    dtdevolucao = dtemprestimo + datetime.timedelta(days=random.randint(1, 30))
    id_livro = random.randint(1, 400)
    id_usuario = random.randint(1, 600)

    return id_livro, id_usuario, dtemprestimo, hremprestimo , dtdevolucao, hrdevolucao