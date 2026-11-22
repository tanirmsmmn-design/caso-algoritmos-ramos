Tania Mamani Ramos

# Parcial 2 - Variante A: medicion

Medido en Python 3.13.7 en Windows, en mi computadora. Funcion de carga: n pacientes llegan y luego se atiende a los n. Protocolo: 1 corrida de calentamiento + 3 corridas medidas + promedio.

| n (pacientes) | Ingenua (ms) | Ingenua vs fila anterior | Mejorada (ms) | Mejorada vs fila anterior |
|---:|---:|---:|---:|---:|
| 2,000 | 699.7 | - | 4.4 | - |
| 4,000 | 2631.0 | x3.8 | 14.9 | x3.4 |
| 8,000 | 9984.0 | x3.8 | 18.4 | x1.2 |


## Conclusion

- **Ingenua:** al duplicar los pacientes, el tiempo se multiplico por x3,8 las dos veces (de 699,7 ms a 2.631,0 ms y a 9.984,0 ms). Se espera cerca de x4 si es O(n^2), asi que se comporta como declare: AtenderSiguiente recorre toda la lista en cada llamada, y si n se duplica el trabajo se multiplica por 4.
- **Mejorada:** al duplicar los pacientes, los cocientes fueron x3,4 y x1,2, que no se ven limpios. Mirando de 2.000 a 8.000 pacientes (4 veces mas datos), el tiempo paso de 4,4 ms a 18,4 ms, unas 4,2 veces mas, lo que es compatible con O(n log n) (un poco mas de x4 para 4 veces mas datos). Con 8.000 pacientes la mejorada tardo 18,4 ms contra 9.984,0 ms de la ingenua, unas 540 veces mas rapida.
- **Ruido:** los tiempos de la mejorada son de pocos milisegundos, y por eso sus cocientes saltan de una fila a otra (x3,4 y x1,2) y cambiaron entre mis corridas. El ruido de la computadora pesa mas cuando el tiempo es tan chico. Por eso miro la tendencia general y no un numero suelto.
