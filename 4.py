def f(n):
    if n == 0 or n == 1:
        return 1
    return n * f(n-1)

print(f(5))  
print(f(0))  
#calcula o fatorial de um número inteiro
