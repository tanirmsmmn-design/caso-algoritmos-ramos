import random, time
from bisect import bisect_left

N = 1_000_000
CONSULTAS = 1_000

datos = list(range(0, N * 2, 2))          # 1.000.000 de enteros ORDENADOS
claves = random.sample(datos, CONSULTAS)  # 1.000 claves que SI existen

def lineal(lista, clave):
    for i, x in enumerate(lista):
        if x == clave:
            return i
    return -1

def binaria(lista, clave):
    i = bisect_left(lista, clave)
    return i if i < len(lista) and lista[i] == clave else -1

def medir(funcion):
    t = time.perf_counter()
    for c in claves:
        funcion(datos, c)
    return (time.perf_counter() - t) * 1000  # ms

def promedio(funcion):
    medir(funcion)                       # calentamiento (no cuenta)
    tiempos = [medir(funcion) for _ in range(3)]
    return sum(tiempos) / 3

print("Midiendo... la lineal tarda un poco, espera.")
t_lin = promedio(lineal)
t_bin = promedio(binaria)

tabla = f"""# Taller c4: lineal contra binaria
Medido en Python, en mi computadora. {N:,} datos ordenados, {CONSULTAS:,} consultas.
Protocolo: 1 calentamiento + 3 corridas, promedio.

| Algoritmo | Tiempo promedio (ms) |
|-----------|----------------------|
| Lineal    | {t_lin:.1f} |
| Binaria   | {t_bin:.3f} |

Cociente (lineal / binaria): x{t_lin / t_bin:.0f}

## Mi proceso (inventario)
...
"""
open("tabla_c4.md", "w", encoding="utf-8").write(tabla)
print(tabla)
