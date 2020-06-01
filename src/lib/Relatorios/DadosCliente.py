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
print('\nRELATÓRIO DE CLIENTES')
all_rows = cursor.fetchall()
for user1 in all_rows:
    print('----------------------------------------------------------')
    print('Codigo Cliente:', user1[0])  # Imprime o primeiro campo
    print('Telefone:', user1[1])  # Imprime o segundo campo
    print('Celular:', user1[2])  # Imprime o terceiro campo
    print('Nome:', user1[3])  # Imprime o terceiro campo
    print('Endereço:', user1[4])  # Imprime o quarto campo
    print('Número:', user1[5])  # Imprime o quarto campo
    print('Complemento:', user1[6])  # Imprime o quarto campo
    print('Bairro:', user1[7])  # Imprime o quarto campo
    print('Cidade:', user1[8])  # Imprime o quarto campo
    print('UF:', user1[9])  # Imprime o quarto campo
    print('Data Cadastro:', user1[10])  # Imprime o quarto campo
    print('Data Inativo:', user1[11])  # Imprime o quarto campo

# fim da bifrost
Bifrost.connection.close()
