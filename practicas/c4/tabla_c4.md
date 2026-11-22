# Taller C4: Lineal contra binaria

Medido en Python, en mi computadora. 1.000.000 datos ordenados, 1.000 consultas.

**Protocolo:** 1 calentamiento + 3 corridas, promedio.

## Tabla de resultados

| Algoritmo | Tiempo promedio (ms) |
|---|---:|
| Lineal | 41443.0 |
| Binaria | 3.178 |

**Cociente (lineal / binaria):** x13042

## Justificación aplicada a mi proceso (Inventario)

En mi caso de inventario (aproximadamente 1.500 productos y 80 consultas diarias), sí conviene mantener los datos ordenados y usar búsqueda binaria cuando se realizan búsquedas repetidas sobre el catálogo, ya que el ordenamiento se realiza una vez o al actualizar los datos y luego las consultas son mucho más ágiles. En volúmenes grandes, la diferencia es considerable, como se demostró en mi prueba con 1.000.000 de datos, donde la búsqueda binaria fue x13042 más rápida en tiempo promedio.

Sin embargo, la búsqueda binaria exige que los datos estén ordenados. Si ingresan productos nuevos, hay que reordenar los datos o insertarlos manteniendo el orden. Si tuviera que elegir entre burbuja e inserción para ordenar, preferiría inserción porque suele requerir menos operaciones en conjuntos pequeños o parcialmente ordenados. En cambio, para volúmenes muy altos, ambos métodos cuadráticos resultan costosos.

