def numprimo(n):
    if n < 2:
        return False
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True

print(numprimo(17))  
print(numprimo(10))
#verifica se um número inteiro é primo ou não

