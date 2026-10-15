import asyncio
from dotenv import load_dotenv

from chain import process_text

load_dotenv()


async def main():
    print("========================================")
    print("PROBANDO PIPELINE LCEL (TP 2)")
    print("========================================\n")

    # 1. Caso Normal: Log técnico estructurado
    texto_tecnico = """
    Nuestra API en FastAPI está devolviendo timeouts intermitentes. El caché en Redis 
    parece saturarse en picos de tráfico y las conexiones a PostgreSQL se agotan 
    porque el pool está mal dimensionado. Esto está afectando a usuarios en producción.
    """

    print("--- 1. Caso Normal: Log Técnico ---")
    try:
        resultado = await process_text(texto_tecnico)
        print("\n✅ Resultado JSON Validado:")
        print(resultado.model_dump_json(indent=2))
    except Exception as e:
        print(f"❌ Error en caso normal: {e}")

    print("\n" + "=" * 40 + "\n")

    # 2. Prueba de Estrés: Texto ambiguo sin nombres explícitos de tecnologías
    texto_ambiguo = """
    El sistema anda medio lento últimamente. Parece que cuando entra mucha gente 
    se cae la base de datos pero no estoy muy seguro de qué motor estamos usando en el servidor.
    """

    print("--- 2. Prueba de Estrés: Texto Ambiguo ---")
    try:
        resultado_ambiguo = await process_text(texto_ambiguo)
        print("\n✅ Resultado JSON Validado (Texto ambiguo):")
        print(resultado_ambiguo.model_dump_json(indent=2))
    except Exception as e:
        print(f"❌ Error en prueba de estrés: {e}")


if __name__ == "__main__":
    asyncio.run(main())