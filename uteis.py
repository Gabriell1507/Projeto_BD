

def select(cursor):
    for row in cursor:
        print(row)


def returned_data(cursor):
    count = 0
    for row in cursor:
        count += 1
    print(count, 'registros retornados')