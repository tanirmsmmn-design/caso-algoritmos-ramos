# Tania Mamani Ramos
# EVALUACION INTEGRADORA - VARIANTE B: Compras de una escuela (portado de C# a Python)
import random
from collections import namedtuple

Util = namedtuple("Util", "codigo costo utilidad")

# ---------- SOLUCION INGENUA: prueba todos los subconjuntos (2^n) ----------
class CompradorIngenuo:
    def __init__(self):
        self._elegidos = []

    def elegir(self, utiles, presupuesto):
        n, mejor, mejor_mascara = len(utiles), 0, 0
        for mascara in range(1 << n):
            costo = utilidad = 0
            for i in range(n):
                if mascara & (1 << i):
                    costo += utiles[i].costo
                    utilidad += utiles[i].utilidad
            if costo <= presupuesto and utilidad > mejor:
                mejor, mejor_mascara = utilidad, mascara
        self._elegidos = [utiles[i].codigo for i in range(n) if mejor_mascara & (1 << i)]
        return mejor, list(self._elegidos)

    def esta_en_la_compra(self, codigo):          # recorre la lista: O(k)
        return codigo in self._elegidos

# ---------- MI SOLUCION: programacion dinamica (mochila 0/1) + conjunto ----------
class CompradorMejorado:
    def __init__(self):
        self._set = set()                          # codigos elegidos: consulta O(1)

    def elegir(self, utiles, presupuesto):
        self._set = set()
        if presupuesto < 0 or not utiles:
            return 0, []
        n = len(utiles)
        # mejor[p] = maxima utilidad posible con presupuesto p (cada subproblema se resuelve una sola vez)
        mejor = [0] * (presupuesto + 1)
        # tomar[i][p] = 1 si, al considerar el util i con presupuesto p, conviene comprarlo (sirve para reconstruir)
        tomar = [bytearray(presupuesto + 1) for _ in range(n)]
        for i in range(n):
            costo, util, fila = utiles[i].costo, utiles[i].utilidad, tomar[i]
            for p in range(presupuesto, costo - 1, -1):      # de mayor a menor: cada util se usa una sola vez
                v = mejor[p - costo] + util
                if v > mejor[p]:
                    mejor[p] = v
                    fila[p] = 1
        # reconstruir: de atras hacia adelante, siguiendo las decisiones
        elegidos, p = [], presupuesto
        for i in range(n - 1, -1, -1):
            if tomar[i][p]:
                elegidos.append(utiles[i].codigo)
                p -= utiles[i].costo
        self._set = set(elegidos)
        return mejor[presupuesto], elegidos

    def esta_en_la_compra(self, codigo):          # O(1)
        return codigo in self._set

def lote(*datos):
    return [Util(c, costo, u) for c, costo, u in datos]

# (que, utiles, presupuesto, utilidad esperada, codigos esperados) - todos con optimo unico
CASOS = [
    ("el voraz se equivoca", lote(("U1", 20, 120), ("U2", 40, 200), ("U3", 60, 240)), 100, 440, ["U2", "U3"]),
    ("cuatro utiles",        lote(("U1", 4, 6), ("U2", 6, 8), ("U3", 8, 10), ("U4", 10, 12)), 16, 20, ["U2", "U4"]),
    ("presupuesto cero",     lote(("U1", 5, 10), ("U2", 7, 12)), 0, 0, []),
    ("sin utiles",           lote(), 30, 0, []),
    ("nada cabe",            lote(("U1", 80, 90), ("U2", 100, 100)), 60, 0, []),
    ("entran todos",         lote(("U1", 10, 20), ("U2", 14, 24), ("U3", 6, 8)), 200, 52, ["U1", "U2", "U3"]),
]

def probar(titulo, fabrica):
    bien = total = 0
    for que, utiles, presupuesto, esperada, codigos in CASOS:
        utilidad, elegidos = fabrica().elegir(utiles, presupuesto)
        total += 1
        if utilidad == esperada and sorted(elegidos) == sorted(codigos):
            bien += 1
        else:
            print(f"   MAL en '{que}': esperado {esperada} con {codigos}, obtuvo {utilidad} con {elegidos}")
    c = fabrica()
    c.elegir(CASOS[0][1], CASOS[0][2])
    total += 2
    if c.esta_en_la_compra("U2"): bien += 1
    else: print("   MAL en esta_en_la_compra(U2): esperado True")
    if not c.esta_en_la_compra("U1"): bien += 1
    else: print("   MAL en esta_en_la_compra(U1): esperado False")
    print(f"{titulo}: {bien} de {total} pruebas correctas")

# Carga para medir: n utiles al azar (semilla fija) y presupuesto de un tercio del costo total
def generar_utiles(n):
    azar = random.Random(n + 1000)
    return [Util("K" + str(i), azar.randint(4, 49), azar.randint(10, 99)) for i in range(n)]

def ejecutar_carga(comprador, n):
    utiles = generar_utiles(n)
    presupuesto = sum(u.costo for u in utiles) // 3
    utilidad, _ = comprador.elegir(utiles, presupuesto)
    return utilidad

if __name__ == "__main__":
    probar("CompradorIngenuo ", CompradorIngenuo)
    probar("CompradorMejorado", CompradorMejorado)
