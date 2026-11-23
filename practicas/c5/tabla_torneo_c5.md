# Torneo de ordenamientos (clase 5)

Medido en: Python 3.13.7 en Windows, modo normal, protocolo: 1 calentamiento + 3 corridas + promedio.

Cada algoritmo ordeno la MISMA lista de numeros al azar, y verifique que el resultado quedara ordenado antes de medir. Entre parentesis: cuantas veces mas tardo respecto a la cantidad anterior (los datos se duplican en cada columna).

| Algoritmo | n = 10,000 | n = 20,000 | n = 40,000 | n = 80,000 |
|---|---:|---:|---:|---:|
| Insercion (cuadratico) | 5149.9 ms | 22656.8 ms (x4.4) | no medido | no medido |
| MergeSort | 48.5 ms | 100.5 ms (x2.1) | 209.9 ms (x2.1) | 488.0 ms (x2.3) |
| QuickSort | 34.5 ms | 75.6 ms (x2.2) | 162.0 ms (x2.1) | 366.5 ms (x2.3) |
| sorted() de Python | 1.8 ms | 9.4 ms (x5.1) | 9.9 ms (x1.1) | 22.7 ms (x2.3) |

Nota: la insercion no se midio con mas de 20,000 datos porque en Python tardaria demasiado (es cuadratica).

