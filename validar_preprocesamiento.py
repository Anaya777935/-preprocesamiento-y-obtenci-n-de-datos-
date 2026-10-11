
from pathlib import Path
from PIL import Image
import numpy as np

ROOT = Path("datos/mvtec_anomaly_detection")
CATEGORIAS = [
    "bottle", "cable", "capsule", "carpet", "grid",
    "hazelnut", "leather", "metal_nut", "pill", "screw",
    "tile", "toothbrush", "transistor", "wood", "zipper"
]
GRAYSCALE = {"grid", "screw", "zipper"}

def revisar_train_solo_good():
    for c in CATEGORIAS:
        subcarpetas = [p.name for p in (ROOT / c / "train").iterdir()]
        if subcarpetas != ["good"]:
            print(f"  ⚠️ {c}/train tiene: {subcarpetas}")

def revisar_mascaras():
    for c in CATEGORIAS:
        gt = ROOT / c / "ground_truth"
        test = ROOT / c / "test"
        if not gt.exists():
            continue
        for defecto in gt.iterdir():
            for mask in defecto.glob("*_mask.png"):
                img = test / defecto.name / mask.name.replace("_mask.png", ".png")
                if not img.exists():
                    print(f"  ❌ Falta imagen para máscara: {mask}")
                    continue
                m = np.array(Image.open(mask))
                im = np.array(Image.open(img))
                if m.shape[:2] != im.shape[:2]:
                    print(f"  ❌ Shape distinto: {mask}")

def revisar_grayscale():
    for c in GRAYSCALE:
        imgs = list((ROOT / c / "train" / "good").glob("*.png"))
        if not imgs:
            continue
        arr = np.array(Image.open(imgs[0]))
        if arr.ndim != 2:
            print(f"  ⚠️ {c} debería ser grayscale, tiene {arr.ndim} canales")

def main():
    print("Revisando train solo con 'good'...")
    revisar_train_solo_good()
    print("Revisando alineación de máscaras...")
    revisar_mascaras()
    print("Revisando categorías en escala de grises...")
    revisar_grayscale()
    print("✅ Validación de preprocesamiento terminada")

if __name__ == "__main__":
    main()
