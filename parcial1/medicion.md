Tania Mamani Ramos

# Parcial 1 - Variante B: curar y medir

**Mi cura:** recorre la lista una sola vez guardando lo ya visto en un conjunto (set); si un comprobante ya estaba, hay repetido. No modifica la lista. Costo: O(n) en promedio (memoria extra O(n)).

Medido en Python 3.13.7 en Windows, en mi computadora, en el peor caso (lista sin repetidos). Protocolo: 1 corrida de calentamiento + 3 corridas medidas + promedio.

| n | Por pares (ms) | Por pares vs fila anterior | Mi cura (ms) | Mi cura vs fila anterior |
|---:|---:|---:|---:|---:|
| 1,500 | 40.46 | - | 0.138 | - |
| 3,000 | 172.05 | x4.3 | 0.149 | x1.1 |
| 6,000 | 691.81 | x4.0 | 0.837 | x5.6 |
| 12,000 | 2695.23 | x3.9 | 0.818 | x1.0 |


## Conclusion

- **Por pares:** al duplicar los datos, el tiempo se multiplico por x4,3, x4,0 y x3,9, cerca de x4. Coincide con O(n^2): dos ciclos anidados, asi que si n se duplica, el trabajo se multiplica por 4.
- **Mi cura:** sus cocientes fueron irregulares (x1,1, x5,6 y x1,0), pero de n = 1.500 a n = 12.000 (8 veces mas datos) el tiempo paso de 0,138 ms a 0,818 ms, unas 5,9 veces. Es compatible con O(n), aunque no se ve limpio.
- **Ruido:** si, hay ruido en los tiempos de mi cura, porque duran menos de 1 ms y una pequena variacion de la computadora cambia mucho el cociente. En la solucion por pares, con tiempos de cientos de milisegundos, el ruido casi no se nota.
- **Peor tiempo medido:** 2.695,23 ms (unos 2,7 s), de la solucion por pares con n = 12.000.
