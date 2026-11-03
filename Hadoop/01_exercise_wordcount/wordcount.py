import sys
from collections import Counter
from pathlib import Path

archivo_entrada = sys.argv[1]
carpeta_salida = Path(sys.argv[2])

with open(archivo_entrada, "r", encoding="utf-8", errors="ignore") as f:
    texto = f.read()

palabras = texto.lower().split()
conteo = Counter(palabras)

carpeta_salida.mkdir()

archivo_salida = carpeta_salida / "part-r-00000"

with open(archivo_salida, "w", encoding="utf-8") as f:
    for palabra, cantidad in sorted(conteo.items()):
        f.write(f"{palabra}\t{cantidad}\n")

print(f"Resultado guardado en: {archivo_salida}")

# ejemplo de ejecución:
# python wordcount.py /path/to/input.txt /path/to/output_folder