# Práctica 1: Búsqueda binaria a mano

## 1. Buscar el 31

Lista:
[8, 12, 19, 25, 31, 40, 47]

**Paso 1:** El número del medio es 25. Como 31 es mayor, buscamos a la derecha. Queda [31, 40, 47].

**Paso 2:** El número del medio es 40. Como 31 es menor, buscamos a la izquierda. Queda [31].

**Paso 3:** Encontramos el 31.

Resultado: 3 pasos.

## 2. Buscar el 5 (no existe)

Lista:
[8, 12, 19, 25, 31, 40, 47]

**Paso 1:** Revisamos 25. Como 5 es menor, vamos a la izquierda.

**Paso 2:** Revisamos 12. Como 5 es menor, vamos a la izquierda.

**Paso 3:** Revisamos 8. Como 5 es menor, vamos a la izquierda.

Ya no quedan números por revisar, por lo tanto, el 5 no existe en la lista.

Resultado: 3 pasos.

## 3. ¿Cuántos pasos como máximo para 1.000 y 1.000.000 de datos?

La búsqueda binaria divide la cantidad de datos por la mitad en cada paso.

- 1.000 datos: aproximadamente 10 pasos.
- 1.000.000 de datos: aproximadamente 20 pasos.

¿Por qué?

Porque en cada paso se elimina la mitad de los datos. Aunque la cantidad de datos aumente muchísimo, la cantidad de pasos aumenta muy poco.
