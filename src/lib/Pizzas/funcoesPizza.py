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

# variavel "cursor" pode ser alterada para qualquer outro nome de sua escolha
cursor = Bifrost.connection.cursor()


def nova_pizza():  # solicita os dados, os coloca em uma lista e aloca no banco
    cod = (input("Código da Pizza: "))
    data = (input("Data de criação: (formato: DD/MM/AAAA)"))
    nome = (input("Nome da pizza:"))
    ing = (input("Ingredientes: "))
    valor = (input("Valor de Custo:"))

    novaPizza = [(cod, data, nome, ing, valor)];  # lista com os dados obtidos

    cursor.executemany("INSERT INTO pizza(CODIGO_PIZ, DATA_CRIACAO, NOME_PIZ, INGREDIENTES, VALOR_CUSTO) \
                    values (?, ?, ?, ?, ?)", novaPizza)  # alocando no banco
    cursor.connection.commit()
    print('Pizza', nome, 'cadastrada com sucesso!')



def apagar_pizza():  # funçao para apagar pizza do banco

    cod = (input("Digite o código da pizza que deseja apagar: "))

    # excluindo a pizza pelo seu código
    cursor.execute("""DELETE FROM pizza WHERE CODIGO_PIZ = ?""", (cod,))

    cursor.connection.commit()

    print("Pizza apagada com sucesso!")


# fechando conexão
cursor.connection.close();
