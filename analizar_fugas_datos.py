"""
Detecta si hay imágenes repetidas entre train y test.
Usa hash MD5 para comparación exacta.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path("datos/mvtec_anomaly_detection")
CATEGORIAS = [
    "bottle", "cable", "capsule", "carpet", "grid",
    "hazelnut", "leather", "metal_nut", "pill", "screw",
    "tile", "toothbrush", "transistor", "wood", "zipper"
]

def hashes(carpeta):
    return {hashlib.md5(f.read_bytes()).hexdigest() for f in carpeta.rglob("*.png")}

def main():
    reporte = {}
    for c in CATEGORIAS:
        train = hashes(ROOT / c / "train")
        test = hashes(ROOT / c / "test")
        comunes = train & test
        reporte[c] = len(comunes)
        if comunes:
            print(f"❌ Fuga en {c}: {len(comunes)} imágenes repetidas")
        else:
            print(f"✅ {c}: sin fuga")

    Path("resultados").mkdir(exist_ok=True)
    with open("resultados/fugas_datos.json", "w") as f:
        json.dump(reporte, f, indent=2)

if __name__ == "__main__":
    main()
