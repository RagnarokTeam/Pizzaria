 from src.db.Asgard import Bifrost


# variavel "cursor" pode ser alterada para qualquer outro nome de sua escolha
cursor = Bifrost.connection.cursor()
cursor.execute("select distinct codigo_piz, tipo_piz, data_criacao, data_inativacao, nome_piz, ingredientes, valor_custo,valor_custo, (valor_custo * 1.15) as pizza_media,(valor_custo * 1.25) as pizza_grande,(valor_custo * 1.35) as pizza_gigante from pizza")
user1 = cursor.fetchone()  # retrieve the first row
print('\nImpressao de campo a campo')
print('Cod: ', codigo_piz[0])
print('Tipo: ', tipo_piz[1])
print('Data criação: ', data_criacao[2])
print('Data Inativação: ', data_inativação[3])
print('Nome da pizza: ', nome_piz[4])
print('Ingredientes: ', ingredientes[5])
print('Valor custo: ', valor_custo[6])
print('Valor pizza média: ', pizza_media[7])
print('Valor pizza grande: ', pizza_grande[8])
print('Valor pizza gigante: ', pizza_gigante[9])



print('\nImpressao de toda as tuplas')
all_rows = cursor.fetchall()
for row in all_rows:
    # row[0] retorna a primeira coluna da query (id),
    # row[1] retorna a segunda coluna (nome)
    print('{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8} , {9}'.format(row[0], row[1], row[2], row[3], row[4], row [5], row[6], row[7], row[8], row[9]))


# fim da bifrost
Bifrost.connection.close()
