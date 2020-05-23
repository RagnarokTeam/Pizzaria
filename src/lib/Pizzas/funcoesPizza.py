# """
# Data........: 2020-05-21
# Projeto.....: Pizzaria-Ragnarok
# Arquivo.....: funcoesPiz.py
# Descrição...: Funções para gerenciamento das pizzas - criar, ativar, inativar e deletar pizzas.
# Autor.......: Camila A. Oliveira - Eq. Ragnarok
# Observações.: 2020-05-21 - [R00] Criação do Arquivo - Versao 1.00
#
# Referencias:
# ""

from src.db.Asgard import Bifrost
from src.lib.Fenrir import GETDATE


# variavel "cursor" pode ser alterada para qualquer outro nome de sua escolha
cursor = Bifrost.connection.cursor()


def pausa():
    programPause = input("\nPressione <ENTER> para voltar ao menu.")

def nova_pizza(): #solicita os dados, os coloca em uma lista e aloca no banco
    nome = (input("Nome da pizza:"))
    ing = (input("Ingredientes: "))
    valor = (input("Valor de Custo:"))

    novaPizza = [(GETDATE(), nome, ing, valor)]  #lista com os dados obtidos

    cursor.executemany("INSERT INTO pizza(DATA_CRIACAO, NOME_PIZ, INGREDIENTES, VALOR_CUSTO) \
                    values (?, ?, ?, ?)", novaPizza)  # alocando no banco
    cursor.connection.commit()
    print('Pizza', nome, 'cadastrada com sucesso!')



def inativ_pizza(): #coloca a data atual na data de inativação
    cod = (input("Digite o código da pizza que deseja desativar: "))

    cursor.execute("UPDATE pizza SET DATA_INATIVACAO = ? WHERE CODIGO_PIZ = ?", (GETDATE(), cod))

    cursor.connection.commit()

    print("Pizza desativada com sucesso!")


def ativar_pizza(): #insere NULL na data de inativação
    cod = (input("Digite o código da pizza que deseja reativar: "))
    cursor.execute("UPDATE pizza SET DATA_INATIVACAO = NULL WHERE CODIGO_PIZ = ?", (cod))

    cursor.connection.commit()

    print("Pizza reativada com sucesso!")



def apagar_pizza(): #funçao para apagar pizza do banco caso cadastrada errado

    cod = (input("Digite o código da pizza que deseja apagar: "))

    # excluindo a pizza pelo seu código
    cursor.execute("""DELETE FROM pizza WHERE CODIGO_PIZ = ?""", (cod,))
    
    cursor.connection.commit()
     
    print("Pizza apagada com sucesso!")

#menu gerenciador de pizzas
def menu_pizzas():
    opcao = 0
    op = 0
    print("[1] - Criar novo sabor")
    print("[2] - Inativar pizza")
    print("[3] - Ativar pizza")
    print('[4] - Apagar cadastro')

    opcao = eval(input("Digite a opção desejada: "))

    if opcao == 1:
        nova_pizza()
        menu_pizzas()
    elif opcao == 2:
        inativ_pizza()
        menu_pizzas()
    elif opcao == 3:
        ativar_pizza()
        menu_pizzas()
    elif (opcao == 4):
        print("Essa opção excluirá permanentemente!")
        op = eval(input("Deseja continuar \n [1] - Sim \n [2] - Não"))

        if op == 1:
            apagar_pizza()

        else :
            menu_pizzas()
    else :
        print("Opção Invalida!")
        pausa()
        menu_pizzas()

#fechando conexão
Bifrost.connection.close()
