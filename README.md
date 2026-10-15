# Pipeline de Extracción de Entidades Técnicas con LCEL y Pydantic

Este proyecto implementa un pipeline asíncrono y resiliente con **LangChain Expression Language (LCEL)** y **Pydantic** para la extracción estructurada de entidades técnicas a partir de logs o descripciones de arquitectura.

## 🎯 Características
* **Contratos con Pydantic**: Salida validada con campos `tecnologias`, `nivel_de_criticidad` y `resumen_tecnico`.
* **Composición LCEL**: Unión modular con `prompt | model.with_structured_output(Schema)`.
* **Resiliencia Automática**: Reintentos automáticos mediante `.with_retry()`.
* **Procesamiento Asíncrono**: Ejecución con `.ainvoke()`.

## 🛠️ Instalación y Uso

1. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt