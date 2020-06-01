def relatorioPorData():
    datainicial = '23-05-2020' #input("Digite a data inicial")
    datafinal = '27-12-2020' #input("Digite a data final") 
    cursor.execute("select COD_PED, DATA_PED, CODIGO_CLI, TOTAL_PED from PEDIDO WHERE DATA_PED BETWEEN "+ datainicial + " AND "+ datafinal)
 
    print('\nRELATÓRIO DE PEDIDOS ENTRE', datainicial, 'E', datafinal)
    all_rows = cursor.fetchall()
    for user1 in all_rows:
        print('------------------------------------------------------------')
        print('Códog do Pedido:', user1[0])  # Imprime o primeiro campo
        print('Data:', user1[1])  # Imprime o segundo campo
        print('Códogo do Cliente:', user1[2])  # Imprime o terceiro campo22-03-2020
        print('Total do Pedido:', user1[3])  # Imprime o terceiro campo
        print('\n')
    cursor.connection.commit()    
    pause()
    limparTelaOS()

relatorioPorData()