def encrypt_caesar(plaintext: str) -> str:
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
    # PUT YOUR CODE HERE
    for id in plaintext:

        if ('a' <= id <= 'z') or ('A' <= id <= 'Z'):
            if ('a' <= id <= 'w') or ('A' <= id <= 'W'):
                ans = chr(ord(id) + 3)
            else:
                ans = chr(ord(id) - 23)
        else:
            id += ans
        plaintext = plaintext.replace(id, ans)

    return plaintext

def decrypt_caesar(ciphertext: str) -> str:
    """
     >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
     >>> decrypt_caesar("sbwkrq")
     'python'
     >>> decrypt_caesar("Sbwkrq3.6")
     'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    for id in ciphertext:

        if ('a' <= id <= 'z') or ('A' <= id <= 'Z'):
            if ('c' <= id <= 'z') or ('C' <= id <= 'Z'):
                ans = chr(ord(id) - 3)
            else:
                ans = chr(ord(id) + 23)
        else:
            id += ans
        ciphertext = ciphertext.replace(id, ans)
    return ciphertext
