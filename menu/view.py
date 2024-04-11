from objetos.funcionario import lista_funcionarios
from utils.utils import input_digito
from objetos.horista import Horista
from objetos.comissao import Comissao
from objetos.assalariado import Assalariado

def opc_horista():
    nome = input('\n Digite o nome do funcionário: ')
    salario_base = input_digito('\n Digite o salário base do funcionário: ')
    valor_hora = input_digito('\n Insira o valor/hora do funcionário: ')
    funcionario = Horista(nome, salario_base, valor_hora)
    lista_funcionarios.append(funcionario)
    print('\n Funcionário cadastrado com sucesso! \n')
    print(funcionario)

def opc_comissao():
    nome = input('\n Digite o nome do funcionário: ')
    salario_base = input_digito('\n Digite o salário base do funcionário: ')
    porcentagem_comissao = input_digito('\n Insira a porcentagem de comissão: ')
    funcionario = Comissao(nome, salario_base, porcentagem_comissao)
    lista_funcionarios.append(funcionario)
    print('\n Funcionário cadastrado com sucesso! \n')
    print(funcionario)

def opc_assalariado():
    nome = input('\n Digite o nome do funcionário: ')
    salario_base = input_digito('\n Digite o salário base do funcionário: ')
    funcionario = Assalariado(nome, salario_base)
    lista_funcionarios.append(funcionario)
    print('\n Funcionário cadastrado com sucesso! \n')
    print(funcionario)

def consulta_funcionario():
        codigo = input_digito('\n Digite o código identificador do funcionário(a) para o cálculo do salário: ')

        for funcionario in lista_funcionarios:
            if getattr(funcionario, 'codigo') == codigo:
                return funcionario
             
        print(f'\n Digite um valor válido')

def salario():
    funcionario = consulta_funcionario()
    if isinstance(funcionario, Assalariado):
        print(funcionario.calcular_salario())

    elif isinstance(funcionario, Horista):
        horas_extras_trabalhadas = input_digito('\n Digite a quantidade de horas extras trabalhadas: ')
        print(funcionario.calcular_salario(horas_extras_trabalhadas))

    elif isinstance(funcionario, Comissao):
        valor_vendas = input('\n Digite o valor das vendas realizadas: ')
        print(funcionario.calcular_salario(valor_vendas))
        
