"""
Data........: 2020-05-14
Projeto.....: RagnarokProject - Pizzaria
Arquivo.....: Fenrir.py
Descrição...: Desacorrentamento generalizada para toda a aplicação utilizando função
Autor.......: Jefferson de L. Matos - Eq. Ragnarok
Observações.: 2020-05-22 - [R00] Criação do Arquivo - Versao 1.00
              ...
Referencias:
"""
from datetime import datetime
from src.db.Asgard import Bifrost


def GETDATE():
    data = datetime.now().strftime("%d/%m/%Y")
    return data

def selectValorPadraoPizza(Tamanho,nomePizza):
    # inicialmente vou usar apenas por nome mas o correto é se usar o cod
    cursor = Bifrost.connection.cursor()
    cursor.execute('SELECT DISTINCT CODIGO_PIZ,NOME_PIZ, VALOR_CUSTO FROM PIZZA '
                   'WHERE DATA_INATIVACAO IS NULL'
                   ' AND NOME_PIZ LIKE ?', ('%' + nomePizza + '%',))

    data = cursor.fetchone()

    # verificando qual a porcentagem usar
    if data is not None:
        valorPadrao = data[2]
        if Tamanho == 'gigante':
            valorPadrao = valorPadrao * 1.35
        elif Tamanho == 'grande':
            valorPadrao = valorPadrao * 1.25
        else:
            valorPadrao = valorPadrao * 1.15


    return valorPadrao

#tam = tamanho da pizza
#nomePizza = nome da pizza
#meia = é 1/2 pizza? passe 1 é inteira? passe 0. só passe se for meia pizza;
#nomePizza2 = necessario se passar meia.
#em casos de ERRO ela vai retornar 1, caso tenha sucesso retorna o valor da pizza de acordo
#com a documentacao


def CalculaValorFinalPizza(Tamanho, nomePizza, meia = 0, nomePizza2 = 'null' ):

    valorPizza = valorPadrao1 = float(selectValorPadraoPizza(Tamanho,nomePizza))

    if meia != 0:

        valorPadrao1 = valorPadrao1/2
        valorPadrao2 = float(selectValorPadraoPizza(Tamanho,nomePizza2))/2

        if valorPadrao1 > valorPadrao2:
            valorPizza = valorPadrao1 *2
        else:
            valorPizza = valorPadrao2 *2

    return valorPizza

def ListarPizzasCadastradas():
    cursor = Bifrost.connection.cursor()
    cursor.execute('SELECT * FROM PIZZA',)

    cursor.connection.close()
    return  0
