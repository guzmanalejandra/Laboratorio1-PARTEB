import math
import itertools
from math import gcd 

alfabeto = "abcdefghijklmnñopqrstuvwxyz"



def cifrado_afin(mensaje, a, b):
    mensaje = mensaje.lower()
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            indice_nuevo = (a * indice + b) % len(alfabeto)
            mensaje_cifrado += alfabeto[indice_nuevo]
        else:
            mensaje_cifrado += letra
    return mensaje_cifrado


def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def descifrar_afin(ciphertext, a, b, alfabeto=alfabeto):
    plaintext = ""
    m = len(alfabeto)
    a_inv = modinv(a, m)
    if a_inv is None:
        return None  
    for letra in ciphertext:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            indice_nuevo = (a_inv * (indice - b)) % m
            plaintext += alfabeto[indice_nuevo]
        else:
            plaintext += letra
    return plaintext

def encontrar_coprimos(n):
    return [a for a in range(2, n) if gcd(a, n) == 1]


def contar_palabras_comunes(texto, palabras_comunes):
    texto_palabras = texto.lower().split()
    contador = sum(palabra in texto_palabras for palabra in palabras_comunes)
    return contador

def ataque_fuerza_bruta_afin(ciphertext, alfabeto="abcdefghijklmnñopqrstuvwxyz", k=5):
    coprimos = encontrar_coprimos(len(alfabeto))
    resultados = []
    for a in coprimos:
        for b in range(len(alfabeto)):
            plaintext = descifrar_afin(ciphertext, a, b, alfabeto)
            if plaintext is not None:
                # Considera implementar una métrica más sofisticada aquí
                metrica = sum(plaintext.count(vocal) for vocal in 'aeiou')
                resultados.append((a, b, metrica, plaintext[:100]))
    resultados.sort(key=lambda x: x[2], reverse=True)
    return resultados[:k]




#print("Mensaje para cifrar:", mensaje)
#cifrar = cifrado_afin(mensaje, a, b)
#print("Mensaje cifrado:", cifrar)
#descifrar = descifrado_afin(cifrar, a, b)
#print("Mensaje descifrado:", descifrar)
