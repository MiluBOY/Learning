def sieve_of_eratosthenes(n):
    """
    获取小于等于n的所有质数
    """
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    primes = [i for i in range(2, n+1) if is_prime[i]]
    return primes

primes = sieve_of_eratosthenes(9999)
print(primes)