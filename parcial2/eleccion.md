Tania Mamani Ramos

# Parcial 2 - Variante A: eleccion de la estructura

## 1. Operaciones, estructura y costo

Uso dos estructuras a la vez: una **cola de prioridad (heap)** con tuplas (urgencia, llegada, nombre), y un **conjunto (set)** con los nombres que siguen en espera. La tupla incluye el numero de llegada, asi que si dos pacientes tienen la misma urgencia sale primero el que llego antes (desempate).

| Operacion | Veces en un dia | Estructura | Costo O |
|---|---:|---|---|
| Registrar | 100.000 | heap (push) + set (add) | O(log n) |
| AtenderSiguiente | 100.000 | heap (pop) + set (remove) | O(log n) |
| EstaEsperando | 30.000 | set | O(1) |
| Esperando | no se indica | tamano del set | O(1) |

## 2. Por que no sirve la lista simple (con n = 100.000)

Costo aproximado de un dia, contando comparaciones:

| Operacion | Lista simple | Mi estructura |
|---|---|---|
| Registrar | 100.000 x 1 = 1 x 10^5 | 100.000 x 17 = 1,7 x 10^6 |
| AtenderSiguiente | recorre toda la lista: unos n^2 / 2 = 5 x 10^9 | 100.000 x 17 = 1,7 x 10^6 |
| EstaEsperando | 30.000 x hasta 100.000 = hasta 3 x 10^9 | 30.000 x 1 = 3 x 10^4 |
| **Total aproximado** | **unos 8 x 10^9** | **unos 3,4 x 10^6** |

(17 es log2 de 100.000, redondeado.) La lista simple hace unas 2.000 veces mas trabajo. La causa es que AtenderSiguiente y EstaEsperando recorren la lista completa en cada llamada, lo que da O(n) por operacion y O(n^2) en el dia.

## 3. Condicion para cambiar de opinion

- Si hubiera muy pocos pacientes (por ejemplo, 20 en espera), la lista simple bastaria y seria mas facil de escribir: no hay que pagar la complejidad de dos estructuras por un ahorro minimo.
- Si el sistema permitiera cancelar a un paciente que esta esperando, el heap no puede sacar un elemento del medio de forma barata, y tendria que cambiar de estructura o usar eliminacion diferida.
