# """
# Data........: 2020-05-23
# Projeto.....: Pizzaria-Ragnarok
# Arquivo.....: main.py
# Descrição...: Menu Principal
# Autor.......: Paula Tanaka - Eq. Ragnarok
# Observações.: 2020-05-08 - [R00] Criação do Arquivo - Versao 1.00
#
# Referencias:
# ""

import os

from sources.lib import library

def limparTelas():
    print('\n' * 40)

def cadastroCliente():
    limparTelas()
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
    limparTelas()
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
        library.cabecalhoMenu()
        print('MENU PRINCIPAL')
        print('[1] - Cliente Cadastrado')
        print('[2] - Cliente Novo')
        print('[3] - Relatorios')
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
        else:
            print('Opcao invalida!')

def main():
    menuPrincipal()

if __name__ == '__main__': # chamada da funcao principal
    main()

