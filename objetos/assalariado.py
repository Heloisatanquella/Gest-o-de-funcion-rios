from objetos.funcionario import Funcionario, lista_funcionarios

class Assalariado(Funcionario):
    def calcular_salario(self):
        return super().calcular_salario()
    
def opc_assalariado():
    nome = input('\n Digite o nome do funcionário: ')
    salario_base = input('\n Digite o salário base do funcionário: ')
    funcionario = Assalariado(nome, salario_base)
    lista_funcionarios.append(funcionario)
    print('Funcionário cadastrado com sucesso!')
    print(funcionario)