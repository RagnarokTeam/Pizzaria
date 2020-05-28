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
from src.main import menuPrincipal
from src.lib.Fenrir import limparTelaOS
from src.lib.Fenrir import cabecalhoMenu

# variavel "cursor" pode ser alterada para qualquer outro nome de sua escolha
cursor = Bifrost.connection.cursor()


def pausa():
    programPause = input("\nPressione <ENTER> para voltar ao menu.")

def nova_pizza(): #solicita os dados, os coloca em uma lista e aloca no banco
    nome = (input("Nome da pizza:"))
    tipo = (input("Tipo:"))
    ing = (input("Ingredientes:"))
    valor = (input("Valor de Custo:"))

    novaPizza = [(GETDATE(), nome, tipo, ing, valor)]  #lista com os dados obtidos

    cursor.executemany("INSERT INTO pizza(DATA_CRIACAO, NOME_PIZ,TIPO_PIZ, INGREDIENTES, VALOR_CUSTO) \
                    values (?, ?, ?, ?, ?)", novaPizza)  # alocando no banco
  
    cursor.connection.commit()

    print('\nPizza', nome, 'cadastrada com sucesso!')
    pausa()



def inativ_pizza(): #coloca a data atual na data de inativação
    cod = (input("Digite o código da pizza que deseja desativar: "))

    cursor.execute("UPDATE pizza SET DATA_INATIVACAO = ? WHERE CODIGO_PIZ = ?", (GETDATE(), cod))

    cursor.connection.commit()

    print("\nPizza desativada com sucesso!")
    pausa()

def ativar_pizza(): #insere NULL na data de inativação
    cod = (input("Digite o código da pizza que deseja reativar: "))
    cursor.execute("UPDATE pizza SET DATA_INATIVACAO = NULL WHERE CODIGO_PIZ = ?", (cod))

    cursor.connection.commit()

    
    cabecalhoMenu()

    print("\nPizza reativada com sucesso!")
    pausa()


def apagar_pizza(): #funçao para apagar pizza do banco caso cadastrada errado

    cod = (input("Digite o código da pizza que deseja apagar: "))

    # excluindo a pizza pelo seu código
    cursor.execute("""DELETE FROM pizza WHERE CODIGO_PIZ = ?""", (cod,))
    
    cursor.connection.commit()
     
    print("Pizza apagada com sucesso!")
    pausa()

def listar_pizzas():#lista o código, tipo e nome das pizzas
    cursor.execute("SELECT CODIGO_PIZ, TIPO_PIZ, NOME_PIZ FROM pizza")
    print("Cód| Tipo  | Nome  ")
    for coluna in cursor.fetchall():
        print(coluna)

#menu gerenciador de pizzas
def menu_pizzas():
    limparTelaOS()
    opcao = 0
    op = 0
    print(" Gerenciado de Pizzas \n")
    print("[1] - Criar novo sabor")
    print("[2] - Inativar pizza")
    print("[3] - Ativar pizza")
    print("[4] - Listar pizzas")
    print("[5] - Menu Principal")

    opcao = eval(input("\nDigite a opção desejada: "))#lendo opção desejada

    if opcao == 1:
        limparTelaOS()#limpando a tela
        nova_pizza()#função referente a opção
        limparTelaOS()#limpando a tela
        menu_pizzas()#voltando ao menu principal
    elif opcao == 2:
        limparTelaOS()
        inativ_pizza()
        limparTelaOS()
        menu_pizzas()
    elif opcao == 3:
        limparTelaOS()
        ativar_pizza()
        limparTelaOS()
        menu_pizzas()
    elif opcao == 4:
        limparTelaOS()
        listar_pizzas()
        menu_pizzas()
    elif opcao == 5:
        limparTelaOS()
        menuPrincipal()
    else :
        limparTelaOS()
        print("Opção Invalida!")
        pausa()
        limparTelaOS()
        menu_pizzas()

menu_pizzas()

#fechando conexão
Bifrost.connection.close()
