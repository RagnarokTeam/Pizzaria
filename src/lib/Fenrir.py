"""
Data........: 2020-05-14
Projeto.....: RagnarokProject - Pizzaria
Arquivo.....: Fenrir.py
Descrição...: Conexão generalizada para toda a aplicação
Autor.......: Jefferson de L. Matos - Eq. Ragnarok
Observações.: 2020-05-22 - [R00] Criação do Arquivo - Versao 1.00
              ...
Referencias:
"""
from datetime import datetime


def GETDATE():
    data = datetime.now().strftime("%d/%m/%Y")
    return data


print(GETDATE())
