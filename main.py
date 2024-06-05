def calcular_fatorial(n):
    if n == 0:
        return 1
    else: 
        return n * calcular_fatorial(n - 1)
    

# programa principal

n = int(input('Informe o número inteiro:'))

# exibir o fatorial

print(f'Fatorial de {n}: {calcular_fatorial(n)}.')