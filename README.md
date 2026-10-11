# Testeo de MVTec AD — Detección de Anomalías

## Integrantes
- Abdiel Anaya Benítez
- David Sarmiento Alvarado
 Cristiam Damian

## Descripción del proyecto

Este proyecto tiene como objetivo validar y verificar el trabajo realizado por el **Equipo 2 (Transformer / embeddings)** y el **Equipo 4 (preprocesamiento y obtención de datos)** sobre el dataset **MVTec Anomaly Detection (MVTec AD)**.

Se verifica que:
- El dataset se cargue con la estructura oficial.
- El preprocesamiento no tenga fuga de datos.
- Los embeddings tengan las dimensiones correctas.
- Las métricas sean reproducibles.
- Los resultados sean comparables con los baselines del paper original de Bergmann et al. (2021).

## Estructura del repositorio

- `datos/` — dataset MVTec AD (se descarga aparte).
- `docs/` — plan de pruebas, matriz de trazabilidad e informe final.
- `resultados/` — métricas, figuras y evidencias de las pruebas.
- `*.py` — scripts de validación y análisis.

## Requisitos

```bash
pip install -r requirements.txt
