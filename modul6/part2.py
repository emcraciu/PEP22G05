# generate prime numbers
import math
import random


def primes(limit):
    result = []
    for i in range(2, limit):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)
    return result


my_primes = primes(255)


# get 2 random prime number from list. Second number is smaller than first

# def get_primes(list_primes):
#     while True: # not a good solution
#         base = random.choice(list_primes)
#         if base < 129:
#             continue
#         else:
#             break
#     print(base)
#     return 1,2


def get_primes(list_primes):
    base_set = []
    for i in list_primes:
        if i >= 129:
            base_set.append(i)
    base = random.choice(base_set)
    prime_set = []
    for i in list_primes:
        if i < base:
            prime_set.append(i)
    prime = random.choice(prime_set)

    return base, prime


# bigger    #smallerr
base, prime = get_primes(my_primes)
print(f'{base} - {prime}')


def generate_local_secret(base):
    result = random.choice(range(2, base))
    return result


# this get's executed on first PC
secret1 = generate_local_secret(base)
print(secret1)  # no access to this

# this get's executed on second PC
secret2 = generate_local_secret(base)
print(secret2)  # no access to this


def generate_remote_secret(base, prime, secret):
    result = pow(prime, secret) % base
    return result


# this get's executed on first PC
remote_secret1 = generate_remote_secret(base, prime, secret1)
print(remote_secret1)

# this get's executed on second PC
remote_secret2 = generate_remote_secret(base, prime, secret2)
print(remote_secret2)

# this get's executed on first PC
local_secret1 = generate_remote_secret(base, remote_secret2, secret1)
print('First computer has', local_secret1)

# this get's executed on first PC
local_secret2 = generate_remote_secret(base, remote_secret1, secret2)
print('Second computer has', local_secret2)

assert local_secret2 == local_secret1

# Text on first computer:
my_message = "My message to encrypt"
encrypted_result = ''
for letter in my_message:
    encrypted_result += chr(ord(letter) ^ local_secret1)
print(80 * '#')
print(encrypted_result)
print(80 * '#')

# Text on second computer:
decrypted_result = ""
for letter in encrypted_result:
    decrypted_result += chr(ord(letter) ^ local_secret2)
print(decrypted_result)
