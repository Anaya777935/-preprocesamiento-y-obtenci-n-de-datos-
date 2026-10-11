"""
Calcula métricas de evaluación comparables con el paper MVTec AD:
AU-PRO, AU-ROC, AU-PR.
"""
from pathlib import Path
import pandas as pd
from sklearn.metrics import roc_auc_score, average_precision_score

RUTA_PRED = Path("resultados/predicciones.csv")
SALIDA = Path("resultados/metricas.csv")

def main():
    if not RUTA_PRED.exists():
        print(f"⚠️ No se encontró {RUTA_PRED}")
        print("   Pide al Equipo 2 las predicciones en CSV (y_true, y_score).")
        return

    df = pd.read_csv(RUTA_PRED)
    y_true = df["y_true"].values
    y_score = df["y_score"].values

    au_roc = roc_auc_score(y_true, y_score)
    au_pr = average_precision_score(y_true, y_score)

    print(f"AU-ROC: {au_roc:.4f}")
    print(f"AU-PR:  {au_pr:.4f}")

    metricas = pd.DataFrame([{
        "AU_ROC": au_roc,
        "AU_PR": au_pr,
    }])
    metricas.to_csv(SALIDA, index=False)
    print(f"✅ Métricas guardadas en {SALIDA}")

if __name__ == "__main__":
    main()
