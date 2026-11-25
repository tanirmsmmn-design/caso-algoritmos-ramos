Tania Mamani Ramos

# Evaluacion integradora (variante B): analisis

## a) Costo de CompradorIngenuo.Elegir

**O(n x 2^n).** El ciclo de afuera prueba todos los subconjuntos posibles de los n utiles: son 2^n (cada util se compra o no se compra). Por cada subconjunto, el ciclo de adentro recorre los n utiles para sumar su costo y su utilidad. Total: 2^n x n.

## b) La recursion "lo compro o no lo compro"

Cumple T(n) = 2 T(n-1) + 1.

**Por que no se aplica el teorema maestro de bolsillo:** ese teorema sirve para recurrencias donde el problema se **divide** en pedazos mas chicos, T(n) = a T(n/b) + n^d, con b mayor que 1. Aqui el problema solo se **achica en uno** (n-1), no se divide entre b, asi que no tiene la forma que el teorema exige.

**Cuanto cuesta:** se resuelve desarrollando. Cada nivel duplica las llamadas: 1, 2, 4, 8... y hay n niveles. La suma es 1 + 2 + 4 + ... + 2^(n-1) = 2^n - 1, asi que **T(n) = O(2^n)**. Es exponencial: cada util mas duplica el trabajo.

## c) Sirve un algoritmo voraz?

El voraz elegiria los utiles por **utilidad por Bs** (utilidad / costo), de mayor a menor, mientras quepan.

**Contraejemplo con el primer caso de las pruebas** (presupuesto 100 Bs):

| Util | Costo (Bs) | Utilidad | Utilidad por Bs |
|---|---:|---:|---:|
| U1 | 20 | 120 | 6,0 |
| U2 | 40 | 200 | 5,0 |
| U3 | 60 | 240 | 4,0 |

- **El voraz** compra U1 (cuesta 20, quedan 80), luego U2 (cuesta 40, quedan 40), y U3 ya no cabe (cuesta 60). Utilidad total: 120 + 200 = **320**.
- **El optimo** es U2 + U3: cuestan 40 + 60 = 100 Bs y dan 200 + 240 = **440**.
- 320 es menor que 440, asi que el voraz **no sirve**: elegir lo mejor en cada paso lo deja sin presupuesto para la mejor combinacion.

**Mi estrategia: programacion dinamica.**
- **Que se repite:** la recursion "lo compro o no lo compro" llega muchas veces a la misma pregunta: "cual es la maxima utilidad con un presupuesto de p Bs usando los primeros k utiles?". Se puede llegar a ese mismo (k, p) por muchos caminos distintos.
- **Por que funciona:** en lugar de recalcularla, se resuelve **una sola vez** y se guarda en una tabla, `mejor[p]`. Cada util se procesa una vez, y de mayor a menor presupuesto para no usarlo dos veces. Ademas se guarda una tabla de decisiones para reconstruir cuales utiles se eligieron.
- **Costo:** **O(n x P)**, donde P es el presupuesto en Bs: n utiles por P posiciones de la tabla. Memoria: O(n x P) por la tabla de decisiones.

## d) Estructura para EstaEnLaCompra

Un **conjunto (set)** con los codigos de los utiles elegidos. Preguntar si un codigo esta cuesta **O(1)** en promedio. Recorrer la lista de elegidos cuesta **O(k)**, donde k es la cantidad de utiles elegidos, y como se consulta miles de veces, el conjunto es mucho mejor.
