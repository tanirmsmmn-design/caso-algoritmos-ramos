# Practica clase 3 - Tabla de mediciones (busqueda lineal)

**Algoritmo medido:** busqueda lineal de un codigo de producto en una lista (peor caso: el codigo no existe, se revisa toda la lista).

**Lenguaje:** Python 3.13.7 | **Equipo:** Windows 11 (AMD64)

**Protocolo:** 1 corrida de calentamiento (descartada) + 5 corridas medidas + promedio. Datos escalados n, 4n, 16n. Mismas condiciones en todas las mediciones.

## Tabla de mediciones

| n (datos) | Corrida 1 (ms) | Corrida 2 | Corrida 3 | Corrida 4 | Corrida 5 | Promedio (ms) | Ratio vs anterior |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 100,000 | 4.73 | 4.76 | 4.66 | 4.78 | 4.76 | 4.74 | - |
| 400,000 | 21.62 | 20.50 | 20.69 | 22.24 | 20.85 | 21.18 | x4.5 |
| 1,600,000 | 81.85 | 77.43 | 82.02 | 78.81 | 76.30 | 79.28 | x3.7 |

## Observacion

Con datos x4, el tiempo subio en promedio x4.1 en cada salto. Si la busqueda lineal es O(n), se espera cerca de x4.

## Conclusion

- Mis ratios dieron cerca de x4: x4.5 y x3.7 (promedio cerca de x4.1).
- Entonces mi busqueda es O(n) porque tiene un solo ciclo que revisa todos los datos, y al multiplicar los datos por 4 el tiempo se multiplico por 4 aproximadamente.
- Esto se relaciona con mi proceso (busqueda en el inventario) porque en la tienda tambien se busca el producto fila por fila, asi que si el inventario crece, la busqueda tarda proporcionalmente mas.
