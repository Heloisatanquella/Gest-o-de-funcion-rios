
from menu.menu import menu, sub_menu_cadastro
from menu.view import salario, opc_assalariado, opc_horista, opc_comissao

def main():
    while True:
        opc = menu()
        if opc == 1:
            sub_opc = sub_menu_cadastro()

            if sub_opc == 1:            
                opc_assalariado()
            if sub_opc == 2: 
               opc_horista()
            if sub_opc == 3:
                opc_comissao()
            if sub_opc == 4:
                break

        if opc == 2: 
            salario()

        if opc == 3:
            break

main()