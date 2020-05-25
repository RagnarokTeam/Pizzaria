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
from src.lib.Fenrir import GETDATE
from src.lib.Fenrir import limparTelaOS
from src.main import menuPrincipal

# variavel "cursor" pode ser alterada para qualquer outro nome de sua escolha
cursor = Bifrost.connection.cursor()

def pausa():
    programPause = input("\nPressione <ENTER> para voltar ao menu.")

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

    novoCliente = [(telf, telc, nome, end, num, comp, bai, cid, uf, GETDATE())] #lista com os dados obtidos
       
    cursor.executemany("INSERT INTO cliente(TEL_FIXO, TEL_CEL, NOME_CLI, ENDERECO, NR_END, COMPLEMENTO, \
                        BAIRRO, CIDADE, UF, DATA_CADASTRO) \
                    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", novoCliente) #alocando no banco

    cursor.connection.commit()
    print('\nCliente cadastrado com sucesso!')
    pausa()

def atualizar_cliente (): #função para atualizar algum dado do cliente
    opc = 0
    cod = input("Digite o código do cliente: ")#pegando o cod para passar para funções de atualização
    print("[1] - Nome")
    print("[2] - Telefone Fixo")
    print("[3] - Telefone Celular")
    print("[4] - Endereço")
    print("[5] - Número")
    print("[6] - Complemento")
    print("[7] - Bairro")
    print("[8] - Cidade")
    print("[9] - UF")
    print("[0] - Voltar ao gerenciador de clientes")

    opc = eval (input("\nDigite a opçao desejada: "))
    if opc == 1:
        limparTelaOS()
        at_nome(cod)
        limparTelaOS()
    elif opc == 2:
        limparTelaOS()
        at_telf(cod)
        limparTelaOS()
    elif opc == 3:
        limparTelaOS()
        at_telc(cod)
        limparTelaOS()
    elif opc == 4:
        limparTelaOS()
        at_end(cod)
        limparTelaOS()
    elif opc == 5:
        limparTelaOS()
        at_num(cod)
        limparTelaOS()
    elif opc == 6:
        limparTelaOS()
        at_comp(cod)
        limparTelaOS()
    elif opc == 7:
        limparTelaOS()
        at_bairro(cod)
        limparTelaOS()
    elif opc == 8:
        limparTelaOS()
        at_cid(cod)
        limparTelaOS()
    elif opc == 9:
        limparTelaOS()
        at_uf(cod)
        limparTelaOS()
    elif opc == 0:
        limparTelaOS()
        menu_cliente()

def at_nome(codcliente): #atualização do nome
    new = input("Digite o novo nome: ")
    cursor.execute("UPDATE cliente SET NOME_CLI = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nNome atualizado com sucesso!")
    pausa()

def at_telf(codcliente):
    new = input("Digite o novo Telefone Fixo: ")
    cursor.execute("UPDATE cliente SET TEL_FIXO = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nTelefone Fixo atualizado com sucesso!")
    pausa()

def at_telc(codcliente):
    new = input("Digite o novo Telefone Celular: ")
    cursor.execute("UPDATE cliente SET TEL_CEL = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nTelefone Celular atualizado com sucesso!")
    pausa()

def at_end(codcliente):
    new = input("Digite o novo Endereço: ")
    cursor.execute("UPDATE cliente SET ENDERECO = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nEndereço atualizado com sucesso!")
    pausa()

def at_num(codcliente):
    new = input("Digite o novo Número: ")
    cursor.execute("UPDATE cliente SET NR_END = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nNúmero atualizado com sucesso!")
    pausa()

def at_comp(codcliente):
    new = input("Digite o novo Comlemento: ")
    cursor.execute("UPDATE cliente SET COMPLEMENTO = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nComplemento atualizado com sucesso!")
    pausa()

def at_bairro(codcliente):
    new = input("Digite o novo Bairro: ")
    cursor.execute("UPDATE cliente SET BAIRRO = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nBairro atualizado com sucesso!")
    pausa()

def at_cid(codcliente):
    new = input("Digite a nova Cidade: ")
    cursor.execute("UPDATE cliente SET CIDADE = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nCidade atualizada com sucesso!")
    pausa()

def at_uf(codcliente):
    new = input("Digite o novo Estado (UF): ")
    cursor.execute("UPDATE cliente SET UF = ? WHERE CODIGO_CLI = ?", (new, codcliente))

    cursor.connection.commit()

    print("\nEstado atualizado com sucesso!")
    pausa()

def ativar_cliente():
    codi = (input("Digite o código do cliente que deseja reativar: "))
    cursor.execute("UPDATE cliente SET DATA_INATIVO = NULL WHERE CODIGO_CLI = ?", (codi))

    cursor.connection.commit()

    print("Cliente reativado com sucesso!")
    pausa()

def desativar_cliente():
    codi = (input("Digite o código do cliente que deseja desativar: "))
    cursor.execute("UPDATE cliente SET DATA_INATIVO = ? WHERE CODIGO_CLI = ?", (GETDATE(), codi))

    cursor.connection.commit()

    print("Cliente desativado com sucesso!")
    pausa()

def menu_cliente():
    limparTelaOS()
    o = 0
    print(" Gerenciador de Clientes\n ")
    print("[1] - Novo Cliente")
    print("[2] - Atualizar Cliente")
    print("[3] - Ativar Cliente")
    print("[4] - Desativar Cliente")
    print("[5] - Voltar ao Menu Principal")

    o = eval(input("\nDigite a opção desejada: "))

    if o == 1:
        limparTelaOS()
        novo_cliente()
        limparTelaOS()
        menu_cliente()
    elif o == 2:
        limparTelaOS()
        atualizar_cliente()
        limparTelaOS()
        menu_cliente()
    elif o == 3:
        limparTelaOS()
        ativar_cliente()
        limparTelaOS()
        menu_cliente()
    elif o == 4:
        limparTelaOS()
        desativar_cliente()
        limparTelaOS()
        menu_cliente()
    elif o == 5:
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