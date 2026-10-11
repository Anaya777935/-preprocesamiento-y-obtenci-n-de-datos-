
from pathlib import Path
import pandas as pd

BASELINES = {
    "f-AnoGAN":           0.528,
    "Feature Dictionary": 0.803,
    "Student-Teacher":    0.924,
    "L2-Autoencoder":     0.632,
    "SSIM-Autoencoder":   0.617,
    "Texture Inspection": 0.741,
    "Variation Model":    0.556,
}

def main():
    ruta = Path("resultados/metricas.csv")
    if not ruta.exists():
        print("⚠️ Ejecuta primero evaluar_modelo.py")
        return

    m = pd.read_csv(ruta).iloc[0]
    au_pro = m.get("AU_PRO", m.get("AU_PR", 0))

    print(f"AU-PRO obtenido: {au_pro:.4f}\n")
    print("Comparación con baselines del paper:")
    for nombre, valor in sorted(BASELINES.items(), key=lambda x: -x[1]):
        estado = "✅ supera" if au_pro > valor else "❌ no supera"
        print(f"  {nombre:22s} {valor:.3f}  → {estado}")

if __name__ == "__main__":
    main()
