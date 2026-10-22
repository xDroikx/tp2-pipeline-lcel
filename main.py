import asyncio
from dotenv import load_dotenv
from rag_chain import get_rag_response

load_dotenv()


async def main():
    print("========================================")
    print("PROBANDO SISTEMA RAG LOCAL (TP 3)")
    print("========================================\n")

    # 1. Caso 1: Pregunta cuya respuesta SÍ está en los documentos
    pregunta_valida = "¿Qué es ChromaDB y cómo funciona su persistencia local?"
    print("--- 1. Prueba con Pregunta Válida ---")
    print(f"Pregunta: {pregunta_valida}\n")
    
    try:
        respuesta1 = await get_rag_response(pregunta_valida)
        print("✅ Respuesta Validada:")
        print(f"• Respuesta: {respuesta1.respuesta}")
        print(f"• Fuentes:   {respuesta1.fuentes}\n")
    except Exception as e:
        print(f"❌ Error en prueba 1: {e}\n")

    print("=" * 50 + "\n")

    # 2. Caso 2: Pregunta Trampa (NO está en los documentos)
    pregunta_trampa = "¿Cómo se despliega un cluster de Kubernetes en Google Cloud?"
    print("--- 2. Prueba con Pregunta Trampa (Filtro Anti-Alucinación) ---")
    print(f"Pregunta: {pregunta_trampa}\n")
    
    try:
        respuesta2 = await get_rag_response(pregunta_trampa)
        print("✅ Respuesta Validada:")
        print(f"• Respuesta: {respuesta2.respuesta}")
        print(f"• Fuentes:   {respuesta2.fuentes}\n")
    except Exception as e:
        print(f"❌ Error en prueba 2: {e}\n")


if __name__ == "__main__":
    asyncio.run(main())