"""
Data........: 2020-05-14
Projeto.....: RagnarokProject - Pizzaria
Arquivo.....: Fenrir.py
Descrição...: Conexão generalizada para toda a aplicação
Autor.......: Jefferson de L. Matos - Eq. Ragnarok
Observações.: 2020-05-22 - [R00] Criação do Arquivo - Versao 1.00
              ...
Referencias:
"""
from datetime import datetime
from src.db.Asgard import Bifrost


print(numpy)
def GETDATE():
    data = datetime.now().strftime("%d/%m/%Y")
    return data

#tam = tamanho da pizza
#nomePizza = nome da pizza
#meia = é 1/2 pizza? passe 1.5 é inteira? passe 1.

#em casos de ERRO ela vai retornar 1, caso tenha sucesso retorna o valor da pizza de acordo
#com a documentacao

def CalculaTamPizza(Tam, nomePizza, meia):
    # inicialmente vou usar apenas por nome mas o correto é se usar o cod
    cursor = Bifrost.connection.cursor()
    SQL = ('SELECT CODIGO_PIZ,NOME_PIZ, VALOR_CUSTO '
           'FROM PIZZA'
           'WHERE NOME_PIZ LIKE ? AND DATA_INATIVACAO IS NULL'
           )
    cursor.execute('SELECT DISTINCT CODIGO_PIZ,NOME_PIZ, VALOR_CUSTO FROM PIZZA '
                   'WHERE DATA_INATIVACAO IS NULL'
                   ' AND NOME_PIZ LIKE ?', ('%' + nomePizza + '%',))
    data = cursor.fetchone()

    #verificando qual a porcentagem usar

    if data is not None:
        valorPadrao = data[2]
        if Tam == 'grande':
            valorPadrao = valorPadrao * 1.35
        elif Tam == 'media':
            valorPadrao = valorPadrao * 1.25
        else:
            valorPadrao = valorPadrao * 1.15

    else:
        print('parametro inválido ou sem registro! - erro 00')
        return 1
    print(valorPadrao)

    #vefifica se é meia

    if meia != 1:



    return valorPadrao

#CalculaTamPizza('media', 'aleo', 1)
