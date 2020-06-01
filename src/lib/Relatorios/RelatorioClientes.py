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
cursor.execute("select distinct  A.CODIGO_CLI, NOME_CLI, DATA_PED, sum(b.CODIGO_CLI) AS TOTAL from cliente a inner join pedido b on a.CODIGO_CLI = b.CODIGO_CLI order by data_ped")

all_rows = cursor.fetchall()
print('RELATORIO DE CLIENTES QUE REALIZARAM PEDIDOS\n')
for row in all_rows:
    print('CODIGO CLIENTE: {0}\n NOME CLIENTE: {1}\n DATA PEDIDO: {2}\n QTD PEDIDOS: {3}'.format(row[0], row[1], row[2], row[3]))
    print('\n\n')

# fim da bifrost
Bifrost.connection.close()
