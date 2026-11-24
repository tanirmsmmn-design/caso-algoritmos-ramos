Tania Mamani Ramos

# Caso: busqueda de productos en el inventario de una tienda de barrio de El Alto

## Mi proceso

Busco un producto por su codigo en el inventario de una tienda de barrio, para consultar su precio y su stock. La persona que atiende la tienda lo sufre, sobre todo cuando hay clientes esperando.

- Datos: unos 1.500 productos y unas 80 consultas por dia (estimado).
- Hoy tarda entre 15 y 20 segundos por consulta (estimado), porque se recorre la lista fila por fila: es una busqueda lineal, O(n).
- Lenguaje: Python.


## Donde esta cada entrega

| Que | Carpeta |
|---|---|
| H1: mi proceso y datos de muestra | [h1/](h1/) |
| Practicas de las clases 3, 4, 5 y 6 | [practicas/](practicas/) |
| H2: la estructura de mi caso | [hitos/h2/](hitos/h2/) |
| H3: voraz contra dinamica | [hitos/h3/](hitos/h3/) |
| Parcial 1 | [parcial1/](parcial1/) |
| Parcial 2 | [parcial2/](parcial2/) |



## Mi caso como grafo

Mi operacion principal (buscar un producto por codigo) no necesita un grafo: se resuelve mejor con un diccionario. Pero mi caso se puede modelar asi:

- **Nodos:** los productos del inventario.
- **Aristas:** une dos productos que se compran juntos en la misma venta (por ejemplo, fideo y salsa). El peso de la arista seria cuantas veces se compraron juntos.

Serviria para ubicar productos cercanos en la tienda o para sugerir que reponer juntos. No lo implemente porque mi inventario no registra ventas por cliente.
