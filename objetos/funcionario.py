codigo = 0
lista_funcionarios = []

def novo_codigo():
    global codigo
    codigo = codigo + 1
    return codigo

class Funcionario:

    def __init__(self, nome, salario_base):
        self.nome = nome
        self.codigo = novo_codigo()
        self.salario_base = salario_base

    def __str__(self) -> str:
        return f'\n código: {self.codigo} \n nome: {self.nome} \n salário base: R${round(self.salario_base, 2)}'

    def calcular_salario(self):
        return f'\n O salário do(a) funcionário(a) {self.nome} é de: R${round(self.salario_base, 2)}'

