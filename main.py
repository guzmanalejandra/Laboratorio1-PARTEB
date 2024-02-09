
import afin
import caesar
import vigenere

distribuciones_wikipedia = {
    'A': 12.53, 'B': 1.42, 'C': 4.68, 'D': 5.86, 'E': 13.68, 'F': 0.69,
    'G': 1.01, 'H': 0.70, 'I': 6.25, 'J': 0.44, 'K': 0.02, 'L': 4.97,
    'M': 3.15, 'N': 6.71, 'Ñ': 0.31, 'O': 8.68, 'P': 2.51, 'Q': 0.88,
    'R': 6.87, 'S': 7.98, 'T': 4.63, 'U': 3.93, 'V': 0.90, 'W': 0.01,
    'X': 0.22, 'Y': 0.90, 'Z': 0.52
}
alfabeto = "abcdefghijklmnñopqrstuvwxyz"

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    return contenido

    
def calcular_distribucion(texto):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    frecuencias = dict.fromkeys(alfabeto, 0)
    total_caracteres = 0

    texto = texto.lower().replace(" ", "")  
    for letra in texto:
        if letra in alfabeto:
            frecuencias[letra] += 1
            total_caracteres += 1

    for letra in frecuencias:
        frecuencias[letra] = (frecuencias[letra] / total_caracteres) * 100 if total_caracteres > 0 else 0

    return frecuencias


def ordenar_distribucion(distribucion):
    return dict(sorted(distribucion.items(), key=lambda x: x[1], reverse=True))


def filtrar_distribucion(distribucion):
    return {letra: frec for letra, frec in distribucion.items() if frec > 0}

def lado_a_lado(distribucion_ordenada, distribuciones_wikipedia):
    for letra, frec in distribucion_ordenada.items():
        frec_wikipedia = distribuciones_wikipedia.get(letra.upper(), 0)
        print(f"{letra.upper()}: {frec:.2f}% - Wikipedia: {frec_wikipedia:.2f}%")



def main():
    #cesar descomentar 
    # ruta_archivo_entrada = "cipher1.txt"
    # texto = leer_archivo(ruta_archivo_entrada)
    
    # k_mejores = caesar.descifrado_fuerza_bruta(texto, k=27) 
    
    # print("Los resultados del descifrado por fuerza bruta son:")
    # for desplazamiento, _ in k_mejores:
    #     print(f"Desplazamiento {desplazamiento}: {caesar.descifrado_cesar(texto, desplazamiento)}")
    # #afin
    ruta_archivo_entrada_afin = "cipher2.txt"
    texto_afin = leer_archivo(ruta_archivo_entrada_afin)
    k_mejores_afin = afin.ataque_fuerza_bruta_afin(texto_afin, alfabeto, k=5)
    print("\nLos resultados del descifrado por fuerza bruta Afín son:")
    for a, b, metrica, muestra in k_mejores_afin:
        print(f"Clave (a={a}, b={b}) con métrica {metrica}: {muestra}...")


if __name__ == "__main__":
    main()
    





