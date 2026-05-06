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

    if opcao == 1:
        titulo = str(input('Insira o nome do filme: '))
        categoria = str(input('Insira a categoria do filme: '))
        anoLancamento = int(input('Insira o ano de lançamento do fIlme: '))

        #insert
        insert = f'INSERT INTO filme (titulo, categoria, anoLancamento) VALUES ("{titulo}","{categoria}",{anoLancamento})'
        cursor.execute(insert)
        connect.commit()
        print(f'Filme {titulo}({anoLancamento}) adicionado com sucesso!')
    
    
    
    
    elif opcao == 5:
        print('Encerrando Programa!')
        break
print('encerrado.')



connect.close()
cursor.close()
