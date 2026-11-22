# Tania Mamani Ramos
# PARCIAL 2 - VARIANTE A: Turnos de una clinica (portado de C# a Python)
import heapq, time, os, platform
from collections import namedtuple

Paciente = namedtuple("Paciente", "nombre urgencia llegada")

# ---------- SOLUCION INGENUA (lista simple): correcta pero lenta ----------
class GestorIngenuo:
    def __init__(self):
        self._lista = []
        self._llegadas = 0

    def registrar(self, nombre, urgencia):
        self._lista.append(Paciente(nombre, urgencia, self._llegadas))
        self._llegadas += 1

    def atender_siguiente(self):
        if not self._lista:
            return None
        mejor = 0
        for i in range(1, len(self._lista)):
            p, m = self._lista[i], self._lista[mejor]
            if p.urgencia < m.urgencia or (p.urgencia == m.urgencia and p.llegada < m.llegada):
                mejor = i
        nombre = self._lista[mejor].nombre
        del self._lista[mejor]
        return nombre

    def esta_esperando(self, nombre):
        for p in self._lista:
            if p.nombre == nombre:
                return True
        return False

    @property
    def esperando(self):
        return len(self._lista)

# ---------- MI SOLUCION: cola de prioridad (heap) + conjunto (set) ----------
class GestorMejorado:
    def __init__(self):
        self._heap = []          # tuplas (urgencia, llegada, nombre): el heap saca la menor
        self._en_espera = set()  # nombres que siguen esperando
        self._llegadas = 0

    def registrar(self, nombre, urgencia):                 # O(log n)
        heapq.heappush(self._heap, (urgencia, self._llegadas, nombre))
        self._en_espera.add(nombre)                        # O(1)
        self._llegadas += 1

    def atender_siguiente(self):                           # O(log n)
        if not self._heap:
            return None
        _, _, nombre = heapq.heappop(self._heap)
        self._en_espera.remove(nombre)                     # O(1)
        return nombre

    def esta_esperando(self, nombre):                      # O(1)
        return nombre in self._en_espera

    @property
    def esperando(self):                                   # O(1)
        return len(self._en_espera)

# ---------- Guion de pruebas (el mismo del examen) ----------
GUION = [
    ("registrar", "Ana", 3, ""), ("registrar", "Beto", 1, ""), ("registrar", "Carla", 3, ""), ("registrar", "Diego", 2, ""),
    ("esperando", "", 0, "4"),
    ("esta", "Beto", 0, "True"), ("esta", "Zoe", 0, "False"),
    ("atender", "", 0, "Beto"), ("esta", "Beto", 0, "False"),
    ("atender", "", 0, "Diego"),
    ("registrar", "Elena", 1, ""),
    ("atender", "", 0, "Elena"), ("atender", "", 0, "Ana"), ("atender", "", 0, "Carla"),
    ("atender", "", 0, "(nadie)"), ("esperando", "", 0, "0"),
]

def ejecutar(g, op, arg, urg):
    if op == "registrar":
        g.registrar(arg, urg); return ""
    if op == "atender":
        r = g.atender_siguiente(); return "(nadie)" if r is None else r
    if op == "esta":
        return str(g.esta_esperando(arg))
    return str(g.esperando)

def probar(titulo, g):
    bien = total = 0
    for op, arg, urg, esperado in GUION:
        obtenido = ejecutar(g, op, arg, urg)
        if op == "registrar":
            continue
        total += 1
        if obtenido == esperado:
            bien += 1
        else:
            print(f"   MAL en '{op} {arg}': esperado {esperado}, obtuvo {obtenido}")
    print(f"{titulo}: {bien} de {total} pasos correctos")

# ---------- Carga para medir: n pacientes llegan y luego se atiende a los n ----------
def ejecutar_carga(g, n):
    for i in range(n):
        g.registrar("P" + str(i), (i * 7919) % 5 + 1)
    control = 0
    for _ in range(n):
        control += len(g.atender_siguiente())
    return control

def medir(clase, n, corridas=3):
    ejecutar_carga(clase(), n)                  # calentamiento (se descarta)
    tiempos = []
    for _ in range(corridas):
        g = clase()
        a = time.perf_counter(); ejecutar_carga(g, n); b = time.perf_counter()
        tiempos.append((b - a) * 1000)
    return sum(tiempos) / len(tiempos)          # promedio en ms

if __name__ == "__main__":
    probar("GestorIngenuo ", GestorIngenuo())
    probar("GestorMejorado", GestorMejorado())
    # comprobar que ambos dan el mismo resultado en la carga
    assert ejecutar_carga(GestorIngenuo(), 2000) == ejecutar_carga(GestorMejorado(), 2000)
    print("Ambos dan el mismo resultado en la carga: OK")
