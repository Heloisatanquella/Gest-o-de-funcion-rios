def input_digito(msg):
    while True:
            digito = input(msg)
            if digito.isdigit():
                return float(digito)
            print('Digite um valor válido')