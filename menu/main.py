"""
Data........: 2020-05-08
Projeto.....: Projeto03
Descricao...: Modelo de estrutura de projeto
Arquivo.....: Main.py - Função Principal contendo menu para chamada das demais funções
Autor.......: Rodrigo Saito
Observações.: 2020-05-08 - [R00] Criação do Arquivo - Versao 1.00
              ...
"""

import os

from sources.lib import library

def cadastroCliente():
    input("Telefone Fixo: ")
    input('Telefone Celular: ')
    input('Nome Completo: ')
    input('Endereço: ')
    input('Número: ')
    input('Complemento (Se Tiver): ')
    input('Bairro: ')
    input('Cidade: ')
    input('UF: ')
    input('CEP: ')
    

def menuPrincipal():
    opcao = 0
    while opcao != 9:
        library.cabecalhoMenu()
        print('MENU PRINCIPAL')
        print('[1] - Cliente Cadastrado')
        print('[2] - Cliente Novo')
        print('[9] - Sair')
        opcao = eval(input('Digite a opção desejada: '))
        print('Opcao escolhido foi: ', opcao)

        if opcao == 1:
            input('Digite o numero de telefone do cliente: ')
        #    menuCriaBasePadrao()
        elif opcao == 2:
            cadastroCliente()

        else:
            print('Opcao invalida!')

def main():
    menuPrincipal()

if __name__ == '__main__': # chamada da funcao principal
    main()

