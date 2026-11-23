Tania Mamani Ramos

# H2: medicion de la estructura de mi caso

Mismo problema para las dos estructuras: cargar n productos (codigo de 13 digitos), hacer n consultas por codigo y borrar n/10 productos. Datos de ejemplo con el formato de mi inventario.csv.

Medido en Python 3.13.7 en Windows. Protocolo: 1 calentamiento + 3 corridas + promedio.

| n productos | Lista simple (ms) | Lista vs fila anterior | Diccionario (ms) | Diccionario vs fila anterior |
|---:|---:|---:|---:|---:|
| 2,000 | 146.35 | - | 1.702 | - |
| 4,000 | 570.99 | x3.9 | 3.376 | x2.0 |
| 8,000 | 2284.70 | x4.0 | 6.907 | x2.0 |
| 16,000 | 10423.29 | x4.6 | 14.969 | x2.2 |

## Conclusion

- **Lista simple:** al duplicar los productos, el tiempo se multiplico por x3,9, x4,0 y x4,6, cerca de x4. Coincide con O(n^2): hago n consultas y cada una puede recorrer hasta n productos, asi que si n se duplica el trabajo se multiplica por 4.
- **Diccionario:** al duplicar los productos, el tiempo se multiplico por x2,0, x2,0 y x2,2, cerca de x2. Coincide con O(n) en total: hago n operaciones y cada una cuesta O(1) en promedio, asi que si n se duplica el trabajo se duplica.
- **Ruido:** hay un poco de ruido. El x4,6 de la lista queda algo por encima de x4, y los tiempos del diccionario son de pocos milisegundos, donde una pequena variacion de la computadora cambia el cociente. Por eso miro la tendencia y no un numero suelto.
- **Para mi tienda:** con 16.000 productos la lista tardo 10.423 ms y el diccionario 14,97 ms, unas 700 veces mas rapido. Mi inventario es mas chico (unos 1.500 productos), pero la diferencia crece al aumentar los datos, asi que el diccionario es la estructura adecuada para buscar por codigo.
