##Cypher encryption

def encryption(plain_text, offset):
    cypher_text = ""
    for i in range(len(plain_text)):
        letter = plain_text[i]

        if (letter.isupper()):
            cypher_text += chr((ord(letter) + offset - 65) % 26 + 65)
        else:
            cypher_text += chr((ord(letter) + offset - 97) % 26 + 97)
    return cypher_text

plain_text = raw_input("Enter word to encode: ")
offset = input("Enter the offset by how many shifts: ")

print("Plaintext: " + plain_text)
print("Encypted text: " + encryption(plain_text, offset))
