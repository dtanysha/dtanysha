def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    alfavit1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfavit2 = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(plaintext)):
        if plaintext[i] in alfavit1:
            m = alfavit1.find(plaintext[i])
            shift = alfavit1.find(keyword[i%len(keyword)])
            ciphertext += alfavit1[(m + shift) % 26]
        else:
            m = alfavit2.find(plaintext[i])
            shift = alfavit2.find(keyword[i % len(keyword)])
            ciphertext += alfavit2[(m + shift) % 26]

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    alfavit1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfavit2 = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(ciphertext)):
        if ciphertext[i] in alfavit1:
            m = alfavit1.find(ciphertext[i])
            shift = alfavit1.find(keyword[i % len(keyword)])
            plaintext += alfavit1[(m - shift) % 26]
        else:
            m = alfavit2.find(ciphertext[i])
            shift = alfavit2.find(keyword[i % len(keyword)])
            plaintext += alfavit2[(m - shift) % 26]
    return plaintext
