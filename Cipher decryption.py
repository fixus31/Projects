# Cipher decryption

def decryption(cipher_text, offset):
    plain_text = ""
    for i in range(len(cipher_text)):
        letter = cipher_text[i]

        if(letter.isupper()):
            plain_text += chr((ord(letter) + offset - 65) % 26 + 65)
        else:
            plain_text += chr((ord(letter) + offset - 97) % 26 + 97)
    return plain_text

cipher_text = raw_input("Enter the Cipher Text: ")
offset = 0

while offset < 26:
    print(str(offset + 1) + " letters shift " + decryption(cipher_text, offset))
    offset += 1
