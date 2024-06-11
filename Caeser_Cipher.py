import string

# list of special characters
sp_char = list(string.punctuation)

# encryption of (case-sensitive) alpha-numeric characters as well as special characters
def encrypt(text, en_key):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            result += chr((ord(char) - ascii_offset + en_key) % 26 + ascii_offset)
        elif char.isdigit():
            result += str((int(char) + en_key) % 10)
        else:
            if char in sp_char:
                char_index = sp_char.index(char)
                dsp = char_index + en_key
                result += sp_char[dsp]
    return result

# decryption of encrypted text which includes alpha-numeric characters as well as special characters
def decrypt(text, dc_key):
    result = ""
    org_shift = dc_key
    shift = 26 - dc_key
    for char in text:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        elif char.isdigit():
            result += str((int(char) - org_shift) % 10)
        else:
            if char in sp_char:
                char_index = sp_char.index(char)
                dsp = char_index - org_shift
                result += sp_char[dsp]
    return result

# Dynamic code: pursuing text and key from user to encrypt & decrypt it respectively
plaintext = input("Enter the text to encrypt: ")
key = int(input("Enter the Key: "))

#output code: displaying the original text, key, encrypted text, and decrypted text.
print("Text :", plaintext, "\t Key :", key)
cipher = encrypt(plaintext, key)
print("Cipher (Encrypted):", cipher)
print("Cipher (Decrypted):", decrypt(cipher, key))
