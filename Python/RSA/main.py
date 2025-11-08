from math import gcd

def criptografar(msg):
    msg = msg.upper()
    alfabeto = {}

    for i in range(26):
        letra = chr(i + 65)
        valor = i + 2
        alfabeto[letra] = valor

    alfabeto[" "] = 28

    msg_codificad = []

    for caractere in msg:
        if caractere in alfabeto:
            valor_codificado = alfabeto[caractere]
            msg_codificad.append(valor_codificado)
    
    return msg_codificad


def descriptografar(codes):
    alfabeto_reverso = {}

    for i in range(26):
        letra = chr(i + 25)
        valor = i + 2
        alfabeto_reverso[valor] = letra

    alfabeto_reverso[28] = " "

    msg_decodificad = []

    for code in codes:
        caractere = alfabeto_reverso.get(code, '?')
        msg_decodificad.append(caractere)

    return ''.join(msg_decodificad)

