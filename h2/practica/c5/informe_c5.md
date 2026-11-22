# Informe de conclusiones - Torneo de ordenamientos (Clase 5)

Medí los tiempos en mi computadora con Python, siguiendo el protocolo del ingeniero: 1 corrida de calentamiento, 3 corridas medidas y el cálculo del promedio. Cada algoritmo ordenó la misma lista de números aleatorios y verifiqué que el resultado estuviera correctamente ordenado antes de medir.

## 1. ¿Cuál fue el más rápido y cuál el más lento?

El algoritmo más rápido fue `sorted()` de Python en todos los tamaños de datos, por ejemplo, con 80.000 datos tardó 22,7 ms.

El algoritmo más lento fue el de inserción. Con 20.000 datos tardó 22.656,8 ms, mientras que MergeSort tardó 100,5 ms y QuickSort 75,6 ms. Con 10.000 datos, la inserción ya era aproximadamente 100 veces más lenta que MergeSort (5.149,9 ms contra 48,5 ms).

## 2. ¿Qué pasa cuando los datos se duplican?

- **Inserción (O(n²)):** al pasar de 10.000 a 20.000 datos, el tiempo se multiplicó por 4,4. Es decir, con el doble de datos tarda aproximadamente 4 veces más.
- **MergeSort y QuickSort (O(n log n)):** con cada duplicación, el tiempo creció entre 2,1 y 2,3 veces, un poco más del doble.

Esto confirma la diferencia entre O(n²) y O(n log n). A medida que crece la cantidad de datos, el algoritmo cuadrático se vuelve cada vez más lento y poco práctico.

Por esta razón, no medí la inserción con 40.000 y 80.000 datos, porque en Python habría tardado demasiado.

El incremento de x5,2 de `sorted()` entre 10.000 y 20.000 datos se debe probablemente al ruido de la computadora, porque con tiempos tan pequeños (1,8 ms) una variación puede cambiar mucho el cociente. Lo importante es observar la tendencia general y no un número aislado.

## 3. Comparación entre MergeSort, QuickSort y sorted()

QuickSort fue más rápido que MergeSort en todos los tamaños. Con 80.000 datos, QuickSort tardó 366,5 ms, mientras que MergeSort tardó 488,0 ms.

Considero que esto se debe a que MergeSort necesita dividir los datos y luego combinar las mitades ordenadas, mientras que QuickSort realiza el ordenamiento utilizando particiones.

Sin embargo, `sorted()` de Python superó a ambos, tardando solamente 22,7 ms con 80.000 datos, aproximadamente 16 veces menos que mi implementación de QuickSort.

Esto probablemente se debe a que `sorted()` está implementado en C y altamente optimizado, mientras que mis versiones de los algoritmos están escritas en Python.

## 4. ¿Cuál me conviene para mi caso (inventario de tienda)?

Para mi inventario, que tiene aproximadamente 1.500 productos, elegiría `sorted()` de Python.

Fue el algoritmo más rápido en todos los tamaños de mi tabla y, además, me permite utilizar una función ya implementada, sin necesidad de escribir ni mantener mi propio algoritmo de ordenamiento.

Con 1.500 datos, las diferencias de tiempo probablemente serían de pocos milisegundos, por lo que el algoritmo de inserción también podría funcionar. Sin embargo, no tendría ventajas frente a `sorted()`, que es más rápido y sencillo de utilizar.

Finalmente, confirmaré esta elección con la medición de la práctica C6, utilizando datos del tamaño real de mi inventario.
