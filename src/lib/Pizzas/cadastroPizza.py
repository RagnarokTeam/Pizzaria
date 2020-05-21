# """
# Data........: 2020-05-16
# Projeto.....: Pizzaria-Ragnarok
# Arquivo.....: cadastro.py
# Descrição...: Cadastro das pizzas no SQLite
# Autor.......: Camila A. Oliveira - Eq. Ragnarok
# Observações.: 2020-05-08 - [R00] Criação do Arquivo - Versao 1.00
#
# Referencias:
# ""


from src.db.Asgard import Bifrost


# variavel "cursor" pode ser alterada para qualquer outro nome de sua escolha
cursor = Bifrost.connection.cursor()


def cad_pizza():  # função que cadastra as pizzas do cardápio

    lista_pizza = [(1, 'Salgada', 'ALEO E OLEO', 'Alho frito picado, parmesão ralado e azeitonas', 22.90),
                   (2, 'Salgada', 'ALLICI',
                    'Alicci importado, rodelas de tomate, parmesão e azeitonas', 28.90),
                   (3, 'Salgada', 'ATUM', 'Atum, cebola e azeitona', 22.90),
                   (4, 'Salgada', 'BACON',
                    'Bacon coberto com muzzarela e azeitonas', 26.90),
                   (5, 'Salgada', 'BERINGELA',
                    'Beringela, cobertura com muzzarela, manjericão e parmesão', 23.90),
                   (6, 'Salgada', 'CAIPIRA',
                    'Frango desfiado, coberto com catupiry e milho verde e azeitonas', 26.90),
                   (7, 'Salgada', 'CALABRESA',
                    'Linguiça cababresa, cebola e azeitonas', 19.90),
                   (8, 'Salgada', 'CINCO QUEIJOS',
                    'Muzzarela, parmesão, catupiry, gorgonzola e provolone', 29.90),
                   (9, 'Salgada', 'ESCAROLA',
                    'Escarola refogada, muzzarela, e azeitonas', 24.90),
                   (10, 'Salgada', 'EXECUTIVA',
                    'Milho Verde, catupiry e azeitonas', 22.90),
                   (11, 'Salgada', 'PERUANA',
                    'Atum, cebola, muzarela e azeitonas', 26.90),
                   (12, 'Salgada', 'PALMITO',
                    'Palmito com muzarela e azeitonas', 26.90),
                   (13, 'Doce', 'BANANA',
                    'Banana fatiada com, cobertura com leite condensado e canela em pó', 21.90),
                   (14, 'Doce', 'BRIGADEIRO',
                    'Chocolate, leite condensado e chocolate granlado', 23.90),
                   (15, 'Doce', 'PRESTIGIO', 'Chocolate coberta com côco', 23.90)]

    cursor.executemany("INSERT INTO pizza(CODIGO_PIZ, TIPO_PIZ, NOME_PIZ, INGREDIENTES, VALOR_CUSTO) \
                    values (?, ?, ?, ?, ?)", lista_pizza)

    cursor.connection.commit()
    print('Dados inseridos com sucesso!')


# Chamada da funcao de inserção de dados
cad_pizza()

# fechando conexão
Bifrost.connection.close()
