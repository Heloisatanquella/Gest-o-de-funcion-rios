from objetos.funcionario import Funcionario

class Comissao(Funcionario):
    def __init__(self, nome, salario_base, porcentagem_comissao):
        super().__init__(nome, salario_base)
        # self.nome = nome
        # self.codigo = codigo_funcionario + 1
        # self.salario_base = salario_base
        # codigo_funcionario = codigo_funcionario + 1
        self.porcentagem_comissao = porcentagem_comissao

    def calcular_salario(self, valor_vendas):
        salario = self.salario_base + ((valor_vendas / 100 )* self.porcentagem_comissao)
        return f'\n O salário do(a) funcionário(a) {self.nome} é de: R${round(salario, 2)}'

    

