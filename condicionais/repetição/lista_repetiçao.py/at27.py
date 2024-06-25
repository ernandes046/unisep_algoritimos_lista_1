
def fibonacci(n):
    fib_sequence = [1, 2]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def soma_pares_fibonacci(n):
    fib_sequence = fibonacci(n)
    soma = sum(num for num in fib_sequence if num % 2 == 0)
    return soma

limite = 4000000
soma = soma_pares_fibonacci(limite)
print("A soma dos termos pares da sequência de Fibonacci até", limite, "é:", soma)
