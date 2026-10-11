"""
Genera el informe final combinando los resultados obtenidos.
"""
from pathlib import Path
from datetime import datetime

DOCS = Path("docs")
DOCS.mkdir(exist_ok=True)

def main():
    contenido = f"""# Informe Final de Testeo — MVTec AD

Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}

## 1. Objeto evaluado
- Equipo 2: Transformer / embeddings
- Equipo 4: Preprocesamiento y obtención de datos
- Dataset: MVTec AD (Bergmann et al., 2021)

## 2. Pruebas ejecutadas
Ver `docs/matriz_trazabilidad.md`.

## 3. Resultados
Ver `resultados/metricas.csv` y `resultados/fugas_datos.json`.

## 4. Veredicto
(Pendiente de completar tras revisión final)

## 5. Evidencia
- `resultados/metricas.csv`
- `resultados/fugas_datos.json`
- Capturas y logs en `resultados/`
"""
    (DOCS / "informe_final.md").write_text(contenido, encoding="utf-8")
    print("✅ Informe generado en docs/informe_final.md")

if __name__ == "__main__":
    main()
