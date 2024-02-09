# caesar cipher
import math

alfabeto = "abcdefghijklmnñopqrstuvwxyz"

distribuciones_wikipedia = {
    'A': 12.53, 'B': 1.42, 'C': 4.68, 'D': 5.86, 'E': 13.68, 'F': 0.69,
    'G': 1.01, 'H': 0.70, 'I': 6.25, 'J': 0.44, 'K': 0.02, 'L': 4.97,
    'M': 3.15, 'N': 6.71, 'Ñ': 0.31, 'O': 8.68, 'P': 2.51, 'Q': 0.88,
    'R': 6.87, 'S': 7.98, 'T': 4.63, 'U': 3.93, 'V': 0.90, 'W': 0.01,
    'X': 0.22, 'Y': 0.90, 'Z': 0.52
}


def cifrado_cesar(mensaje):
    mensaje = mensaje.lower()
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            indice_nuevo = indice + 3
            if indice_nuevo >= len(alfabeto):
                indice_nuevo = indice_nuevo - len(alfabeto)
            mensaje_cifrado = mensaje_cifrado + alfabeto[indice_nuevo]
        else:
            mensaje_cifrado = mensaje_cifrado + letra
    return mensaje_cifrado

def descifrado_cesar(mensaje, desplazamiento):
    mensaje = mensaje.lower()
    mensaje_descifrado = ""
    for letra in mensaje:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            indice_nuevo = indice - desplazamiento
            if indice_nuevo < 0:
                indice_nuevo += len(alfabeto)
            mensaje_descifrado += alfabeto[indice_nuevo]
        else:
            mensaje_descifrado += letra
    return mensaje_descifrado


def calcular_metrica(mensaje_descifrado, distribucion_referencia):
    mensaje_descifrado = ''.join(filter(str.isalpha, mensaje_descifrado.lower()))
    total_caracteres = len(mensaje_descifrado)
    
    frecuencias_descifrado = {letra: 0 for letra in alfabeto}
    for letra in mensaje_descifrado:
        if letra in frecuencias_descifrado:
            frecuencias_descifrado[letra] += 1
    

    for letra in frecuencias_descifrado:
        frecuencias_descifrado[letra] = (frecuencias_descifrado[letra] / total_caracteres) * 100 if total_caracteres > 0 else 0
    diferencia_total = 0
    for letra, frec in frecuencias_descifrado.items():
        diferencia = abs(frec - distribucion_referencia.get(letra.upper(), 0))
        diferencia_total += diferencia
    
    return diferencia_total


def descifrado_fuerza_bruta(mensaje_cifrado, k=3):
    resultados = []
    for desplazamiento in range(len(alfabeto)):
        mensaje_descifrado = ""
        for letra in mensaje_cifrado:
            if letra in alfabeto:
                indice = alfabeto.index(letra)
                indice_nuevo = indice - desplazamiento
                if indice_nuevo < 0:
                    indice_nuevo += len(alfabeto)
                mensaje_descifrado += alfabeto[indice_nuevo]
            else:
                mensaje_descifrado += letra
        metrica = calcular_metrica(mensaje_descifrado, distribuciones_wikipedia)
        resultados.append((desplazamiento, metrica))
    resultados.sort(key=lambda x: x[1], reverse=True)
    return resultados[:k]

