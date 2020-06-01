 from src.db.Asgard import Bifrost


# variavel "cursor" pode ser alterada para qualquer outro nome de sua escolha
cursor = Bifrost.connection.cursor()



# fim da bifrost
Bifrost.connection.close()
