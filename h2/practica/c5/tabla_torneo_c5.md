# Torneo de ordenamientos (Clase 5)

**Medido en:** Python 3.13.7 en Windows, modo normal.  
**Protocolo:** 1 calentamiento + 3 corridas medidas + promedio.

Cada algoritmo ordenó la MISMA lista de números al azar y verifiqué que el resultado quedara ordenado antes de medir. Entre paréntesis se indica cuántas veces más tardó respecto a la cantidad anterior de datos (los datos se duplican en cada columna).

## Resultados de las mediciones

| Algoritmo | n = 10,000 | n = 20,000 | n = 40,000 | n = 80,000 |
|---|---:|---:|---:|---:|
| Inserción (cuadrático) | 5149.9 ms | 22656.8 ms (x4.4) | No medido | No medido |
| MergeSort | 48.5 ms | 100.5 ms (x2.1) | 209.9 ms (x2.1) | 488.0 ms (x2.3) |
| QuickSort | 34.5 ms | 75.6 ms (x2.2) | 162.0 ms (x2.1) | 366.5 ms (x2.3) |
| sorted() de Python | 1.8 ms | 9.4 ms (x5.1) | 9.9 ms (x1.1) | 22.7 ms (x2.3) |

**Nota:** La inserción no se midió con más de 20.000 datos porque en Python tardaría demasiado, debido a su complejidad cuadrática.
