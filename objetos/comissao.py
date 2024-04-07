from objetos.funcionario import Funcionario, lista_funcionarios

class Comissao(Funcionario):
    def __init__(self, nome, salario_base, porcentagem_comissao, valor_vendas):
        super().__init__(nome, salario_base)
        # self.nome = nome
        # self.codigo = codigo_funcionario + 1
        # self.salario_base = salario_base
        # codigo_funcionario = codigo_funcionario + 1
        self.porcentagem_comissao = float(porcentagem_comissao)
        self.valor_vendas = float(valor_vendas)

    def calcular_salario(self):
        salario = self.salario_base + ((self.valor_vendas / 100 )* self.porcentagem_comissao)
        return self.str_salario(salario) 
    
def opc_comissao():
    nome = input('\n Digite o nome do funcionário: ')
    salario_base = input('\n Digite o salário base do funcionário: ')
    porcentagem_comissao = input('\n Insira a porcentagem de comissão: ')
    valor_vendas = input('\n Insira o valor total das vendas realizadas: ')
    funcionario = Comissao(nome, salario_base, porcentagem_comissao, valor_vendas)
    lista_funcionarios.append(funcionario)
    print('Funcionário cadastrado com sucesso!')
    print(funcionario)
