# A python program to illustrate Caesar Cipher Technique
def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

# input
text = input("Enter text to be encrypted: ")
s = int(input("Enter the key/shift value: "))
print("Text  : " + text)
ciphertext = encrypt(text,s)
print("Cipher encrypted: " + ciphertext)


def decrypt(ciphertext, s):
    result = ""

    for char in ciphertext:
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += char

    return result


decrypted_text = decrypt(ciphertext, s)
print("Decrypted Text: " + decrypted_text)
