Tania Mamani Ramos

# Parcial 1 - Variante B: analisis

## a) Cuatro fragmentos (costo O en el peor caso)

| Fragmento | Costo O | Justificacion (una linea) |
|---|---|---|
| F1 | O(n) | Un solo ciclo que recorre los n datos, y dentro hace trabajo constante (un if y una suma). |
| F2 | O(n^2) | Un ciclo dentro de otro, cada uno de n vueltas: n x n = n^2 comparaciones. |
| F3 | O(log n) | k se duplica en cada vuelta (1, 2, 4, 8...), asi que llega a n en unas log2(n) vueltas. |
| F4 | O(n log n) | El ciclo de afuera da n vueltas, y por cada una el ciclo de adentro divide k entre 3 hasta llegar a 1, unas log3(n) vueltas: n x log n. |

## b) Dos recurrencias (teorema maestro de bolsillo, T(1) = 1)

La forma general es T(n) = a T(n/b) + n^d. Se compara a con b^d:
- si a < b^d, el resultado es O(n^d);
- si a = b^d, el resultado es O(n^d log n);
- si a > b^d, el resultado es O(n^(log_b a)).

**(i) T(n) = 4 T(n/3) + n**
- a = 4, b = 3, d = 1, entonces b^d = 3.
- Comparacion: a = 4 es mayor que b^d = 3.
- Forma: T(n) = O(n^(log_3 4)), que es aproximadamente O(n^1,26).

**(ii) T(n) = 2 T(n/2) + n^2**
- a = 2, b = 2, d = 2, entonces b^d = 4.
- Comparacion: a = 2 es menor que b^d = 4.
- Forma: T(n) = O(n^2).
