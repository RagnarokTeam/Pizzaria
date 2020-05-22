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
from datetime import datetime
getdate = datetime.now().strftime("%d/%m/%Y")


# variavel "cursor" pode ser alterada para qualquer outro nome de sua escolha
cursor = Bifrost.connection.cursor()


def cad_pizza():  # função que cadastra as pizzas do cardápio

    lista_pizza = [( 'Salgada',getdate, 'ALEO E OLEO', 'Alho frito picado, parmesão ralado e azeitonas', 22.90),
                   ( 'Salgada',getdate, 'ALLICI',
                    'Alicci importado, rodelas de tomate, parmesão e azeitonas', 28.90),
                   ( 'Salgada',getdate, 'ATUM', 'Atum, cebola e azeitona', 22.90),
                   ( 'Salgada',getdate, 'BACON',
                    'Bacon coberto com muzzarela e azeitonas', 26.90),
                   ( 'Salgada',getdate, 'BERINGELA',
                    'Beringela, cobertura com muzzarela, manjericão e parmesão', 23.90),
                   ( 'Salgada',getdate, 'CAIPIRA',
                    'Frango desfiado, coberto com catupiry e milho verde e azeitonas', 26.90),
                   ( 'Salgada',getdate, 'CALABRESA',
                    'Linguiça cababresa, cebola e azeitonas', 19.90),
                   ( 'Salgada',getdate, 'CINCO QUEIJOS',
                    'Muzzarela, parmesão, catupiry, gorgonzola e provolone', 29.90),
                   ( 'Salgada',getdate, 'ESCAROLA',
                    'Escarola refogada, muzzarela, e azeitonas', 24.90),
                   ( 'Salgada',getdate, 'EXECUTIVA',
                    'Milho Verde, catupiry e azeitonas', 22.90),
                   ( 'Salgada',getdate, 'PERUANA',
                    'Atum, cebola, muzarela e azeitonas', 26.90),
                   ('Salgada',getdate, 'PALMITO',
                    'Palmito com muzarela e azeitonas', 26.90),
                   ( 'Doce',getdate, 'BANANA',
                    'Banana fatiada com, cobertura com leite condensado e canela em pó', 21.90),
                   ( 'Doce',getdate, 'BRIGADEIRO',
                    'Chocolate, leite condensado e chocolate granlado', 23.90),
                   ( 'Doce',getdate, 'PRESTIGIO', 'Chocolate coberta com côco', 23.90)]

    cursor.executemany("INSERT INTO pizza( TIPO_PIZ,DATA_CRIACAO, NOME_PIZ, INGREDIENTES, VALOR_CUSTO) \
                    values ( ?,?, ?, ?, ?)", lista_pizza)

    cursor.connection.commit()
    print('Dados inseridos com sucesso!')


# Chamada da funcao de inserção de dados
cad_pizza()

# fechando conexão
cursor.connection.close()
