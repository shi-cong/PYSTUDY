from sclib.encryptlib import caesar_cipher, reverse_cipher, transposition_cipher

result = caesar_cipher("QYH I miss you!", 13)
print(result)

result = reverse_cipher("QYH I miss you!")
print(result)

result = transposition_cipher(5, "QYH I miss you!")
print(result)