# Informe Final de Testeo — MVTec Anomaly Detection

**Proyecto:** Validación del pipeline de detección de anomalías sobre MVTec AD
**Equipo testador:** Equipo 2 — Transformer / embeddings
**Integrantes:**
- Abdiel Anaya Benitez
- David Sarmiento
- Cristian Damianis

**Equipos evaluados:**
- Equipo 2 — Transformer / embeddings
- Equipo 4 — Preprocesamiento y obtención de datos



---

## 1. Resumen ejecutivo

Se realizó una validación integral del pipeline de detección de anomalías no supervisada desarrollado por los Equipos 2 y 4 sobre el dataset **MVTec Anomaly Detection (MVTec AD)** de Bergmann et al. (2021). El objetivo fue verificar que:

- El dataset se cargue respetando la estructura oficial.
- El preprocesamiento no introduzca fuga de datos.
- Los embeddings y el Transformer produzcan resultados consistentes.
- Las métricas obtenidas sean comparables con los baselines del paper original.

El veredicto final se presenta en la sección 8.

---

## 2. Objeto evaluado

| Elemento | Descripción |
|----------|-------------|
| Dataset | MVTec AD — 15 categorías, 5354 imágenes |
| Tarea | Detección de anomalías no supervisada (nivel imagen y píxel) |
| Modelo evaluado | Transformer / embeddings (Equipo 2) |
| Preprocesamiento | Equipo 4 |
| Referencia | Bergmann et al., IJCV 129:1038–1059, 2021 |

---



---

## 4. Casos de prueba ejecutados

| ID | Prueba | Criterio | Estado |
|----|--------|----------|--------|
| CP-01 | Estructura del dataset | 15 categorías presentes | _(✅/❌)_ |
| CP-02 | Train solo con imágenes `good` | 0 imágenes defectuosas | _(✅/❌)_ |
| CP-03 | Máscaras alineadas con imágenes | Shapes coinciden | _(✅/❌)_ |
| CP-04 | Sin fuga train/test | 0 hashes comunes | _(✅/❌)_ |
| CP-05 | Categorías grayscale (`grid`, `screw`, `zipper`) | 1 canal o replicado | _(✅/❌)_ |
| CP-06 | Normalización solo con train | Stats no incluyen test | _(✅/❌)_ |
| CP-07 | Shape de embeddings | `(N, d_model)` correcto | _(✅/❌)_ |
| CP-08 | Sin NaN / inf en embeddings y predicciones | 0 valores anómalos | _(✅/❌)_ |
| CP-09 | Métricas comparables al paper | AU-PRO > 0.528 | _(✅/❌)_ |
| CP-10 | Reproducibilidad con semilla fija | Métricas idénticas | _(✅/❌)_ |

---

## 5. Resultados obtenidos

### 5.1 Métricas globales

| Métrica | Valor obtenido | Baseline mínimo (paper) | Estado |
|---------|---------------|-------------------------|--------|
| AU-PRO | _(valor)_ | 0.528 (f-AnoGAN) | _(✅/❌)_ |
| AU-ROC | _(valor)_ | 0.472 (f-AnoGAN) | _(✅/❌)_ |
| AU-PR | _(valor)_ | 0.136 (f-AnoGAN) | _(✅/❌)_ |

### 5.2 Comparación con baselines del paper

| Método | AU-PRO (paper) | Superado por el modelo |
|--------|---------------|------------------------|
| f-AnoGAN | 0.528 | _(✅/❌)_ |
| Variation Model | 0.556 | _(✅/❌)_ |
| SSIM-Autoencoder | 0.617 | _(✅/❌)_ |
| L2-Autoencoder | 0.632 | _(✅/❌)_ |
| Texture Inspection | 0.741 | _(✅/❌)_ |
| Feature Dictionary | 0.803 | _(✅/❌)_ |
| Student-Teacher | 0.924 | _(✅/❌)_ |

### 5.3 Análisis de fuga de datos

Resultado del script `analizar_fugas_datos.py`:

- Categorías con fuga detectada: _(listar o "ninguna")_
- Total de hashes repetidos: _(N)_

---

## 6. Incidencias encontradas

| ID | Descripción | Severidad | Estado |
|----|-------------|-----------|--------|
| INC-01 | _(descripción)_ | _(bloqueante/crítico/mayor/menor)_ | _(abierta/cerrada)_ |
| INC-02 | | | |
| INC-03 | | | |

---

## 7. Evidencia

- `resultados/metricas.csv` — métricas calculadas.
- `resultados/fugas_datos.json` — análisis de fuga.
- `resultados/` — figuras y capturas.
- Scripts en la raíz del repositorio.

---

## 8. Veredicto

**Aprobado / Aprobado con observaciones / Rechazado**

Justificación:
_(Redactar según los resultados reales. Ejemplo:)_
> El pipeline cumple con la estructura esperada del dataset MVTec AD y no presenta fuga de datos entre train y test. Las métricas obtenidas superan el baseline mínimo del paper (f-AnoGAN, AU-PRO = 0.528), aunque no alcanzan el desempeño del método Student-Teacher (AU-PRO = 0.924). Se recomienda revisar la selección del umbral y el tratamiento de las categorías en escala de grises.

---

## 9. Recomendaciones

1. Documentar la estrategia de selección de umbral usada para binarizar los mapas de anomalía.
2. Verificar que la normalización se calcule únicamente con estadísticas del conjunto de entrenamiento.
3. Reportar métricas por categoría, no solo el promedio global, ya que el paper muestra alta variabilidad entre categorías.
4. Añadir pruebas con semillas fijas para garantizar reproducibilidad.

---

## 10. Referencias

Bergmann, P., Batzner, K., Fauser, M., Sattlegger, D., & Steger, C. (2021).
*The MVTec Anomaly Detection Dataset: A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection.*
International Journal of Computer Vision, 129(4), 1038–1059.
