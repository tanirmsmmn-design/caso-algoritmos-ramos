# Tania Mamani Ramos
# H2: medicion de la estructura de mi caso. Protocolo: 1 calentamiento + 3 corridas medidas + promedio.
# Uso: python medicion_h2.py   (necesita estructuras_inventario.py en la misma carpeta)
import time, platform
from estructuras_inventario import InventarioIngenuo, InventarioDiccionario, generar_codigos, ejecutar_carga

N_BASE = 2000      # tamanos n, 2n, 4n, 8n. Si la lista tarda mas de 20 s con 8n, baja N_BASE.

def medir(clase, codigos, corridas=3):
    ejecutar_carga(clase(), codigos)                    # calentamiento (se descarta)
    t = []
    for _ in range(corridas):
        inv = clase()
        a = time.perf_counter(); ejecutar_carga(inv, codigos); b = time.perf_counter()
        t.append((b - a) * 1000)
    return sum(t) / len(t)

print(f"Python {platform.python_version()} en {platform.system()}. Protocolo: 1 calentamiento + 3 corridas + promedio.")
print("| n productos | Lista simple (ms) | Lista vs fila anterior | Diccionario (ms) | Diccionario vs fila anterior |")
pi = pd = None
for k in (1, 2, 4, 8):
    n = N_BASE * k
    cods = generar_codigos(n)
    ti, td = medir(InventarioIngenuo, cods), medir(InventarioDiccionario, cods)
    ri = f"x{ti / pi:.1f}" if pi else "-"
    rd = f"x{td / pd:.1f}" if pd else "-"
    print(f"| {n:,} | {ti:.2f} | {ri} | {td:.3f} | {rd} |")
    pi, pd = ti, td
print("Los numeros varian un poco entre corridas (ruido); la tabla de medicion.md es de mi corrida.")
