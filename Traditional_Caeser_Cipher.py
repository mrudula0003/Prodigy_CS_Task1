def encrypt(text, en_key, cipher):
    for i in text:
        if i == " ":
            cipher += " "
        else:
            cipher += chr((ord(i) + en_key - 65) % 26 + 65)
    return cipher


def decrypt(text, dc_key, cipher):
    for i in cipher:
        if i == " ":
            text += " "
        else:
            text += chr((ord(i) + dc_key - 65) % 26 - 65)
    return plain_text


ip_text = input("enter string:")
plain_text = ip_text.upper()
key = int(input("enter key:"))
cipher_txt = " "
e = encrypt(plain_text, key, cipher_txt)
print("cipher (encrypted):", e)
d = decrypt(plain_text, key, cipher_txt)
print("cipher (decrypted):", d)
