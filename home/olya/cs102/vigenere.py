def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    for id in range(len(plaintext)):
       
        position = ord(plaintext[id])
        cur = plaintext[id]
        q = len(keyword)
        if ord(keyword[id % q]) >= ord('a') and ord(keyword[id % q]) <= ord('z'):
            k = ord(keyword[id % q]) - ord('a')
        else:
            k = ord(keyword[id % q]) - ord('A')

        k = k % 26

        if (ord('a') <= position and position <= ord('z')):
            z = ord('z')
            a = ord('a')
            if position + k > z:
                cur = chr(k - (z - position) + a - 1)
            else:
                cur = chr(k + position)
        elif (ord('A') <= position and position <= ord('Z')):
            z = ord('Z')
            a = ord('A')
            if position + k > z:
                cur = chr(k - (z - position) + a - 1)
            else:
                cur = chr(k + position)
        ciphertext += cur


    return ciphertext
"""print(encrypt_vigenere("PYTHON", "A"))"""
