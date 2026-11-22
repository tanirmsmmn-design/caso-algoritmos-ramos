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

**¿Conviene ordenar primero? Sí, con una advertencia.** Mi inventario tiene unos 1.500 productos y se consulta unas 80 veces al día sobre los mismos datos. Ordenar una sola vez y usar binaria baja cada consulta de hasta 1.500 comparaciones a unos 11 pasos, y con 1.000.000 de datos la binaria fue x13042 más rápida (3,178 ms contra 41.443 ms en 1.000 consultas). Con solo 1.500 productos la diferencia en segundos es pequeña, pero crece si el inventario crece.

**Costo y límite:** la binaria exige datos ordenados, y ordenar cuesta (esta tabla no lo incluye porque se paga una sola vez). Si entran productos nuevos hay que reordenar o insertarlos en su lugar. Para ordenar elegiría inserción y no burbuja, porque con datos casi ordenados (el inventario más unos pocos productos nuevos) hace pocas operaciones, como medí en c6.

