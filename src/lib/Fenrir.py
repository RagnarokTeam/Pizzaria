"""
Data........: 2020-05-14
Projeto.....: RagnarokProject - Pizzaria
Arquivo.....: Fenrir.py
Descrição...: Desacorrentamento generalizada para toda a aplicação utilizando função
Autor.......: Jefferson de L. Matos - Eq. Ragnarok
Observações.: 2020-05-22 - [R00] Criação do Arquivo - Versao 1.00
              ...
Referencias: imcorporando funções cliente criado pela camila
"""
from datetime import datetime
from src.db.Asgard import Bifrost
#from src.lib.Clientes import funcoesCliente
#from src.lib.Pizzas import funcoesPizza
import os

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


def limparTelaOS():
    os.system('cls')

def cabecalhoMenu():
    limparTelaOS()
    print('  _________________')
    print(' |  MASTER-PIZZAS  | ')
    print(' |_________________|')
    print(' \                / ')
    print('  \              / ')
    print('   \            / ')
    print('    \          / ')
    print('     \        /')
    print('      \      / ')
    print('       \    / ')
    print('        \  / ')
    print('         \/')

    print('\n')


def cadastroCliente():
    limparTelaOS()
    input('Telefone Fixo: ')
    input('Telefone Celular: ')
    input('Nome Completo: ')
    input('Endereço: ')
    input('Número: ')
    input('Complemento (Se Tiver): ')
    input('Bairro: ')
    input('Cidade: ')
    input('UF: ')
    input('CEP: ')


def todosRelatorios():
    limparTelaOS()
    opcaoRelat = 0


    while opcaoRelat != 5:
        print('[1] - Dados do Clientes')
        print('[2] - Detalhamentos cliente')
        print('[3] - Pizzas')
        print('[4] - Pedidos')
        print('[6] - Voltar')
        opcaoRelat = eval(input('Digite qual relatório você quer abrir: '))

        if opcaoRelat == 1:
            input('que')
        elif opcaoRelat == 2:
            input('oi')
        elif opcaoRelat == 3:
            input('hello')
        elif opcaoRelat == 4:
            input('hehe')
        else:
            menuPrincipal()


def menuPrincipal():
    opcao = 0
    while opcao != 9:
        cabecalhoMenu()
        print('MENU PRINCIPAL')
        print('[1] - Cliente Cadastrado')
        print('[2] - Cliente Novo')
        print('[3] - Relatorios')
        print('[4] - Gerenciar Clientes')
        print('[5] - Gerenciar Pizzas')
        print('[9] - Sair')
        opcao = eval(input('Digite a opção desejada: '))
        print('Opcao escolhido foi: ', opcao)

        if opcao == 1:
            input('Digite o numero de telefone do cliente: ')
        #    menuCriaBasePadrao()
        elif opcao == 2:
            cadastroCliente()
        elif opcao == 3:
            todosRelatorios()
        elif opcao == 4:
            limparTelaOS()
            menu_cliente()
            limparTelaOS()
        elif opcao == 5:
            limparTelaOS()
            funcoesPizza.menu_pizzas()
            limparTelaOS()
        else:
            print('Opcao invalida!')

# variavel "cursor" pode ser alterada para qualquer outro nome de sua escolha
cursor = Bifrost.connection.cursor()


def pause():
    prog = input("\nPressione <ENTER> para voltar.")


def pausa():
    programPause = input("\nPressione <ENTER> para voltar ao menu.")


def listar_clientes():  # lista o código e nome dos clientes
    cursor.execute("SELECT CODIGO_CLI, NOME_CLI FROM cliente WHERE DATA_INATIVO IS NULL")
    print("Cód  |  Nome  ")
    for coluna in cursor.fetchall():
        print(coluna)

    cursor.connection.commit()
    pause()


def consulta_cliente(codcliente):  # consulta determinado cliente pelo seu código
    cursor.execute(
        "SELECT CODIGO_CLI, NOME_CLI, TEL_FIXO, TEL_CEL, ENDERECO, NR_END, COMPLEMENTO, BAIRRO, CIDADE, UF, DATA_CADASTRO, DATA_INATIVO FROM cliente WHERE CODIGO_CLI = ?",
        (codcliente,))
    colum = cursor.fetchone()
    print("Codigo Cliente:", colum[0])
    print("Nome:", colum[1])
    print("Telefone Fixo", colum[2])
    print("Telefone Celular:", colum[3])
    print("Endereço:", colum[4])
    print("Número:", colum[5])
    print("Complemento:", colum[6])
    print("Bairro:", colum[7])
    print("Cidade:", colum[8])
    print("UF:", colum[9])
    print("Data de Cadastro:", colum[10])
    print("Data de Inativação:", colum[11])
    pause()


def novo_cliente():  # função para cadastrar um novo cliente
    nome = (input("Nome: "))
    telf = (input("Telefone Fixo: "))
    telc = (input("Telefone Celular: "))
    end = (input("Endereço: "))
    num = (input("Número: "))
    comp = (input("Complemento: (opcional)"))
    bai = (input("Bairro: "))
    cid = (input("Cidade: "))
    uf = (input("UF: "))

    novoCliente = [(telf, telc, nome, end, num, comp, bai, cid, uf, lETDATE())]  # lista com os dados obtidos

    cursor.executemany("INSERT INTO cliente(TEL_FIXO, TEL_CEL, NOME_CLI, ENDERECO, NR_END, COMPLEMENTO, \
                        BAIRRO, CIDADE, UF, DATA_CADASTRO) \
                    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", novoCliente)  # alocando no banco

    cursor.connection.commit()
    print('\nCliente cadastrado com sucesso!')
    pausa()


def atualizar_cliente():  # função para atualizar algum dado do cliente
    opc = 0
    cod = input("Digite o código do cliente: ")  # pegando o cod para passar para funções de atualização

    def atualizar_cliente():

        print("[1] - Nome")  # imprimindo opções de atualização
        print("[2] - Telefone Fixo")
        print("[3] - Telefone Celular")
        print("[4] - Endereço")
        print("[5] - Número")
        print("[6] - Complemento")
        print("[7] - Bairro")
        print("[8] - Cidade")
        print("[9] - UF")
        print("[0] - Voltar ao gerenciador de clientes")

        opc = eval(input("\nDigite a opçao desejada: "))  # leitra da opção
        if opc == 1:
            limparTelaOS()
            at_nome(cod)
            limparTelaOS()
            atualizar_cliente()
        elif opc == 2:
            limparTelaOS()
            at_telf(cod)
            limparTelaOS()
            atualizar_cliente()
        elif opc == 3:
            limparTelaOS()
            at_telc(cod)
            limparTelaOS()
            atualizar_cliente()
        elif opc == 4:
            limparTelaOS()
            at_end(cod)
            limparTelaOS()
            atualizar_cliente()
        elif opc == 5:
            limparTelaOS()
            at_num(cod)
            limparTelaOS()
            atualizar_cliente()
        elif opc == 6:
            limparTelaOS()
            at_comp(cod)
            limparTelaOS()
            atualizar_cliente()
        elif opc == 7:
            limparTelaOS()
            at_bairro(cod)
            limparTelaOS()
            atualizar_cliente()
        elif opc == 8:
            limparTelaOS()
            at_cid(cod)
            limparTelaOS()
            atualizar_cliente()
        elif opc == 9:
            limparTelaOS()
            at_uf(cod)
            limparTelaOS()
            atualizar_cliente()
        elif opc == 0:
            limparTelaOS()
            menu_cliente()
        else:
            limparTelaOS()
            print("\nOpção Inválida!")
            pausa()

            atualizar_cliente()

    atualizar_cliente()


def at_nome(codcliente):  # atualização do nome
    new = input("Digite o novo nome: ")
    cursor.execute("UPDATE cliente SET NOME_CLI = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nNome atualizado com sucesso!")
    pausa()


def at_telf(codcliente):  # atualização do telefone fixo
    new = input("Digite o novo Telefone Fixo: ")
    cursor.execute("UPDATE cliente SET TEL_FIXO = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nTelefone Fixo atualizado com sucesso!")
    pausa()


def at_telc(codcliente):  # atualização do telefone celular
    new = input("Digite o novo Telefone Celular: ")
    cursor.execute("UPDATE cliente SET TEL_CEL = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nTelefone Celular atualizado com sucesso!")
    pausa()


def at_end(codcliente):  # atualização do endereço
    new = input("Digite o novo Endereço: ")
    cursor.execute("UPDATE cliente SET ENDERECO = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nEndereço atualizado com sucesso!")
    pausa()


def at_num(codcliente):  # atualização do número do endereço
    new = input("Digite o novo Número: ")
    cursor.execute("UPDATE cliente SET NR_END = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nNúmero atualizado com sucesso!")
    pausa()


def at_comp(codcliente):  # atualização do complemento
    new = input("Digite o novo Comlemento: ")
    cursor.execute("UPDATE cliente SET COMPLEMENTO = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nComplemento atualizado com sucesso!")
    pausa()


def at_bairro(codcliente):  # atualização do bairro
    new = input("Digite o novo Bairro: ")
    cursor.execute("UPDATE cliente SET BAIRRO = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nBairro atualizado com sucesso!")
    pausa()


def at_cid(codcliente):  # atualização da cidade
    new = input("Digite a nova Cidade: ")
    cursor.execute("UPDATE cliente SET CIDADE = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nCidade atualizada com sucesso!")
    pausa()


def at_uf(codcliente):  # atualização do estado (UF)
    new = input("Digite o novo Estado (UF): ")
    cursor.execute("UPDATE cliente SET UF = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nEstado atualizado com sucesso!")
    pausa()


def ativar_cliente():  # ativação de cliente
    codi = (input("Digite o código do cliente que deseja reativar: "))
    cursor.execute("UPDATE cliente SET DATA_INATIVO = NULL WHERE CODIGO_CLI = ?", (codi))

    cursor.connection.commit()

    print("Cliente reativado com sucesso!")
    pausa()


def desativar_cliente():  # desativando cliente
    codi = (input("Digite o código do cliente que deseja desativar: "))
    cursor.execute("UPDATE cliente SET DATA_INATIVO = ? WHERE CODIGO_CLI = ?", (lETDATE(), codi))

    cursor.connection.commit()

    print("Cliente desativado com sucesso!")
    pausa()


def menu_cliente():  # menu que gerencia as funções com clientes
    limparTelaOS()
    o = 0
    print(" Gerenciador de Clientes\n ")
    print("[1] - Listar Clientes")
    print("[2] - Consultar um Cliente")
    print("[3] - Novo Cliente")
    print("[4] - Atualizar Cliente")
    print("[5] - Ativar Cliente")
    print("[6] - Desativar Cliente")
    print("[7] - Menu Principal")

    o = eval(input("\nDigite a opção desejada: "))  # lendo a opção desejada

    if o == 1:
        limparTelaOS()  # limpando a tela
        listar_clientes()  # função da opção desejada
        limparTelaOS()  # limpando a tela
        menu_cliente()  # voltando ao menu de cliente
    elif o == 2:
        limparTelaOS()
        cod = input("Digite o codigo do Cliente:")
        limparTelaOS()
        consulta_cliente(cod)
        limparTelaOS()
        menu_cliente()
    elif o == 3:
        limparTelaOS()
        novo_cliente()
        limparTelaOS()
        menu_cliente()
    elif o == 4:
        limparTelaOS()
        atualizar_cliente()
        limparTelaOS()
        menu_cliente()
    elif o == 5:
        limparTelaOS()
        ativar_cliente()
        limparTelaOS()
        menu_cliente()
    elif o == 6:
        limparTelaOS()
        desativar_cliente()
        limparTelaOS()
        menu_cliente()
    elif o == 7:
        limparTelaOS()
        menuPrincipal()
    else:
        limparTelaOS()
        print("Opção Invalida!")
        pausa()
        limparTelaOS()
        menu_cliente()


def pausa():
    programPause = input("\nPressione <ENTER> para voltar ao menu.")


def nova_pizza():  # solicita os dados, os coloca em uma lista e aloca no banco
    nome = (input("Nome da pizza:"))
    tipo = (input("Tipo:"))
    ing = (input("Ingredientes:"))
    valor = (input("Valor de Custo:"))

    novaPizza = [(GETDATE(), nome, tipo, ing, valor)]  # lista com os dados obtidos

    cursor.executemany("INSERT INTO pizza(DATA_CRIACAO, NOME_PIZ,TIPO_PIZ, INGREDIENTES, VALOR_CUSTO) \
                    values (?, ?, ?, ?, ?)", novaPizza)  # alocando no banco

    cursor.connection.commit()

    print('\nPizza', nome, 'cadastrada com sucesso!')
    pausa()


def inativ_pizza():  # coloca a data atual na data de inativação
    cod = (input("Digite o código da pizza que deseja desativar: "))

    cursor.execute("UPDATE pizza SET DATA_INATIVACAO = ? WHERE CODIGO_PIZ = ?", (GETDATE(), cod))

    cursor.connection.commit()

    print("\nPizza desativada com sucesso!")
    pausa()


def ativar_pizza():  # insere NULL na data de inativação
    cod = (input("Digite o código da pizza que deseja reativar: "))
    cursor.execute("UPDATE pizza SET DATA_INATIVACAO = NULL WHERE CODIGO_PIZ = ?", (cod))

    cursor.connection.commit()

    cabecalhoMenu()

    print("\nPizza reativada com sucesso!")
    pausa()


def apagar_pizza():  # funçao para apagar pizza do banco caso cadastrada errado

    cod = (input("Digite o código da pizza que deseja apagar: "))

    # excluindo a pizza pelo seu código
    cursor.execute("""DELETE FROM pizza WHERE CODIGO_PIZ = ?""", (cod,))

    cursor.connection.commit()

    print("Pizza apagada com sucesso!")
    pausa()


def listar_pizzas():  # lista o código, tipo e nome das pizzas
    cursor.execute("SELECT CODIGO_PIZ, TIPO_PIZ, NOME_PIZ FROM pizza")
    print("Cód| Tipo  | Nome  ")
    for coluna in cursor.fetchall():
        print(coluna)


# menu gerenciador de pizzas
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

    opcao = eval(input("\nDigite a opção desejada: "))  # lendo opção desejada

    if opcao == 1:
        limparTelaOS()  # limpando a tela
        nova_pizza()  # função referente a opção
        limparTelaOS()  # limpando a tela
        menu_pizzas()  # voltando ao menu principal
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
    else:
        limparTelaOS()
        print("Opção Invalida!")
        pausa()
        limparTelaOS()
        menu_pizzas()
