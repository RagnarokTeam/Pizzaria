# """
# Data........: 2020-05-24
# Projeto.....: Pizzaria-Ragnarok
# Arquivo.....: funcoesClientes.py
# Descrição...: funções para gerenciamento dos clientes
# Autor.......: Camila A. Oliveira - Eq. Ragnarok
# Observações.: 2020-05-08 - [R00] Criação do Arquivo - Versao 1.00
#
# Referencias:
# ""
from src.db.Asgard import Bifrost
#from src.lib import Fenrir


# variavel "cursor" pode ser alterada para qualquer outro nome de sua escolha
cursor = Bifrost.connection.cursor()

def pause():
    prog = input("\nPressione <ENTER> para voltar.")

def pausa():
    programPause = input("\nPressione <ENTER> para voltar ao menu.")

def listar_clientes():#lista o código e nome dos clientes
    cursor.execute("SELECT CODIGO_CLI, NOME_CLI FROM cliente WHERE DATA_INATIVO IS NULL")
    print("Cód  |  Nome  ")
    for coluna in cursor.fetchall():
        print(coluna)

    cursor.connection.commit()   
    pause()

def consulta_cliente(codcliente): #consulta determinado cliente pelo seu código
    cursor.execute("SELECT CODIGO_CLI, NOME_CLI, TEL_FIXO, TEL_CEL, ENDERECO, NR_END, COMPLEMENTO, BAIRRO, CIDADE, UF, DATA_CADASTRO, DATA_INATIVO FROM cliente WHERE CODIGO_CLI = ?",(codcliente,))
    colum = cursor.fetchone()
    print("Codigo Cliente:",colum[0])
    print("Nome:", colum [1])
    print("Telefone Fixo", colum [2])
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

def novo_cliente (): #função para cadastrar um novo cliente
    nome = (input("Nome: "))
    telf = (input("Telefone Fixo: "))
    telc = (input("Telefone Celular: "))
    end = (input("Endereço: "))
    num = (input("Número: "))
    comp = (input("Complemento: (opcional)"))
    bai = (input("Bairro: "))
    cid = (input("Cidade: "))
    uf = (input("UF: "))

    novoCliente = [(telf, telc, nome, end, num, comp, bai, cid, uf, lETDATE())] #lista com os dados obtidos
       
    cursor.executemany("INSERT INTO cliente(TEL_FIXO, TEL_CEL, NOME_CLI, ENDERECO, NR_END, COMPLEMENTO, \
                        BAIRRO, CIDADE, UF, DATA_CADASTRO) \
                    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", novoCliente) #alocando no banco

    cursor.connection.commit()
    print('\nCliente cadastrado com sucesso!')
    pausa()



def atualizar_cliente (): #função para atualizar algum dado do cliente
    opc = 0
    cod = input("Digite o código do cliente: ")#pegando o cod para passar para funções de atualização
    def atualizar_cliente():

        print("[1] - Nome")#imprimindo opções de atualização
        print("[2] - Telefone Fixo")
        print("[3] - Telefone Celular")
        print("[4] - Endereço")
        print("[5] - Número")
        print("[6] - Complemento")
        print("[7] - Bairro")
        print("[8] - Cidade")
        print("[9] - UF")
        print("[0] - Voltar ao gerenciador de clientes")

        opc = eval (input("\nDigite a opçao desejada: "))#leitra da opção
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

def at_nome(codcliente): #atualização do nome
    new = input("Digite o novo nome: ")
    cursor.execute("UPDATE cliente SET NOME_CLI = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nNome atualizado com sucesso!")
    pausa()

def at_telf(codcliente): #atualização do telefone fixo
    new = input("Digite o novo Telefone Fixo: ")
    cursor.execute("UPDATE cliente SET TEL_FIXO = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nTelefone Fixo atualizado com sucesso!")
    pausa()

def at_telc(codcliente):#atualização do telefone celular
    new = input("Digite o novo Telefone Celular: ")
    cursor.execute("UPDATE cliente SET TEL_CEL = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nTelefone Celular atualizado com sucesso!")
    pausa()

def at_end(codcliente):#atualização do endereço
    new = input("Digite o novo Endereço: ")
    cursor.execute("UPDATE cliente SET ENDERECO = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nEndereço atualizado com sucesso!")
    pausa()

def at_num(codcliente): #atualização do número do endereço
    new = input("Digite o novo Número: ")
    cursor.execute("UPDATE cliente SET NR_END = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nNúmero atualizado com sucesso!")
    pausa()

def at_comp(codcliente): #atualização do complemento
    new = input("Digite o novo Comlemento: ")
    cursor.execute("UPDATE cliente SET COMPLEMENTO = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nComplemento atualizado com sucesso!")
    pausa()

def at_bairro(codcliente): #atualização do bairro
    new = input("Digite o novo Bairro: ")
    cursor.execute("UPDATE cliente SET BAIRRO = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nBairro atualizado com sucesso!")
    pausa()

def at_cid(codcliente): #atualização da cidade
    new = input("Digite a nova Cidade: ")
    cursor.execute("UPDATE cliente SET CIDADE = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nCidade atualizada com sucesso!")
    pausa()

def at_uf(codcliente): #atualização do estado (UF)
    new = input("Digite o novo Estado (UF): ")
    cursor.execute("UPDATE cliente SET UF = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nEstado atualizado com sucesso!")
    pausa()

def ativar_cliente(): #ativação de cliente
    codi = (input("Digite o código do cliente que deseja reativar: "))
    cursor.execute("UPDATE cliente SET DATA_INATIVO = NULL WHERE CODIGO_CLI = ?", (codi))

    cursor.connection.commit()

    print("Cliente reativado com sucesso!")
    pausa()

def desativar_cliente(): #desativando cliente
    codi = (input("Digite o código do cliente que deseja desativar: "))
    cursor.execute("UPDATE cliente SET DATA_INATIVO = ? WHERE CODIGO_CLI = ?", (lETDATE(), codi))

    cursor.connection.commit()

    print("Cliente desativado com sucesso!")
    pausa()



def menu_cliente(): #menu que gerencia as funções com clientes
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

    o = eval(input("\nDigite a opção desejada: "))#lendo a opção desejada

    if o == 1:
        limparTelaOS()#limpando a tela
        listar_clientes()#função da opção desejada
        limparTelaOS()#limpando a tela
        menu_cliente()#voltando ao menu de cliente
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
    else :
        limparTelaOS()
        print("Opção Invalida!")
        pausa()
        limparTelaOS()
        menu_cliente()
        

menu_cliente()

# fechando conexão
Bifrost.connection.close()