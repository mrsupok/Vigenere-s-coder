print("Vigenère encoder and decoder for the english alphabet. Шифратор и дешифратор Виженера для английского алфавита.")
print("Made by ChatGPT & supok#5961. Сделано с помощью ChatGPT и supok#5961.")
print()
print("   1 - Encoder. Шифратор. ")
print("   2 - Decoder. Дешифратор. ")
while True:
    
    say = input()
    
    if say=="1":
        def vigenere_cipher(plaintext, key, decrypt=False):
            key_length = len(key)
            key_as_int = [ord(i) for i in key]
            plaintext_int = [ord(i) for i in plaintext]
            ciphertext = ''
            for i in range(len(plaintext_int)):
                if plaintext[i].isalpha():
                    if decrypt:
                        x = (plaintext_int[i] - key_as_int[i % key_length]) % 26
                    else:
                        x = (plaintext_int[i] + key_as_int[i % key_length]) % 26
                    x += ord('A')
                    ciphertext += chr(x)
                else:
                    ciphertext += plaintext[i]
            return ciphertext

        plaintext = input("Enter the message: ")
        key = input("Enter the key: ")
        print("Ciphertext: " + vigenere_cipher(plaintext.upper(), key.upper()))

    if say=="2":
        def vigenere_decipher(ciphertext, key):
            key_length = len(key)
            key_as_int = [ord(i) for i in key]
            ciphertext_int = [ord(i) for i in ciphertext]
            plaintext = ''
            for i in range(len(ciphertext_int)):
                if chr(ciphertext_int[i]) in [' ', '.', '!', '?', '=', '+', '-', '_', ',', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    plaintext += chr(ciphertext_int[i])
                elif chr(ciphertext_int[i]).isalpha():
                    x = (ciphertext_int[i] - key_as_int[i % key_length] + 26) % 26
                    x += ord('A')
                    plaintext += chr(x)
            return plaintext

        ciphertext = input("Enter the ciphertext: ")
        key = input("Enter the key: ")
        print("Plaintext: " + vigenere_decipher(ciphertext.upper(), key.upper()))

    else:
        print()


