Tania Mamani Ramos

# Parcial 1 - Variante B: eleccion

Datos: n = 250.000 codigos de producto, 8.000 consultas al dia ("esta este codigo registrado?"), memoria limitada (no se puede duplicar el listado). log2(250.000) es aproximadamente 18.

## Costo total aproximado de cada opcion (en operaciones)

| Opcion | Preparar (una vez) | Consultas | Total aproximado |
|---|---|---|---|
| 1. Recorrer el listado en cada consulta | 0 | 8.000 x 250.000 = 2 x 10^9 (peor caso) | **2 x 10^9** |
| 2. Ordenar con n log n + busqueda binaria | 250.000 x 18 = 4,5 x 10^6 | 8.000 x 18 = 1,4 x 10^5 | **unos 4,6 x 10^6** |
| 3. Ordenar con algoritmo cuadratico + busqueda binaria | 250.000^2 = 6,25 x 10^10 | 8.000 x 18 = 1,4 x 10^5 | **unos 6,25 x 10^10** |

La opcion 2 hace unas 430 veces menos trabajo que la 1 y unas 14.000 veces menos que la 3.

## Mi eleccion

**Opcion 2:** ordenar el listado una vez en la manana con un algoritmo n log n y usar busqueda binaria en cada consulta.

- Es la de menor costo total, con una diferencia enorme.
- La opcion 3 es la peor porque ordenar con un algoritmo cuadratico cuesta mas que todas las consultas juntas de la opcion 1.
- Como la memoria es limitada, el ordenamiento debe hacerse **en el mismo listado** (por ejemplo QuickSort, que casi no usa memoria extra). MergeSort no conviene aqui porque necesita una copia del listado.

Apoyo de mi medicion (P1.2): con n = 12.000, la solucion por pares tardo 2.695,23 ms y mi cura 0,818 ms, o sea unas 3.300 veces mas rapida. Esto confirma que pasar de O(n^2) a O(n) cambia el tiempo de forma enorme cuando n crece, que es la misma razon por la que en este almacen conviene ordenar una vez y buscar con busqueda binaria.

## A partir de cuantas consultas cambiaria de opinion

La opcion 1 cuesta q x n y la opcion 2 cuesta n log n + q log n, donde q es el numero de consultas. Se igualan cuando q es aproximadamente log2(n), unas **18 consultas** (unas 36 si cuento que la busqueda lineal encuentra el dato, en promedio, a la mitad del listado). Con menos de unas 18 consultas por manana convendria la opcion 1, porque no vale la pena pagar el ordenamiento; con 8.000 consultas conviene ampliamente la opcion 2.
