# Matriz de Trazabilidad

| Requisito | Caso de prueba | Script | Estado |
|-----------|----------------|--------|--------|
| Dataset completo | CP-01 | validar_estructura_datos.py | |
| Train limpio | CP-02 | validar_preprocesamiento.py | |
| Máscaras alineadas | CP-03 | validar_preprocesamiento.py | |
| Sin fuga | CP-04 | analizar_fugas_datos.py | |
| Grayscale | CP-05 | validar_preprocesamiento.py | |
| Embeddings correctos | CP-07 | validar_embeddings.py | |
| Métricas comparables | CP-09 | evaluar_modelo.py + comparar_con_paper.py | |
