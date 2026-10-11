"""

"""
from pathlib import Path

URL = "https://www.mvtec.com/company/research/datasets/mvtec-ad"
DESTINO = Path("datos/mvtec_anomaly_detection")

def main():
    DESTINO.mkdir(parents=True, exist_ok=True)
    print("Descarga el dataset desde:")
    print(f"  {URL}")
    print("Extrae el contenido en:")
    print(f"  {DESTINO.resolve()}")

if __name__ == "__main__":
    main()
