import random

def is_prime(num, k=5):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False

    def is_probably_prime(num, k):
        if num <= 4:
            return True
        for _ in range(k):
            a = random.randint(2, num - 2)
            x = pow(a, num - 1, num)
            if x != 1:
                return False
        return True

    return is_probably_prime(num, k)

def find_primitive_root(prime):
    if prime == 2:
        return 1
    for primitive in range(2, prime):
        if pow(primitive, prime - 1, prime) == 1:
            return primitive

while True:
    prime_number = int(input("Enter a prime number (P): "))
    if not is_prime(prime_number):
        print("P is not a prime number. Please enter a prime number.")
    else:
        break

primitive_root = find_primitive_root(prime_number)
print(f"The primitive root of {prime_number} is {primitive_root}")

user1_private_key = int(input("Enter the private key of User 1: "))
user2_private_key = int(input("Enter the private key of User 2: "))

if user1_private_key >= prime_number or user2_private_key >= prime_number:
    print(f"Private keys should be less than {prime_number}!")
else:
    user1_public_key = pow(primitive_root, user1_private_key, prime_number)
    user2_public_key = pow(primitive_root, user2_private_key, prime_number)
    
    shared_key1 = pow(user2_public_key, user1_private_key, prime_number)
    shared_key2 = pow(user1_public_key, user2_private_key, prime_number)
    
    if shared_key1 == shared_key2:
        print(f"\nShared Key for User 1 is {shared_key1}")
        print(f"Shared Key for User 2 is {shared_key2}")
        print("Keys have been exchanged successfully.")
    else:
        print("Keys have not been exchanged successfully.")
