def filter_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
l = list(map(int, input().split()))
primes = [num for num in l if  filter_prime(num)]
print(primes)