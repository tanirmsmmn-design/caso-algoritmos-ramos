Tania Mamani Ramos

# H3: comparacion medida, voraz contra dinamica

Problema analogo: elegir que productos reponer con un presupuesto limitado (mochila 0/1). Costos (1 a 20 Bs) y ganancias (1 a 40 Bs) de ejemplo, generados al azar con semilla fija. Presupuesto = 5 x n.

Medido en Python 3.13.7 en Windows. Protocolo: 1 calentamiento + 3 corridas + promedio.

| n productos | presupuesto | ganancia voraz | ganancia dinamica | voraz (ms) | voraz vs anterior | dinamica (ms) | dinamica vs anterior |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 100 | 500 | 1450 | 1450 | 0.047 | - | 9.9 | - |
| 200 | 1,000 | 3115 | 3115 | 0.072 | x1.5 | 45.6 | x4.6 |
| 400 | 2,000 | 6225 | 6228 | 0.155 | x2.1 | 218.2 | x4.8 |
| 800 | 4,000 | 12527 | 12528 | 0.326 | x2.1 | 789.7 | x3.6 |


## Conclusion

- **Calidad del resultado:** en el caso chico (presupuesto de Bs 10) el voraz dio 7 y la dinamica 10, asi que el voraz no siempre encuentra lo mejor. Con muchos productos casi empataron: con n = 400 dieron 6.225 y 6.228, y con n = 800 dieron 12.527 y 12.528 (una diferencia de 1 en mas de 12.000). La dinamica siempre da el mejor resultado.
- **Tiempo:** la dinamica crecio cerca de x4 cada vez que se duplico n (x4,6, x4,8 y x3,6), y el voraz cerca de x2 (x1,5, x2,1 y x2,1). Con n = 800 la dinamica tardo 789,7 ms contra 0,326 ms del voraz, unas 2.400 veces mas lenta.
- **Ruido:** los tiempos del voraz son menores a 1 ms, asi que sus cocientes varian (x1,5 a x2,1) por el ruido de la computadora. Los de la dinamica tambien variaron (x3,6 a x4,8). Por eso miro la tendencia y no un numero suelto.
- **Cual elijo para mi caso y por que:** elijo la programacion dinamica. En mi tienda decido que reponer una vez por semana, asi que tardar menos de un segundo no es problema, y me da siempre la mejor ganancia posible. Si tuviera que decidir muchas veces por minuto, o con cientos de miles de productos, usaria el voraz, porque queda muy cerca del optimo y es mucho mas rapido.
