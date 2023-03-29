def fibo():
    '''Pede um número inteiro e verifica se o mesmo faz parte da sequência de Fibonacci.'''

    num = int(input('Digite um número inteiro: '))


    # Há dois locais que podem retornar sim, então coloquei dentro dessa váriavel..
    pertence = f'O número {num} pertence a sequência de Fibonacci.'

    a, b = 0, 1

    if num == 0 or num == 1:
        return pertence
    
    while b < num:
        c = a + b
        a, b = b, c

        if c == num:
            return pertence
        
    return f'O número {num} não pertence a sequência de Fibonacci.'

print(fibo())
