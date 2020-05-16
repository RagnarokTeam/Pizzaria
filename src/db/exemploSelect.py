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

from Asgard import Bifrost


# variavel "cursor" pode ser alterada para qualquer outro nome de sua escolha
cursor = Bifrost.connection.cursor()
cursor.execute("SELECT id, nome, cidade, salario from cliente")
user1 = cursor.fetchone()  # retrieve the first row
print('\nImpressao de campo a campo')
print('Id:', user1[0])  # Imprime o primeiro campo
print('Nome:', user1[1])  # Imprime o segundo campo
print('Cidade:', user1[2])  # Imprime o terceiro campo
print('Salario:', user1[3])  # Imprime o quarto campo

print('\nImpressao de toda as tuplas')
all_rows = cursor.fetchall()
for row in all_rows:
    # row[0] retorna a primeira coluna da query (id),
    # row[1] retorna a segunda coluna (nome)
    print('{0}, {1}, {2}, {3}'.format(row[0], row[1], row[2], row[3]))


# fim da bifrost
Bifrost.connection.close()
