Tania Mamani Ramos

# Evaluacion integradora (variante B): medicion

Medido en Python 3.13.7 en Windows, en mi computadora. Funcion de carga: n utiles al azar (semilla fija) y presupuesto igual a un tercio del costo total. Protocolo: 1 corrida de calentamiento + 3 corridas medidas + promedio. En cada tamano verifique que las dos soluciones dan la misma utilidad.

## Tabla (cuatro tamanos n, n+2, n+4, n+6)

| n utiles | utilidad (igual en las dos) | Ingenua (ms) | Ingenua vs fila anterior | Mejorada (ms) | Mejorada vs fila anterior |
|---:|---:|---:|---:|---:|---:|
| 14 | 498 | 27.5 | - | 0.153 | - |
| 16 | 548 | 212.7 | x7.7 | 0.247 | x1.6 |
| 18 | 527 | 878.9 | x4.1 | 0.493 | x2.0 |
| 20 | 542 | 2862.0 | x3.3 | 0.359 | x0.7 |

## Mi solucion con 1.000 utiles y presupuesto 10.000

Tiempo (protocolo de siempre): **1129 ms** (utilidad maxima obtenida: 35040). La ingenua no se puede medir con 1.000 utiles: tendria que probar 2^1000 combinaciones.

## Que pasaria con presupuesto de 1.000.000.000 de Bs

Mi solucion cuesta O(n x P), donde P es el presupuesto, porque llena una tabla con una columna por cada boliviano de presupuesto. Con P = 10^9 y n = 1.000:

- **Tiempo:** unas 10^12 operaciones. Es 100.000 veces mas trabajo que el caso de P = 10.000 (10^9 contra 10^4), asi que si ese caso tardo 1.13 s, este tardaria unas 31 horas en mi computadora.
- **Memoria:** el arreglo de utilidades tendria 10^9 posiciones (varios gigabytes) y la tabla de decisiones unos 10^12 bytes (un terabyte). No cabe en una computadora normal.
- **Por que:** la dinamica depende del VALOR del presupuesto, no de cuantos utiles hay. Es un costo "pseudo-polinomial": rapido con presupuestos chicos y inviable con presupuestos enormes.
- **Que haria:** si el presupuesto es mayor o igual a la suma de todos los costos, se compra todo y no hace falta resolver nada; y para presupuestos grandes que si limitan, se puede hacer la tabla sobre la utilidad en vez de sobre el presupuesto, que es mucho mas chica.

## Conclusion

- **Ingenua:** al subir n de 2 en 2, el tiempo se multiplico por x7,7, x4,1 y x3,3. Esperaba cerca de x4,5 si es O(n x 2^n): cada +2 hay 4 veces mas combinaciones y cada una recorre un poco mas de utiles. Los dos ultimos cocientes se acercan; el x7,7 del inicio se debe al ruido, porque con solo 27 ms una pequena variacion cambia mucho el cociente.
- **Mejorada:** sus cocientes fueron x1,6, x2,0 y x0,7, irregulares, porque tarda menos de 1 ms y ahi el ruido de la computadora pesa mas que el crecimiento real. El x0,7 lo demuestra: con mas datos no puede tardar menos. Con presupuesto proporcional a n, su costo O(n x P) crece despacio, y con 1.000 utiles y presupuesto 10.000 tardo 1.129 ms.
- **Ruido:** hay ruido en los tiempos chicos de las dos soluciones, sobre todo en la mejorada. Por eso miro la tendencia general y no un cociente suelto.
- **Peor tiempo medido:** 2.862,0 ms, de la ingenua con n = 20. Con cada +2 se multiplica por cerca de 4, asi que con n = 40 tardaria unos 2.862 ms x 4^10, o sea mas de un mes. La mejorada, en cambio, resuelve 1.000 utiles en poco mas de un segundo.
