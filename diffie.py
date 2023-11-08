import random

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Miller-Rabin primality test
    def is_probably_prime(n, k):
        if n <= 4:
            return True
        for _ in range(k):
            a = random.randint(2, n - 2)
            x = pow(a, n - 1, n)
            if x != 1:
                return False
        return True

    return is_probably_prime(n, k)

def find_primitive_root(p):
    if p == 2:
        return 1
    for g in range(2, p):
        if pow(g, p - 1, p) == 1:
            return g

while True:
    P = int(input("Enter a prime number (P): "))
    if not is_prime(P):
        print("P is not a prime number. Please enter a prime number.")
    else:
        break

G = find_primitive_root(P)
print(f"The primitive root of {P} is {G}")

x1 = int(input("Enter the private key of User 1: "))
x2 = int(input("Enter the private key of User 2: ")

if x1 >= P or x2 >= P:
    print(f"Private keys should be less than {P}!")
else:
    y1 = pow(G, x1, P)
    y2 = pow(G, x2, P)
    
    k1 = pow(y2, x1, P)
    k2 = pow(y1, x2, P)
    
    if k1 == k2:
        print(f"\nSecret Key for User 1 is {k1}")
        print(f"Secret Key for User 2 is {k2}")
        print("Keys have been exchanged successfully.")
    else:
        print("Keys have not been exchanged successfully.")
