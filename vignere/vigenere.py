import math 

alfabeto = "abcdefghijklmnñopqrstuvwxyz"

def cifrado_vignere(mensaje, llave):
    mensaje = mensaje.lower()
    llave = llave.lower()
    mensaje_cifrado = ""
    llave_index = 0

    for letra in mensaje:
        if letra in alfabeto:
            indice_mensaje = alfabeto.index(letra)
            indice_llave = alfabeto.index(llave[llave_index % len(llave)])
            indice_nuevo = (indice_mensaje + indice_llave) % len(alfabeto)
            mensaje_cifrado += alfabeto[indice_nuevo]
            llave_index += 1
        else:
            mensaje_cifrado += letra

    return mensaje_cifrado

def descifrado_vigenere(mensaje_cifrado, llave):
    mensaje_cifrado = mensaje_cifrado.lower()
    llave = llave.lower()
    mensaje_descifrado = ""
    llave_index = 0

    for letra in mensaje_cifrado:
        if letra in alfabeto:
            indice_mensaje = alfabeto.index(letra)
            indice_llave = alfabeto.index(llave[llave_index % len(llave)])
            indice_nuevo = (indice_mensaje - indice_llave) % len(alfabeto)
            mensaje_descifrado += alfabeto[indice_nuevo]
            llave_index += 1
        else:
            mensaje_descifrado += letra

    return mensaje_descifrado

3


#mensaje_cifrado = cifrado_vignere("covercover", "thankyou")
#print("Mensaje cifrado:", mensaje_cifrado)
#mensaje_descifrado = descifrado_vigenere(mensaje_cifrado, "thankyou")
#print("Mensaje descifrado:", mensaje_descifrado)
