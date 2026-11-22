# Eleccion argumentada del algoritmo de ordenamiento (clase 6)

Medido en: Python 3.13.7 en Windows, modo normal, protocolo: 1 calentamiento + 3 corridas + promedio.

Datos: 1,500 codigos de producto (el tamano de mi inventario).

## Datos al azar

| Algoritmo | tiempo (ms) |
|---|---:|
| Insercion (cuadratico) | 105.272 |
| MergeSort | 7.592 |
| QuickSort | 5.234 |
| sorted() de Python | 0.456 |

## Casi ordenados (inventario + 15 productos nuevos)

| Algoritmo | tiempo (ms) |
|---|---:|
| Insercion (cuadratico) | 2.358 |
| MergeSort | 4.257 |
| QuickSort | 8.157 |
| sorted() de Python | 0.032 |

## Mi eleccion

- **Algoritmo que elijo:** el sorted() de Python (la funcion de ordenamiento propia de mi lenguaje).

- **Por que (evidencia):**
  - Con datos al azar fue el mas rapido: 0,456 ms, contra 5,234 ms de QuickSort, 7,592 ms de MergeSort y 105,272 ms de la insercion. Es unas 230 veces mas rapido que la insercion.
  - Con datos casi ordenados, que es lo que pasa en mi inventario (casi siempre entran pocos productos nuevos), tambien fue el mas rapido: 0,032 ms contra 2,358 ms de la insercion, 4,257 ms de MergeSort y 8,157 ms de QuickSort.
  - En la practica c5 tambien gano en todos los tamanos (por ejemplo, 22,7 ms con 80.000 datos contra 366,5 ms de QuickSort y 488,0 ms de MergeSort).
  - La insercion mejora mucho cuando los datos ya estan casi ordenados (de 105 ms a 2,4 ms) y llega a ganarles a MergeSort y QuickSort en ese caso. Pero con datos al azar es la peor, y el sorted() le gana en los dos escenarios, asi que no me conviene.
  - Ademas, no tengo que escribir ni mantener mi propio algoritmo.

- **En que caso cambiaria mi decision:** Si usara otro lenguaje que no tenga una funcion de ordenamiento propia y rapida, elegiria MergeSort o QuickSort, porque en mis tablas con datos al azar fueron mucho mejores que la insercion. Si el inventario creciera a cientos de miles de productos, esa diferencia seria todavia mayor. Tambien volveria a medir si los datos cambiaran todo el tiempo, porque ordenar tiene un costo cada vez que se repite.
