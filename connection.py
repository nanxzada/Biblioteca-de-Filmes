import mysql.connector

connect = mysql.connector.connect(user='root', 
                                password='R3n4nm0t4080406%',
                                host='localhost',
                                database='Filmes')
cursor = connect.cursor()


#Menu de opções

print('Operando Biblioteca de Filmes')
while True:
    opcao = int(input('Selecione uma das opções:'
    '\n1- Adicionar Filme.' \
    '\n2- Editar Filme.' \
    '\n3- Excluir Filme.' \
    '\n4- Buscar Filmes.'
    '\n5- Sair.\n'))

    




connect.close()
cursor.close()