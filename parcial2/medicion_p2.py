
# Tania Mamani Ramos
# Genera medicion.md con el protocolo: 1 calentamiento + 3 corridas + promedio.
import platform
from turnos_clinica import GestorIngenuo, GestorMejorado, medir

N_BASE = 2000                      # tamanos: n, 2n, 4n. Si la ingenua tarda mas de 20 s con 4n, baja N_BASE.
tamanos = [N_BASE, 2 * N_BASE, 4 * N_BASE]
filas = []
prev_i = prev_m = None
for n in tamanos:
    ti = medir(GestorIngenuo, n)
    tm = medir(GestorMejorado, n)
    ri = f"x{ti / prev_i:.1f}" if prev_i else "-"
    rm = f"x{tm / prev_m:.1f}" if prev_m else "-"
    filas.append(f"| {n:,} | {ti:.1f} | {ri} | {tm:.1f} | {rm} |")
    print(f"n={n:,}: ingenua {ti:.1f} ms ({ri}) | mejorada {tm:.1f} ms ({rm})")
    prev_i, prev_m = ti, tm

texto = f"""Tania Mamani Ramos

# Parcial 2 - Variante A: medicion

Medido en Python {platform.python_version()} en {platform.system()}, en mi computadora. Funcion de carga: n pacientes llegan y luego se atiende a los n. Protocolo: 1 corrida de calentamiento + 3 corridas medidas + promedio.

| n (pacientes) | Ingenua (ms) | Ingenua vs fila anterior | Mejorada (ms) | Mejorada vs fila anterior |
|---:|---:|---:|---:|---:|
""" + "\n".join(filas) + """

## Conclusion (COMPLETAR CON EL RESULTADO)

- Ingenua: ...
- Mejorada: ...
- Ruido: ...
"""
open("medicion.md", "w", encoding="utf-8").write(texto)
print("\nListo: se creo medicion.md")
