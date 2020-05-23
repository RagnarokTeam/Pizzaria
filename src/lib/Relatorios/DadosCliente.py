# """
# Data........: 2020-05-15
# Projeto.....: Pizzaria-Ragnarok
# Arquivo.....: exemploSelect.py
# Descrição...: Exemplo de consulta utilizando a Bifrost fazendo a consulta de dados na tabela cliente de todos regitros
# Autor.......: Paula Tanaka - Eq. Ragnarok
# Observações.: 2020-05-08 - [R00] Criação do Arquivo - Versao 1.00
#
# Referencias:
# """

# inicio da bifrost

from src.db.Asgard import Bifrost


# variavel "cursor" pode ser alterada para qualquer outro nome de sua escolha
cursor = Bifrost.connection.cursor()
cursor.execute("select CODIGO_CLI,TEL_FIXO,TEL_CEL,NOME_CLI,ENDERECO,NR_END,COMPLEMENTO,BAIRRO,CIDADE,UF,DATA_CADASTRO, DATA_INATIVO from cliente")
user1 = cursor.fetchone()  # retrieve the first row
print('\nImpressao de campo a campo')
print('Codigo Cliente:', CODIGO_CLI[0])  # Imprime o primeiro campo
print('Telefone:', TEL_FIXO[1])  # Imprime o segundo campo
print('Celular:', TEL_CEL[2])  # Imprime o terceiro campo
print('Nome:', NOME_CLI[3])  # Imprime o terceiro campo
print('Endereço:', ENDERECO[4])  # Imprime o quarto campo
print('Número:', NR_END[5])  # Imprime o quarto campo
print('Complemento:', COMPLEMENTO[6])  # Imprime o quarto campo
print('Bairro:', BAIRRO[7])  # Imprime o quarto campo
print('Cidade:', CIDADE[8])  # Imprime o quarto campo
print('UF:', UF[9])  # Imprime o quarto campo
print('Data Cadastro:', DATA_CADASTRO[10])  # Imprime o quarto campo
print('Data Inativo:', DATA_INATIVO[11])  # Imprime o quarto campo

print('\nImpressao de toda as tuplas')
all_rows = cursor.fetchall()
for row in all_rows:
    # row[0] retorna a primeira coluna da query (id),
    # row[1] retorna a segunda coluna (nome)
    print('{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))


# fim da bifrost
Bifrost.connection.close()
