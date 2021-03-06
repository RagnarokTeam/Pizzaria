"""
Data........: 2020-05-14
Projeto.....: RagnarokProject - Pizzaria
Arquivo.....: Fenrir.py
Descrição...: Desacorrentamento generalizada para toda a aplicação utilizando função
Autor.......: Jefferson de L. Matos - Eq. Ragnarok
Observações.: 2020-05-22 - [R00] Criação do Arquivo - Versao 1.00
              Todas as Funções foram incorporadas ao Fenrir
Referencias: Imcorporando funções cliente criado pela Camila
"""
from datetime import datetime,timedelta
from src.db.Asgard import Bifrost
#from src.lib.Clientes import funcoesCliente
#from src.lib.Pizzas import funcoesPizza
import os

def cont ():
    prog = input("\nPressione <ENTER> para continuar.")
def pause():
    prog = input("\nPressione <ENTER> para voltar.")

def pausa():
    programPause = input("\nPressione <ENTER> para voltar ao menu.")

def GETDATE():
    data = datetime.now().strftime("%d/%m/%Y")

    return data

def GETTIME():
    data = datetime.now().strftime("%H:%M")
    return data

def GETTIMEADD():
    data = (datetime.now() + timedelta(minutes=50)).strftime("%H:%M")
    return data


def limparTelaOS():
    if os.system == 'nt':
        os.system('cls')
    else:
        os.system('cls')

def selectValorPadraoPizza(Tamanho,nomePizza):
    # inicialmente vou usar apenas por nome mas o correto é se usar o cod
    cursor = Bifrost.connection.cursor()
    cursor.execute('SELECT DISTINCT CODIGO_PIZ,NOME_PIZ, VALOR_CUSTO FROM PIZZA '
                   'WHERE DATA_INATIVACAO IS NULL'
                   ' AND NOME_PIZ LIKE ?', ('%' + nomePizza + '%',))

    data = cursor.fetchone()

    # verificando qual a porcentagem usar
    if data is not None:
        valorPadrao = int(data[2])
        if Tamanho == 'gg':
            valorPadrao = valorPadrao * 1.35
        elif Tamanho == 'g':
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
        print('[1] - Maior e Menor Receita')
        print('[2] - Detalhamentos clientes')
        print('[3] - Pizzas cadastradas')
        print('[4] - Quantidade de pedidos por cliente')
        print('[5] - Pedidos Entre Duas Datas')
        print('[6] - Voltar')
        opcaoRelat = eval(input('Digite qual relatório você quer abrir: '))

        if opcaoRelat == 1:
            cursor.execute(
                "SELECT A.COD_PED,A.DATA_PED,A.HORA_PED,MAX(A.TOTAL_PED),B.TAMANHO,C.NOME_PIZ FROM PEDIDO A INNER JOIN ITENS_PEDIDO B ON A.COD_PED = B.COD_PED INNER JOIN PIZZA C ON B.CODIGO_PIZ = C.CODIGO_PIZ GROUP BY TAMANHO")
            print('\nRELATÓRIO DE MAIOR RECEITA POR TAMANHO')
            all_rows = cursor.fetchall()
            for user1 in all_rows:
                print('------------------------------------------------------------')
                print('Codigo Pedido:', user1[0])  # Imprime o primeiro campo
                print('Data Pedido:', user1[1])  # Imprime o segundo campo
                print('Hora Pedido:', user1[2])  # Imprime o terceiro campo
                print('Valor de Venda:', user1[3])  # Imprime o terceiro campo
                print('Tamanho:', user1[4])  # Imprime o quarto campo
                print('Nome da Pizza:', user1[5])  # Imprime o quarto campo
            print('\n\n')

            cursor.execute(
                "SELECT A.COD_PED,A.DATA_PED,A.HORA_PED,min(A.TOTAL_PED),B.TAMANHO,C.NOME_PIZ FROM PEDIDO A INNER JOIN ITENS_PEDIDO B ON A.COD_PED = B.COD_PED INNER JOIN PIZZA C ON B.CODIGO_PIZ = C.CODIGO_PIZ GROUP BY TAMANHO")
            print('\n\n')
            print('\nRELATÓRIO DE MENOR RECEITA POR TAMANHO')
            all_rows = cursor.fetchall()
            for user1 in all_rows:
                print('------------------------------------------------------------')
                print('Codigo Pedido:', user1[0])  # Imprime o primeiro campo
                print('Data Pedido:', user1[1])  # Imprime o segundo campo
                print('Hora Pedido:', user1[2])  # Imprime o terceiro campo
                print('Valor de Venda:', user1[3])  # Imprime o terceiro campo
                print('Tamanho:', user1[4])  # Imprime o quarto campo
                print('Nome da Pizza:', user1[5])  # Imprime o quarto campo
            print('\n\n')
            pause()
            limparTelaOS()
        elif opcaoRelat == 2:
            datainicial = input("Digite a data inicial ex: dd/mm/yyyy")
            datafinal = input("Digite a data final ex: dd/mm/yyyy")
            cursor.execute(
                "select CODIGO_CLI,TEL_FIXO,TEL_CEL,NOME_CLI,ENDERECO,NR_END,COMPLEMENTO,BAIRRO,CIDADE,UF,DATA_CADASTRO, DATA_INATIVO from cliente where data_cadastro between ? and ?",(datainicial,datafinal))
            print('\nRELATÓRIO DE CLIENTES')
            all_rows = cursor.fetchall()
            for user1 in all_rows:
                print('------------------------------------------------------------')
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
            print('\n\n')
            pause()
            limparTelaOS()
        elif opcaoRelat == 3:
            cursor.execute(
                "select distinct codigo_piz, tipo_piz, data_criacao, data_inativacao, nome_piz, ingredientes, valor_custo, (valor_custo * 1.15) as pizza_media,(valor_custo * 1.25) as pizza_grande,(valor_custo * 1.35) as pizza_gigante from pizza")
            print('\nRelatorio Pizzas ')
            all_rows = cursor.fetchall()
            for user1 in all_rows:
                print('\n\n')
                print('------------------------------------------------------------')
                print('Cod: ', user1[0])
                print('Tipo: ', user1[1])
                print('Data criação: ', user1[2])
                print('Data Inativação: ', user1[3])
                print('Nome da pizza: ', user1[4])
                print('Ingredientes: ', user1[5])
                print('Valor custo: ', user1[6])
                print('Valor pizza média: %.2f' % user1[7])
                print('Valor pizza grande: %.2f'% user1[8])
                print('Valor pizza gigante: %.2f'% user1[9])

                print('\n\n')
            pause()
            limparTelaOS()
        elif opcaoRelat == 4:
            cursor.execute(
                "select distinct  A.CODIGO_CLI, NOME_CLI, sum(b.CODIGO_CLI) AS TOTAL, sum(TOTAL_PED) from cliente a inner join pedido b on a.CODIGO_CLI = b.CODIGO_CLI group by a.codigo_cli, nome_cli order by data_ped")

            all_rows = cursor.fetchall()
            print('RELATORIO DE CLIENTES QUE REALIZARAM PEDIDOS\n')
            for row in all_rows:
                print('CODIGO CLIENTE: {0}\n NOME CLIENTE: {1}\n QTD PEDIDOS: {2} \n VALOR GASTO: R$ {3}'.format(row[0],
                                                                                                             row[1],
                                                                                                             row[2],
                                                                                                             row[3]))
                print('\n\n')
            pause()
            limparTelaOS()
        elif opcaoRelat == 5: #Fizemos vários testes com as datas, ordem inversa, AAAA/MM/DD, MM/DD/AAAA e mesmo assim não funcionou
            datainicial = input("Digite a data inicial (formato DD-MM-AAAA)")
            datafinal = input("Digite a data final (formato DD-MM-AAAA)") 
            cursor.execute("select COD_PED, DATA_PED, CODIGO_CLI, TOTAL_PED from PEDIDO WHERE DATA_PED BETWEEN "+ datainicial + " AND "+ datafinal)
        
            print('\nRELATÓRIO DE PEDIDOS ENTRE', datainicial, 'E', datafinal)
            all_rows = cursor.fetchall()
            for user1 in all_rows:
                print('------------------------------------------------------------')
                print('Códog do Pedido:', user1[0])  # Imprime o primeiro campo
                print('Data:', user1[1])  # Imprime o segundo campo
                print('Códogo do Cliente:', user1[2])  # Imprime o terceiro campo22-03-2020
                print('Total do Pedido:', user1[3])  # Imprime o terceiro campo
                print('\n')
            cursor.connection.commit()    
            pause()
            limparTelaOS()
        else:
            menuPrincipal()

def cancelar_pedido ():
    ped = input("Digite o código do pedido que deseja cancelar")
    cursor.execute(
        "select distinct  COD_PED, NOME_CLI, data_ped, hora_ped,total_ped from cliente a inner join pedido b on a.CODIGO_CLI = b.CODIGO_CLI WHERE B.COD_PED = ? group by cod_ped, nome_cli order by data_ped",(ped))

    row = cursor.fetchone()
    if row is not None:
        print('\n------------------------------------------------------------\n\n')
        print('ID PEDIDO: {0}\n NOME CLIENTE: {1}\n DATA PEDIDO: {2} \n HORA DO PEDIDO: {3}\n TOTAL DO PEDIDO: {4}'.format(row[0],row[1],row[2],row[3],row[4]))
        print('\n')
        op = 0
        op = eval(input('\nTem certeza que deseja cancelar o pedido acima?\n [1] - Sim\n [2] - Não\n'))
        if op == 1:
            limparTelaOS()

            cursor.execute("DELETE FROM pedido WHERE COD_PED = ?", (ped))

            cursor.connection.commit()
            cursor.execute("DELETE FROM ITENS_pedido WHERE COD_PED = ?", (ped))

            cursor.connection.commit()

            print("Pedido cancelado com sucesso!")
            cont()
        elif op == 2:
            print('Cancelando operação... \n Retornando ao menu principal')
            cont()
            menuPrincipal()
    else:
        op = 0
        op = eval(input('Pedido não encontrado\n Deseja realizar a operação novamente?\n [1] - Sim\n [2] - Não\n'))
        if op == 1:
            limparTelaOS()
            cancelar_pedido()
        elif op == 2:
            print('Cancelando operação... \n Retornando ao menu principal')
            cont()
            menuPrincipal()
def menuPrincipal():
    opcao = 0
    while opcao != 9:
        cabecalhoMenu()
        print('MENU PRINCIPAL')
        print('[1] - Iniciar Pedido')
        print('[2] - Cancelar Pedido')
        print('[3] - Cliente Novo')
        print('[4] - Relatorios')
        print('[5] - Gerenciar Clientes')
        print('[6] - Gerenciar Pizzas')
        print('[7] - Gerar Banco de Dados Padrão')
        print('[9] - Sair')
        opcao = eval(input('Digite a opção desejada: '))
        print('Opcao escolhido foi: ', opcao)

        if opcao == 1:
            limparTelaOS()
            geraPedido()
            limparTelaOS()
            menuPrincipal()
        elif opcao == 2:
            limparTelaOS()
            cancelar_pedido()
            limparTelaOS()
            menuPrincipal()
        elif opcao == 3:
            limparTelaOS()
            novo_cliente()
            limparTelaOS()
        elif opcao == 4:
            limparTelaOS()
            todosRelatorios()
            limparTelaOS()
        elif opcao == 5:
            limparTelaOS()
            menu_cliente()
            limparTelaOS()
        elif opcao == 6:
            limparTelaOS()
            menu_pizzas()
            limparTelaOS()
        elif opcao == 7:
            limparTelaOS()
            gerarDataBasePadrão()
            menuPrincipal()
            limparTelaOS()
        else:
            print('Opcao invalida!\n')
            pausa()
            limparTelaOS()

# variavel "cursor" pode ser alterada para qualquer outro nome de sua escolha
cursor = Bifrost.connection.cursor()


def pause():
    prog = input("\nPressione <ENTER> para voltar.")


def pausa():
    programPause = input("\nPressione <ENTER> para voltar ao menu.")


def listar_clientes():  # lista o código e nome dos clientes
    cursor.execute("SELECT CODIGO_CLI, NOME_CLI FROM cliente WHERE DATA_INATIVO IS NULL")
    print("Cód  |  Nome  ")
    for row in cursor.fetchall():
        print('{0}, {1}'.format(row[0], row[1]))
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

    novoCliente = [(telf, telc, nome, end, num, comp, bai, cid, uf, GETDATE())]  # lista com os dados obtidos

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
    cursor.execute("UPDATE cliente SET DATA_INATIVO = ? WHERE CODIGO_CLI = ?", (GETDATE(), codi))

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

def at_tipo(codpiz):
    new = 0
    print("Qual será o novo tipo da pizza?")
    new = eval(input("[1] - Salgada\n[2] - Doce\n"))
    novo = " "
    if new == 1:
        novo = "Salgada"
    elif new == 2:
        novo = "Doce"
    else:
        print("Opção inválida !")
        pausa()
        at_tipo

    cursor.execute("UPDATE pizza SET TIPO_PIZ = ? WHERE CODIGO_PIZ = ?", (novo, codpiz))

    cursor.connection.commit()

    print("\nTipo atualizado com sucesso!")
    pausa()

def at_nome(codpiz):
    new = input("Digite o novo nome:")
    
    cursor.execute("UPDATE pizza SET NOME_PIZ = ? WHERE CODIGO_PIZ = ?", (new, codpiz))

    cursor.connection.commit()

    print("\nNome atualizado com sucesso!")
    pausa()

def at_ing(codpiz):
    new = input("Digite os novos ingredientes:")

    cursor.execute("UPDATE pizza SET INGREDIENTES = ? WHERE CODIGO_PIZ = ?", (new, codpiz))

    cursor.connection.commit()

    print("\nIngredientes atualizados com sucesso!")
    pausa()

def at_valor(codpiz):  
    new = input("Digite o novo valor de custo:")

    cursor.execute("UPDATE pizza SET VALOR_CUSTO = ? WHERE CODIGO_PIZ = ?", (new, codpiz))

    cursor.connection.commit()

    print("\nIngredientes atualizados com sucesso!")
    pausa()
    

def atualizar_pizza():
    opc = 0
    limparTelaOS()
    cod = input("Digite o código da pizza: ")  # pegando o cod para passar para funções de atualização
    
    def atualizar_piz():
        limparTelaOS()
        print("[1] - Tipo de Pizza")  # imprimindo opções de atualização
        print("[2] - Nome")
        print("[3] - Ingredientes")
        print("[4] - Valor de Custo")
        print("[5] - Trocar pizza")
        print("[6] - Voltar ao gerenciador de pizzas")

        opc = eval(input("\nDigite a opçao desejada: "))

        if opc == 1:
            limparTelaOS()
            at_tipo(cod)
            limparTelaOS()
            atualizar_piz()
        elif opc == 2:
            limparTelaOS()
            at_nome(cod)
            limparTelaOS()
            atualizar_piz()
        elif opc == 3:
            limparTelaOS()
            at_ing(cod)
            limparTelaOS()
            atualizar_piz()
        elif opc == 4:
            limparTelaOS()
            at_valor(cod)
            limparTelaOS()
            atualizar_piz()
        elif opc == 5:
            limparTelaOS()
            atualizar_pizza()
        elif opc == 6:
            limparTelaOS()
            menu_pizzas()
    atualizar_piz()

def apagar_pizza():  # funçao para apagar pizza do banco caso cadastrada errada

    cod = (input("Digite o código da pizza que deseja apagar: "))

    # excluindo a pizza pelo seu código
    cursor.execute("""DELETE FROM pizza WHERE CODIGO_PIZ = ?""", (cod,))

    cursor.connection.commit()

    print("Pizza apagada com sucesso!")
    pausa()


def listar_pizzas():  # lista o código, tipo e nome das pizzas
    cursor.execute("SELECT CODIGO_PIZ, TIPO_PIZ, NOME_PIZ FROM PIZZA WHERE DATA_INATIVACAO IS NULL")
    print("Cód| Tipo  | Nome  ")
    for row in cursor.fetchall():
        print('{0}, {1}, {2}'.format(row[0], row[1], row[2]))
    cont()


# menu gerenciador de pizzas
def menu_pizzas():
    limparTelaOS()
    opcao = 0
    op = 0
    print(" Gerenciado de Pizzas \n")
    print("[1] - Criar novo sabor")
    print("[2] - Inativar pizza")
    print("[3] - Ativar pizza")
    print("[4] - Atualizar Pizza")
    print("[5] - Listar pizzas")
    print("[6] - Menu Principal")

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
        atualizar_pizza()
        limparTelaOS()
    elif opcao == 5:
        limparTelaOS()
        listar_pizzas()
        menu_pizzas()
    elif opcao == 6:
        limparTelaOS()
        menuPrincipal()
    else:
        limparTelaOS()
        print("Opção Invalida!")
        pausa()
        limparTelaOS()
        menu_pizzas()

def geraPedido():
    tel = input('Digite o numero de telefone do cliente: ')
    cursor.execute("SELECT DISTINCT * FROM CLIENTE WHERE TEL_FIXO = ? OR TEL_CEL = ?",(tel,tel,))
    dados = cursor.fetchone()
    if dados is not None:
        print('Cliente: ',dados[3])
        print('Rua:', dados[4],'-',dados[5])
        op = eval (input('Os dados estão certos? Deseja continuar?\n [1] - Sim\n [2] - Não\n'))
        if op == 1:
            limparTelaOS()
            print("Lista das Pizzas")
            listar_pizzas()
            limparTelaOS()
            codPizza = int(input('Qual o codigo da pizza solicitada?\n '))
            tamanho = input('Qual o tamanho desejado? (gg, g, m)\n')
            limparTelaOS()
            pizza = selectPizza(codPizza)
            opMet = eval (input('Deseja um segundo sabor?\n [1] - Sim\n [2] - Não\n'))
            if opMet == 1:
                limparTelaOS()
                print("Lista das Pizzas")
                listar_pizzas()
                limparTelaOS()
                codPizza2 = int(input('Qual o codigo da pizza solicitada?\n '))
                pizza2 = selectPizza(codPizza2)
                valorPedido = CalculaValorFinalPizza(tamanho,pizza,1,pizza2)
                ultimoid = ultimoIdPedido()
                cursor.execute("insert into pedido values(?,?,?,?,?)",(ultimoid,GETDATE(),GETTIME(),dados[0],valorPedido))
                cursor.connection.commit()
                cursor.execute("insert into itens_pedido values(?,?,?,?)",(ultimoid,1,codPizza,tamanho))
                cursor.connection.commit()
                cursor.execute("insert into itens_pedido values(?,?,?,?)",(ultimoid, 2, codPizza2, tamanho))
                cursor.connection.commit()
                print('Pedido realidado com sucesso!')
                print('No valor de: %.2f' % valorPedido)
                print('Sabores: ',pizza,', ',pizza2)
                print('Seu pedido está previsto para ser feito até às ',GETTIMEADD())

                pause()
            elif opMet == 2:
                valorPedido = CalculaValorFinalPizza(tamanho, pizza)
                ultimoid = ultimoIdPedido()
                cursor.execute("insert into pedido values(?,?,?,?,?)",
                               (ultimoid, GETDATE(), GETTIME(), dados[0], valorPedido))
                cursor.connection.commit()
                print('Pedido realidado com sucesso!')
                print('No valor de: %.2f' % valorPedido)
                print('Sabor: ', pizza)
                print('Seu pedido está previsto para ser feito até às ', GETTIMEADD())

                pause()
        else:
            limparTelaOS()
            geraPedido()
    else:
        def erro():
            c = 0
            limparTelaOS()
            print('Não foi encontrado cliente com esse telefone!')
            c = eval(input("[1] - Tentar novamente\n[2] - Novo cadastro\n"))
            if c == 1:
                geraPedido()
            elif c == 2:
                print('Redirecionando para cadastro')
                cont()
                limparTelaOS()
                novo_cliente()
            else:
                print("Opção invalida!")
                pause()
                erro()
        erro()

def selectPizza(id):
    cursor.execute("SELECT DISTINCT NOME_PIZ FROM PIZZA WHERE CODIGO_PIZ = ?", (id,))
    PIZZA = cursor.fetchone()
    print('Pizza Selecionada: ',PIZZA[0])
    conf = 0
    conf= eval (input('O sabor da pizza está correto?\n [1] - Sim\n [2] - Não\n'))
    if conf == 1:
        return PIZZA[0]
    else:
        listar_pizzas()
        id = int(input('\n\n\nQual o codigo da pizza solicitada? '))
        selectPizza(id)

def ultimoIdPedido():
    cursor.execute("SELECT DISTINCT  MAX(COD_PED) + 1 FROM PEDIDO ")
    id = cursor.fetchone()
    return  id[0]

def gerarDataBasePadrão():
    itens_pedido()
    tab_pedido()
    tab_pizza()
    tab_cliente()
    print('\nTabelas criadas com sucesso!')
    lista_clientes = [('1', '1', 'Paula', 'Rua Anfibólios', '562', 'NULL', 'Bonfim', 'Belo Horizonte', 'MG'),
                      ('2', '2', 'Camila', 'Parque Anhangabaú', '82', 'NULL', 'Centro', 'São Paulo', 'SP'),
                      ('3', '3', 'Jefferson', 'Rua Condado', '585', 'Ap 76 BL 5', 'Cavalhada', 'Porto Alegre', 'RS'),
                      ('4', '4', 'Jonathan', 'Rua Álvaro Anes', '90', 'NULL', 'Pinheiros', 'São Paulo', 'SP')]

    cursor.executemany("INSERT INTO cliente( TEL_FIXO, TEL_CEL, NOME_CLI, ENDERECO, NR_END,COMPLEMENTO,BAIRRO,CIDADE,UF) \
                        values (?,?,?,?,?,?,?,?,?)", lista_clientes)

    cursor.connection.commit()
    print('\nClientes inseridos com sucesso!')
    lista_pizza = [('Salgada', GETDATE(), 'ALHO E OLEO', 'Alho frito picado, parmesão ralado e azeitonas', 22.90),
                   ('Salgada', GETDATE(), 'ALLICI',
                    'Alicci importado, rodelas de tomate, parmesão e azeitonas', 28.90),
                   ('Salgada', GETDATE(), 'ATUM', 'Atum, cebola e azeitona', 22.90),
                   ('Salgada', GETDATE(), 'BACON',
                    'Bacon coberto com muzzarela e azeitonas', 26.90),
                   ('Salgada', GETDATE(), 'BERINGELA',
                    'Beringela, cobertura com muzzarela, manjericão e parmesão', 23.90),
                   ('Salgada', GETDATE(), 'CAIPIRA',
                    'Frango desfiado, coberto com catupiry e milho verde e azeitonas', 26.90),
                   ('Salgada', GETDATE(), 'CALABRESA',
                    'Linguiça cababresa, cebola e azeitonas', 19.90),
                   ('Salgada', GETDATE(), 'CINCO QUEIJOS',
                    'Muzzarela, parmesão, catupiry, gorgonzola e provolone', 29.90),
                   ('Salgada', GETDATE(), 'ESCAROLA',
                    'Escarola refogada, muzzarela, e azeitonas', 24.90),
                   ('Salgada', GETDATE(), 'EXECUTIVA',
                    'Milho Verde, catupiry e azeitonas', 22.90),
                   ('Salgada', GETDATE(), 'PERUANA',
                    'Atum, cebola, muzarela e azeitonas', 26.90),
                   ('Salgada', GETDATE(), 'PALMITO',
                    'Palmito com muzarela e azeitonas', 26.90),
                   ('Doce', GETDATE(), 'BANANA',
                    'Banana fatiada com, cobertura com leite condensado e canela em pó', 21.90),
                   ('Doce', GETDATE(), 'BRIGADEIRO',
                    'Chocolate, leite condensado e chocolate granlado', 23.90),
                   ('Doce', GETDATE(), 'PRESTIGIO', 'Chocolate coberta com côco', 23.90)]

    cursor.executemany("INSERT INTO pizza( TIPO_PIZ,DATA_CRIACAO, NOME_PIZ, INGREDIENTES, VALOR_CUSTO) \
                        values (?, ?, ?, ?, ?)", lista_pizza)

    cursor.connection.commit()
    print('\nPizzas inseridos com sucesso!')
    cont()

def tab_cliente():
    cursor.execute('CREATE TABLE IF NOT EXISTS cliente \
                   (CODIGO_CLI  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, TEL_FIXO string(15), \
                   TEL_CEL string(15), NOME_CLI string(40), ENDERECO string(30), NR_END string(10), \
                    COMPLEMENTO string(25), BAIRRO string(20), CIDADE string(20), UF string(02),DATA_CADASTRO date, DATA_INATIVO date)'
                   )

def tab_pizza():
    cursor.execute('CREATE TABLE IF NOT EXISTS pizza \
                    (CODIGO_PIZ    INTEGER  NOT NULL    PRIMARY KEY AUTOINCREMENT,\
                     TIPO_PIZ string(8), DATA_CRIACAO date,\
                     DATA_INATIVACAO date, NOME_PIZ string(100), '
                   'INGREDIENTES text, VALOR_CUSTO numeric(10, 2))'
                   )

def tab_pedido():
    cursor.execute('CREATE TABLE IF NOT EXISTS PEDIDO (COD_PED	INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT,DATA_PED		DATE,\
	HORA_PED		TIME,\
	CODIGO_CLI		INTEGER,\
	TOTAL_PED		NUMERIC(10,2),\
	CONSTRAINT FK_PEDIDO_CODIGOCLI FOREIGN KEY(CODIGO_CLI) REFERENCES CLIENTE(CODIGO_CLI)\
    );')


def itens_pedido():
    cursor.execute('CREATE TABLE IF NOT EXISTS ITENS_PEDIDO (\
	COD_PED			INTEGER NOT NULL,\
	ITEM			INTEGER NOT NULL,\
	CODIGO_PIZ		INTEGER,\
	TAMANHO			STRING (10),\
	CONSTRAINT PK_ITENSPEDIDO PRIMARY KEY(COD_PED, ITEM),\
	CONSTRAINT FK_ITENSPEDIDO_CODIGOPIZ FOREIGN KEY(CODIGO_PIZ) REFERENCES PIZZA(CODIGO_PIZ));')


def relat_cliente():

    datainicial = eval(input("Digite a data inicial"))
    datafinal = eval(input("Digite a data final"))
    cursor.execute("select codigo_cli, nome_cli,data from cliente where data_cadastro between " + datainicial + " and " + datafinal)

    print('\nRELATÓRIO DE CLIENTES ENTRE', datainicial, 'E', datafinal)
    all_rows = cursor.fetchall()
    for user1 in all_rows:
        print('------------------------------------------------------------')
        print('Código do cliente:', user1[0])  # Imprime o primeiro campo
        print('Nome do cliente:', user1[1])  # Imprime o segundo campo
        print('Data Cadastrado:', user1[2])  # Imprime o segundo campo
        print('Data Inativado:', user1[3])  # Imprime o segundo campo
        print('\n')
    cursor.connection.commit()
    pause()
    limparTelaOS()



