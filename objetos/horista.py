from objetos.funcionario import Funcionario, lista_funcionarios

class Horista(Funcionario):
    def __init__(self, nome, salario_base, valor_hora, horas_extras_trabalhadas):
        super().__init__(nome, salario_base)
        # self.nome = nome
        # self.codigo = codigo_funcionario + 1
        # self.salario_base = salario_base
        # codigo_funcionario = codigo_funcionario + 1
        self.valor_hora = float(valor_hora)
        self.horas_extras_trabalhadas = float(horas_extras_trabalhadas)

    def calcular_salario(self):
        salario = self.salario_base + (self.valor_hora * self.horas_extras_trabalhadas)
        return self.str_salario(salario) 
    
def opc_horista():
    nome = input('\n Digite o nome do funcionário: ')
    salario_base = input('\n Digite o salário base do funcionário: ')
    valor_hora = input('\n Insira o valor/hora do funcionário: ')
    horas_extras_trabalhadas = input('\n Insira as horas adicionais trabalhadas: ')
    funcionario = Horista(nome, salario_base, valor_hora, horas_extras_trabalhadas)
    lista_funcionarios.append(funcionario)
    print('Funcionário cadastrado com sucesso!')
    print(funcionario)

