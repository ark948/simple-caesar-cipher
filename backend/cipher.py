from string import ascii_lowercase, ascii_uppercase, punctuation


def caesar_cipher_encrypt(s, key):
    new_s = []
    for i in s:
        if i == ' ':
            new_s.append(' ')
            continue
        if i.isupper():
            pos = ascii_uppercase.index(i)
            new_s.append(ascii_uppercase[(pos + key) % 26])
            continue
        if i in punctuation:
            new_s.append(i)
            continue
        pos = ascii_lowercase.index(i)
        new_s.append(ascii_lowercase[(pos + key) % 26])
    return ''.join(new_s)


def caesar_cipher_decrypt(s, key):
    new_s = []
    for i in s:
        if i == ' ':
            new_s.append(' ')
            continue
        if i.isupper():
            pos = ascii_uppercase.index(i)
            new_s.append(ascii_uppercase[(pos - key) % 26])
            continue
        if i in punctuation:
            new_s.append(i)
            continue
        pos = ascii_lowercase.index(i)
        new_s.append(ascii_lowercase[(pos - key) % 26])
    return ''.join(new_s)