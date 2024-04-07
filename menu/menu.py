def menu():
    print(f'\n Selecione qual a categoria de funcionário você deseja acessar')

    while True:
        print(f'\n Opção 1: Cadastrar novo funcionário')
        print(f'\n Opção 2: Consultar salário')
        print(f'\n Opção 3: Encerrar programna')
        opc = input('\n')

        if opc.isdigit():
                    opc = int(opc)
                    if opc > 0 and opc < 4:
                        return opc
                    
        print(f'\n Digite um valor válido')

def sub_menu_cadastro():
    print(f'\n Selecione qual a categoria de funcionário você deseja acessar')

    while True:
        print(f'\n Opção 1: Assalariado')
        print(f'\n Opção 2: Por hora')
        print(f'\n Opção 3: Por comissão')
        print(f'\n Opção 4: Voltar')
        opc = input('\n')

        if opc.isdigit():
                    opc = int(opc)
                    if opc > 0 and opc < 5:
                        return opc
                    
        print(f'\n Digite um valor válido')

