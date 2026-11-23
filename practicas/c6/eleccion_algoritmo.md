Tania Mamani Ramos

# Eleccion argumentada del algoritmo de ordenamiento (clase 6)

## 1. Mi proceso y sus datos

Proceso: buscar un producto por su codigo en el inventario de una tienda de barrio de El Alto (mi H1).

- Hoy: unos 1.500 productos y unas 80 consultas por dia (estimado, como en mi H1).
- En el peor mes (por ejemplo, diciembre, con mas clientes y mas productos de temporada): unos 2.000 productos y unas 150 consultas por dia (estimado, como en mi H1).
- Los productos nuevos entran de a pocos, asi que la lista casi siempre queda casi ordenada.

## 2. La operacion que mas pesa

Ordenar el inventario cada vez que entran productos nuevos, porque la busqueda binaria necesita datos ordenados. Buscar con binaria es barato: con 1.500 productos son unos 11 pasos como maximo.

## 3. Dos candidatos

| Candidato | O en el peor caso | Nota |
|---|---|---|
| Insercion | O(n^2) | muy buena cuando los datos ya estan casi ordenados |
| sorted() de Python | O(n log n) | es el ordenamiento propio de mi lenguaje |

## 4. Mi eleccion y por que

Elijo **sorted() de Python**.

Medido con 1.500 codigos de producto (Python 3.13.7, Windows, 1 calentamiento + 3 corridas + promedio):

### Datos al azar

| Algoritmo | tiempo (ms) |
|---|---:|
| Insercion (cuadratico) | 105.272 |
| MergeSort | 7.592 |
| QuickSort | 5.234 |
| sorted() de Python | 0.456 |

### Casi ordenados (inventario + 15 productos nuevos)

| Algoritmo | tiempo (ms) |
|---|---:|
| Insercion (cuadratico) | 2.358 |
| MergeSort | 4.257 |
| QuickSort | 8.157 |
| sorted() de Python | 0.032 |

- Con datos al azar, sorted() fue unas 230 veces mas rapido que la insercion (0,456 ms contra 105,272 ms).
- Con datos casi ordenados, que es lo que pasa en mi inventario, tambien fue el mas rapido (0,032 ms contra 2,358 ms de la insercion). La insercion mejora mucho en ese caso, pero sorted() sigue ganando.
- En la practica c5 tambien gano en todos los tamanos (22,7 ms con 80.000 datos contra 366,5 ms de QuickSort y 488,0 ms de MergeSort).
- Ademas, no tengo que escribir ni mantener mi propio algoritmo.

## 5. Como lo medi

- Tamano: 1.500 datos, el tamano de mi inventario, en dos escenarios (al azar y casi ordenados).
- Protocolo: 1 corrida de calentamiento descartada, 3 corridas medidas y promedio.
- Cada algoritmo recibio una copia de la misma lista.

## Cuando cambiaria mi decision

Si usara un lenguaje sin una funcion de ordenamiento propia y rapida, elegiria MergeSort o QuickSort, porque con datos al azar fueron mucho mejores que la insercion. Si el inventario creciera a cientos de miles de productos, la diferencia seria todavia mayor. Tambien volveria a medir si los datos cambiaran todo el tiempo, porque ordenar cuesta cada vez que se repite.
