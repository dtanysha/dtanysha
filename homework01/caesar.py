import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    alfavit = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(plaintext)):
        if plaintext[i].islower():
            m = alfavit.index(plaintext[i])
            ciphertext += alfavit[(m + shift) % len(alfavit)]
        elif plaintext[i].isupper():
            m = alfavit.index(plaintext[i].lower())
            ciphertext += alfavit[(m + shift) % len(alfavit)].upper()
        else:
            ciphertext += plaintext[i]

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    alfavit = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(ciphertext)):
        if ciphertext[i].islower():
            m = alfavit.index(ciphertext[i])
            plaintext += alfavit[(m - shift) % len(alfavit)]
        elif ciphertext[i].isupper():
            m = alfavit.index(ciphertext[i].lower())
            plaintext += alfavit[(m - shift) % len(alfavit)].upper()
        else:
            plaintext += ciphertext[i]

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    for i in range(26):
        if decrypt_caesar(ciphertext) in dictionary:
            best_shift = i
    return best_shift