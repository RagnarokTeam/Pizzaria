"""
Data.Criacao: 2020-05-08
Projeto.....: Projeto03
Descricao...: Arquivo de biblioteca, contendo rotinas (procedures e funções) comuns para utilização em qualquer
              módulo do sistema
Arquivo.....: Library.py - Função Principal contendo menu para chamada das demais funções
Autor.......: Rodrigo Saito
Observações.: 2020-05-08 - [R00] Criação do Arquivo - Versao 1.00
              ...
"""

import os
import datetime


# envia uma string, geralmente com o caminho relativo e retorna o conteúdo da última posicao do vetor,
# geralmente o nome do arquivo
def file_name(string):
    count = string.find('/')     # find retorna a posicao do caracter a ser encontrado

    if count >= 1:               # se existe o caracter em qualquer posição da string
        sTmp = string.split('/')
    else:
        sTmp = string.split('\\')

    sTmp = sTmp[-1]   # ultimo elemento do vetor, que é o nome do arquivo puro
    return sTmp

# Retorna somente a data e hora atual,
def datetime_fmt(formatstring):
    # no formato YYYY-MM-DD HH: MM:SS
    if formatstring == 'YYYY-MM-DD HH:MM:SS.MS':
        return format(datetime.datetime.now())

def limparTelaOS():
    if os.system == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def limparTelaIdle():
    print('\n' * 40)


def cabecalhoMenu():
    limparTelaIdle()
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

def pause():
    programPause = input("\nPressione <ENTER> para continuar...")
    


