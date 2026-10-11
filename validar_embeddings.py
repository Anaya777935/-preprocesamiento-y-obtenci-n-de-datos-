"""
Verifica que los embeddings producidos por el Equipo 2
tengan las dimensiones correctas.
Adapta las rutas según cómo los entreguen.
"""
from pathlib import Path
import numpy as np

RUTA_EMBEDDINGS = Path("resultados/embeddings.npy")
D_MODEL_ESPERADO = 128  # ajustar según lo que declare el Equipo 2

def main():
    if not RUTA_EMBEDDINGS.exists():
        print(f"⚠️ No se encontró {RUTA_EMBEDDINGS}")
        print("   Pide al Equipo 2 que guarde aquí los embeddings.")
        return

    emb = np.load(RUTA_EMBEDDINGS)
    print(f"Shape de embeddings: {emb.shape}")
    print(f"¿Coincide con d_model={D_MODEL_ESPERADO}?",
          "✅" if emb.shape[-1] == D_MODEL_ESPERADO else "❌")
    print(f"¿Hay NaN? {'❌' if np.isnan(emb).any() else '✅'}")
    print(f"¿Hay infinitos? {'❌' if np.isinf(emb).any() else '✅'}")

if __name__ == "__main__":
    main()
