from objetos.funcionario import Funcionario

class Horista(Funcionario):
    def __init__(self, nome, salario_base, valor_hora):
        super().__init__(nome, salario_base)
        # self.nome = nome
        # self.codigo = codigo_funcionario + 1
        # self.salario_base = salario_base
        # codigo_funcionario = codigo_funcionario + 1
        self.valor_hora = valor_hora

    def calcular_salario(self, horas_extras_trabalhadas):
        salario = self.salario_base + (self.valor_hora * horas_extras_trabalhadas)
        return f'\n O salário do(a) funcionário(a) {self.nome} é de: R${round(salario, 2)}'
    


