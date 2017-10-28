"""
加密算法模块
"""
# 维基百科：https://zh.wikipedia.org/wiki/Bcrypt
# pypi：https://pypi.python.org/pypi/bcrypt/3.1.0

import bcrypt

def check_hashpw(password, salt):
    password = password.encode()
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(salt))
    if bcrypt.checkpw(password, hashed):
        return True
    else:
        return False

def caesar_cipher(message, key):
    """
    凯特加密法
    :param message: 待加密数据
    :param key: 加密向量
    :return: 被加密的字符串
    """
    LEFTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ''
    message = message.upper()
    for symbol in message:
        if symbol in LEFTERS:
            num = LEFTERS.find(symbol)
            num = num + key

            if num >= len(LEFTERS):
                num = num - len(LEFTERS)
            elif num < 0:
                num = num + len(LEFTERS)

            translated = translated + LEFTERS[num]
        else:
            translated = translated + symbol

    return translated


def reverse_cipher(message):
    """
    反转加密法
    :param message: 待加密字符串
    :return: 被加密字符串
    """
    translated = ''

    i = len(message) - 1
    while i >= 0:
        translated = translated + message[i]
        i = i - 1

    return translated


def transposition_cipher(key, message):
    """
    换位加密法
    :param key: 数字Key
    :param message: 待加密字符串
    :return: 被加密数据
    """
    ciphertext = [''] * key
    ml = len(message)
    for col in range(key):
        pointer = col
        while pointer < ml:
            ciphertext[col] += message[pointer]
            pointer += key

    return ''.join(ciphertext)


if __name__ == '__main__':
    passwd = '123456'
    b = check_hashpw(passwd, 14)
    print(b)
