# /archive_v3 - Núcleo Möbius V3.0 a V3.5

> **ESTADO: ARCHIVO HISTÓRICO / LEGACY**  
> **NO EJECUTAR CON V8.4 LITE.** Requiere dependencias deprecadas: `libcore.so`, `ollama`.

Esta carpeta contiene el inicio de evolución del proyecto. Son los fósiles de V3.

### Árbol Genealógico
`V3.0 core.cpp` -> `V3.1 simulacion_real_qnd.py` -> `V3.5 qed_motor.py` -> `V8.4 Lite`

### Inventario

| Archivo | Qué era | Por qué se deprecó en V8.4 |
| --- | --- | --- |
| `AUDITORIA_ERROR.txt` | Log de calibración QND. `kappa_eff` y `Fidelidad 0.31` | Reemplazado por `dephasing_log.json` y gráficos Möbius |
| `core.cpp` | Motor geométrico puro C++. `Weitzenböck`, `Punto de Silla E=0` | Migrado 100% a Python por portabilidad. Ver: `calcular_estado_moebius()` |
| `qed_motor.py` | Orquestador Python + C++ + LLM `Ollama:11434` | Se quitó Ollama y `.so` para que V8.4 corra 100% offline en Termux sin compilar |

### Código Activo Actual
El repo ahora corre con: `python pipeline_moebius_v8.4.py`Zenodo DOI 10.5281/zenodo.21042393

Estos archivos se conservan solo por trazabilidad histórica y evolución del algoritmRequierequiere
