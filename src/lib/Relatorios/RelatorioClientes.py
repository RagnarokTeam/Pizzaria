# """
# Data........: 2020-05-15
# Projeto.....: Pizzaria-Ragnarok
# Arquivo.....: exemploSelect.py
# Descrição...: Exemplo de consulta utilizando a Bifrost fazendo a consulta de dados na tabela cliente de todos regitros
# Autor.......: Jefferson de Lima - Eq. Ragnarok
# Observações.: 2020-05-08 - [R00] Criação do Arquivo - Versao 1.00
#
# Referencias:
# """

# inicio da bifrost

from src.db.Asgard import Bifrost


# variavel "cursor" pode ser alterada para qualquer outro nome de sua escolha
cursor = Bifrost.connection.cursor()
cursor.execute("select CODIGO_CLI, NOME_CLI, DATA_PED, sum(b.CODIGO_CLI) AS TOTAL from cliente a inner join pedido b on a.CODIGO_CLI = b.CODIGO_CLI order by data_ped")
user1 = cursor.fetchone()  # retrieve the first row
print('\nImpressao de campo a campo')
print('CODIGO_CLI:', user1[0])  # Imprime o primeiro campo
print('NOME_CLI:', user1[1])  # Imprime o segundo campo
print('DATA_PED:', user1[2])  # Imprime o terceiro campo
print('TOTAL:', user1[3])  # Imprime o quarto campo
(number_of_rows,)=cursor.fetchone()

print('\nImpressao de toda as tuplas')
all_rows = cursor.fetchall()
for row in all_rows:
    # row[0] retorna a primeira coluna da query (id),
    # row[1] retorna a segunda coluna (nome)
    print('{0}, {1}, {2}, {3}'.format(row[0], row[1], row[2], row[3]))


# fim da bifrost
Bifrost.connection.close()
