def is_prime(n):
    if n == 1: return False
    

    for x in range(2,n):
        if n % x == 0:
            return False

    print("素数")

is_prime(47)