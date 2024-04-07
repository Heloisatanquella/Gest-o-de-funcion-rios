codigo = 0
lista_funcionarios = []

def novo_codigo():
    global codigo
    codigo = codigo + 1
    return codigo

def consulta_funcionario():
    print(f'\n Selecione qual funcionário você deseja calcular o salário')

    while True:
        codigo = input('Digite o código identificador do funcionário(a) para o cálculo do salário: ')

        if codigo.isdigit():
            codigo = int(codigo)

            for funcionario in lista_funcionarios:
                if getattr(funcionario, 'codigo') == codigo:
                    salario = funcionario.calcular_salario()
                    print(salario)
                    return salario
               
            
        print(f'\n Digite um valor válido')


class Funcionario:

    def __init__(self, nome, salario_base):
        self.nome = nome
        self.codigo = novo_codigo()
        self.salario_base = float(salario_base)

    def __str__(self) -> str:
        return f'\n código: {self.codigo} \n nome: {self.nome} \n salário base: {self.salario_base}'
    
    def str_salario(self, salario):
        return f'\n O salário do(a) funcionário(a) {self.nome} é de: R${salario}'

    def calcular_salario(self):
        return self.str_salario(self.salario_base)

