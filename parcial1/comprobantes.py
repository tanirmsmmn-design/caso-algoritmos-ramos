# Tania Mamani Ramos
# PARCIAL 1 - VARIANTE B: Registro de comprobantes (portado de C# a Python)
import random

# Solucion ACTUAL (lenta): comparar cada comprobante con todos los que le siguen.
def hay_repetidos_por_pares(comprobantes):
    for a in range(len(comprobantes)):
        for b in range(a + 1, len(comprobantes)):
            if comprobantes[a] == comprobantes[b]:
                return True
    return False

# MI CURA: recorrer una sola vez guardando lo ya visto en un conjunto (set).
# Si el comprobante ya estaba en el conjunto, esta repetido. No modifica la lista.
# Costo: O(n) en promedio (cada busqueda en el set es O(1)); memoria extra O(n).
def hay_repetidos_curado(comprobantes):
    vistos = set()
    for c in comprobantes:
        if c in vistos:
            return True
        vistos.add(c)
    return False

# El PEOR CASO para las dos: una lista SIN repetidos (hay que mirarlo todo).
def generar_sin_repetidos(n, semilla=77):
    datos = [1000 + i for i in range(n)]
    random.Random(semilla).shuffle(datos)
    return datos

CASOS = [
    ([1010, 1003, 1009, 1003, 1005], True,  "repetido en el medio"),
    ([1010, 1003, 1009, 1004, 1005], False, "sin repetidos"),
    ([],                             False, "lista vacia"),
    ([1008],                         False, "un solo elemento"),
    ([1004, 1001, 1002, 1006, 1004], True,  "repetido en los extremos"),
]

if __name__ == "__main__":
    ok = True
    for datos, esperado, que in CASOS:
        copia = list(datos)
        lenta = hay_repetidos_por_pares(datos)
        curada = hay_repetidos_curado(datos)
        bien = (curada == esperado) and (datos == copia)   # tambien verifica que no modifica la lista
        ok = ok and bien
        print(f"{que:<26} esperado {str(esperado):<5} | por pares {str(lenta):<5} | mi cura {str(curada):<5} | {'OK' if bien else 'MAL'}")
    print("Los 5 casos pasan." if ok else "HAY CASOS QUE FALLAN.")
