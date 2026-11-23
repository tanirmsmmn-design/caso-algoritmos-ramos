# Tania Mamani Ramos
# H2: La estructura de mi caso (inventario de una tienda de barrio de El Alto)
import random

# ---------- ESTRUCTURA INGENUA: lista simple ----------
class InventarioIngenuo:
    def __init__(self):
        self._lista = []                                  # cada elemento: (codigo, producto, precio_bs, stock)

    def insertar(self, codigo, producto, precio, stock):  # O(1): se agrega al final
        self._lista.append((codigo, producto, precio, stock))

    def buscar(self, codigo):                             # O(n): recorre producto por producto
        for item in self._lista:
            if item[0] == codigo:
                return item
        return None

    def borrar(self, codigo):                             # O(n): busca y luego desplaza los siguientes
        for i in range(len(self._lista)):
            if self._lista[i][0] == codigo:
                del self._lista[i]
                return True
        return False

    def __len__(self):
        return len(self._lista)

# ---------- ESTRUCTURA ADECUADA: diccionario (tabla hash) por codigo ----------
class InventarioDiccionario:
    def __init__(self):
        self._d = {}                                      # clave: codigo -> (producto, precio_bs, stock)

    def insertar(self, codigo, producto, precio, stock):  # O(1) en promedio
        self._d[codigo] = (producto, precio, stock)

    def buscar(self, codigo):                             # O(1) en promedio
        return self._d.get(codigo)

    def borrar(self, codigo):                             # O(1) en promedio
        return self._d.pop(codigo, None) is not None

    def __len__(self):
        return len(self._d)

# ---------- Datos de ejemplo con el formato de mi inventario.csv ----------
def generar_codigos(n, semilla=2026):
    rnd = random.Random(semilla)
    codigos = set()
    while len(codigos) < n:
        codigos.add("775" + str(rnd.randint(10**9, 10**10 - 1)))   # codigo de 13 digitos
    codigos = sorted(codigos)
    rnd.shuffle(codigos)
    return codigos

# ---------- Carga: el MISMO problema para las dos estructuras ----------
# 1) se cargan n productos, 2) se hacen n consultas por codigo (todos existen), 3) se borran n/10 productos.
def ejecutar_carga(inventario, codigos):
    n = len(codigos)
    for i, c in enumerate(codigos):
        inventario.insertar(c, "Producto " + str(i), 5.0 + i % 50, i % 100)
    encontrados = 0
    for c in codigos:
        if inventario.buscar(c) is not None:
            encontrados += 1
    for c in codigos[: n // 10]:
        inventario.borrar(c)
    return encontrados, len(inventario)

if __name__ == "__main__":
    cods = generar_codigos(500)
    a = ejecutar_carga(InventarioIngenuo(), cods)
    b = ejecutar_carga(InventarioDiccionario(), cods)
    print("Ingenua:", a, "| Diccionario:", b)
    assert a == b, "las dos estructuras deben dar el mismo resultado"
    print("Las dos estructuras dan el mismo resultado: OK")
