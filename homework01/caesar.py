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
    ciphertext = ""  # зашифровка
    alfavit1 = "abcdefghijklmnopqrstuvwxyz"
    alfavit2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(plaintext)):
        if plaintext[i] in alfavit1:
            m = alfavit1.index(plaintext[i])
            ciphertext += alfavit1[(m + shift) % 26]
        elif plaintext[i] in alfavit2:
            m = alfavit2.index(plaintext[i])
            ciphertext += alfavit2[(m + shift) % 26]
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
    plaintext = ""  # расшифровка
    alfavit1 = "abcdefghijklmnopqrstuvwxyz"
    alfavit2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(ciphertext)):
        if ciphertext[i] in alfavit1:
            m = alfavit1.index(ciphertext[i])
            plaintext += alfavit1[(m - shift) % 26]
        elif ciphertext[i] in alfavit2:
            m = alfavit2.index(ciphertext[i])
            plaintext += alfavit2[(m - shift) % 26]
        else:
            plaintext += ciphertext[i]

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    for best_shift in range(26):
        if decrypt_caesar(ciphertext) in dictionary:
            return best_shift
    return best_shift
