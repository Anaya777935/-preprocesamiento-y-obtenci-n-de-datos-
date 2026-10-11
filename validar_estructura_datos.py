
from pathlib import Path

ROOT = Path("datos/mvtec_anomaly_detection")

CATEGORIAS = [
    "bottle", "cable", "capsule", "carpet", "grid",
    "hazelnut", "leather", "metal_nut", "pill", "screw",
    "tile", "toothbrush", "transistor", "wood", "zipper"
]

def validar():
    errores = []
    for c in CATEGORIAS:
        ruta = ROOT / c
        if not ruta.exists():
            errores.append(f"Falta categoría: {c}")
            continue
        if not (ruta / "train" / "good").exists():
            errores.append(f"{c}: falta train/good/")
        if not (ruta / "test").exists():
            errores.append(f"{c}: falta test/")
        if not (ruta / "ground_truth").exists():
            errores.append(f"{c}: falta ground_truth/")
    return errores

def main():
    errores = validar()
    if errores:
        print("❌ Errores encontrados:")
        for e in errores:
            print(f"  - {e}")
    else:
        print("✅ Estructura del dataset correcta (15 categorías)")

if __name__ == "__main__":
    main()
