# Plan de Pruebas — MVTec AD

## 1. Alcance
Validar el pipeline de preprocesamiento (Equipo 4) y el modelo Transformer / embeddings (Equipo 2) sobre el dataset MVTec AD.

## 2. Casos de prueba

| ID | Prueba | Criterio de aceptación |
|----|--------|------------------------|
| CP-01 | Estructura del dataset | 15 categorías presentes |
| CP-02 | Train solo con imágenes `good` | 0 imágenes defectuosas |
| CP-03 | Máscaras alineadas con imágenes | Shapes coinciden |
| CP-04 | Sin fuga train/test | 0 hashes comunes |
| CP-05 | Categorías grayscale | 1 canal o replicado |
| CP-06 | Normalización solo con train | Stats no incluyen test |
| CP-07 | Shape de embeddings | `(N, d_model)` correcto |
| CP-08 | Sin NaN / inf | 0 valores anómalos |
| CP-09 | Métricas comparables al paper | AU-PRO > 0.528 |
| CP-10 | Reproducibilidad con semilla | Métricas iguales |

## 3. Baselines del paper (AU-PRO mean)

| Método | AU-PRO |
|--------|--------|
| f-AnoGAN | 0.528 |
| Variation Model | 0.556 |
| SSIM-Autoencoder | 0.617 |
| L2-Autoencoder | 0.632 |
| Texture Inspection | 0.741 |
| Feature Dictionary | 0.803 |
| **Student-Teacher** | **0.924** |
