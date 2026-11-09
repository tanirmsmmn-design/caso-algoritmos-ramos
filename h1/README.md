# H1 - Mi proceso lento (caso integrador)

**Proceso:** Buscar un producto en el inventario de una tienda de barrio de El Alto a partir de su código, para consultar su precio y su stock.
**Quién lo sufre:** La persona que atiende la tienda y quien repone la mercadería.
**Cómo se hace hoy:** El inventario está en una planilla y, para cada código, se recorre la lista fila por fila hasta encontrarlo.
**Datos que maneja:** Aproximadamente 1.500 productos en el inventario y unas 80 consultas por día (valores estimados).
**Cuánto tarda hoy:** Entre 15 y 20 segundos por consulta (estimado), sobre todo cuando el producto está lejos en la lista y hay clientes esperando.
**Por qué es lento:** La búsqueda es lineal, así que cada producto nuevo que se agrega vuelve más lenta la búsqueda.
**Qué quiero optimizar:** Comparar la búsqueda lineal contra una búsqueda con hash (diccionario por código) y medir cuál tarda menos.
**Pruebas:** Como 1.500 productos es una lista pequeña, también probaré con listas más grandes de datos de ejemplo para ver cómo crece el tiempo si la tienda crece.
**Muestra de datos:** el archivo `inventario.csv` tiene 20 filas de ejemplo con el formato real (codigo, producto, categoria, precio_bs, stock). Los datos son de ejemplo.
**Lenguaje elegido:** Python.
