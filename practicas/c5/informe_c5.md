# Informe de conclusiones - Torneo de ordenamientos (clase 5)

Medido en mi computadora con Python, con el protocolo del ingeniero (1 corrida de calentamiento, 3 corridas medidas y promedio). Cada algoritmo ordenó la misma lista de números al azar y verifiqué que el resultado quedara ordenado antes de medir.

## 1. Cuál fue el más rápido y cuál el más lento

El más rápido fue el sorted() de Python en todos los tamaños (por ejemplo, 22,7 ms con 80.000 datos). El más lento fue la inserción: con 20.000 datos tardó 22.656,8 ms, mientras que MergeSort tardó 100,5 ms y QuickSort 75,6 ms. Con 10.000 datos la inserción ya era unas 100 veces más lenta que MergeSort (5.149,9 ms contra 48,5 ms).

## 2. Qué pasa cuando los datos se duplican

- Inserción (O(n²)): al pasar de 10.000 a 20.000 datos, el tiempo se multiplicó por x4,4. Con el doble de datos tarda cerca de 4 veces más.
- MergeSort y QuickSort (O(n log n)): con cada duplicación el tiempo creció entre x2,1 y x2,3, un poco más del doble.
- Esto confirma la diferencia entre O(n²) y O(n log n): al crecer los datos, el algoritmo cuadrático se vuelve inusable. Por eso no medí la inserción con 40.000 y 80.000 datos: en Python habría tardado demasiado.
- El x5,2 del sorted() entre 10.000 y 20.000 datos se debe al ruido de la computadora, porque con tiempos tan chicos (1,8 ms) una pequeña variación cambia mucho el cociente. Lo importante es la tendencia, no un número suelto.

## 3. Comparación entre MergeSort, QuickSort y sorted()

QuickSort fue más rápido que MergeSort en todos los tamaños (con 80.000 datos, 366,5 ms contra 488,0 ms). Mi explicación es que MergeSort gasta tiempo en mezclar las mitades, y QuickSort ordena en el lugar sin combinar. Aun así, el sorted() de Python le ganó a los dos (22,7 ms con 80.000 datos, unas 16 veces más rápido que mi QuickSort). Creo que es porque está implementado en C y está muy optimizado, mientras que mis versiones están escritas en Python.

## 4. Cuál me conviene para mi caso (inventario de tienda)

Para mi inventario, que tiene unos 1.500 productos, elijo el sorted() de Python. Fue el más rápido en todos los tamaños de mi tabla, y no tengo que escribir ni mantener mi propio algoritmo. Con 1.500 datos las diferencias serían de pocos milisegundos, así que la inserción también podría servir, pero no gano nada usándola si hay una opción más rápida y más simple. Lo voy a confirmar con la medición de la práctica c6, usando datos con el tamaño de mi inventario.
