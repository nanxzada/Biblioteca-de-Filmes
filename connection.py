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
    
    elif opcao == 2: 
        idFilme = int(input('Insira o ID do Filme que deseja editar: '))
        novo_titulo = str(input('Insira o novo titulo: '))
        nova_categoria = str(input('Insira a nova categoria: '))
        novo_anoLancamento = int(input('Insira o novo ano de lançamento: '))
        #update
        update = f'UPDATE filme SET titulo = "{novo_titulo}", categoria = "{nova_categoria}", anoLancamento = {novo_anoLancamento} WHERE idFilme = {idFilme}'
        cursor.execute(update)
        connect.commit()
        print('Filme atualizado com sucesso')
    
    elif opcao == 3:
        idFilme = int(input('Digite o ID do filme que deseja excluir: '))
        #delete
        nome_filme = f'SELECT * FROM filme WHERE idFilme = {idFilme}'
        cursor.execute(nome_filme)
        nomeFilmeExcluido = cursor.fetchall()
        delete = f'DELETE FROM filme WHERE idFilme = {idFilme}'
        cursor.execute(delete)
        connect.commit()
        print(f'Filme Nº{idFilme}({nomeFilmeExcluido}) foi excluído com sucesso.')
    
    elif opcao == 5:
        print('Encerrando Programa!')
        break
print('encerrado.')



connect.close()
cursor.close()
