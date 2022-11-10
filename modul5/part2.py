# binary chars

# 10 = 0000 1010
# 10 = 0    A
# 10 = 0    12

a_number = ord('a')
A_number = ord('A')
print(bin(a_number))
print(bin(A_number))

print(max('abcd'))
print(max('AabcdZ!'))

letter1 = chr(70)
letter2 = chr(33)
print(letter1, letter2)

print('10 xor 10',10 ^ 10)

# 0000 1010 ^
# 0000 1000 = 8
# 0000 0010 ^
# 0000 1000 = 8
# 0000 1010

print('10 xor 10',(10 ^ 150)^150)


print(80*"#")

my_message = "This is my message"
encrypted_result = ''
for letter in my_message:
    encrypted_result += chr(ord(letter) ^ 48)
print(encrypted_result)

decrypted_result = ""
for letter in encrypted_result:
    decrypted_result += chr(ord(letter) ^ 48)
print(decrypted_result)

