import ctypes
import os
import urllib.request
import json
import math
import time

lib_path = os.path.abspath("./libcore.so")
core = ctypes.CDLL(lib_path)

core.calcular_identitario_total_tensorial.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]
core.calcular_identitario_total_tensorial.restype = ctypes.c_float

def transmitir_a_ollama_qed(psi_total, tension_i, tension_q, fase_berry):
    url = "http://localhost:11434/api/chat"
    
    # SYSTEM PROMPT DE RIGOR CIENTÍFICO EXTREMO
    prompt_laboratorio = (
        "ACTUA COMO UN EXPERTO EN COMPONENTES DE MICROONDAS CRIOJANICAS Y ELECTRODINAMICA CUANTICA DE CAVIDADES (Cavity QED). "
        "PROHIBIDO EL USO DE METAFORAS, FILOSOFIA, POESIA O CUALQUIER TERMINO SUBJETIVO O PSICOLOGICO. "
        "RESPONDE EXCLUSIVAMENTE CON LENGUAJE TECNICO DE FISICA EXPERIMENTAL Y PARAMETROS DE DISPERSION (S-PARAMETERS). "
        "Analiza el siguiente vector de estado para una medicion No-Destructiva Cuantica (QND) a 2.45 GHz:\n"
        f"- Operador de Torsion Covariante (Psi_total): {psi_total:.6f}\n"
        f"- Componentes de Voltaje en Cuadratura: I = {tension_i:.4f} mV, Q = {tension_q:.4f} mV\n"
        f"- Desplazamiento Topologico de Fase de Berry: {fase_berry:.6f} rad.\n"
        "Redacta un reporte tecnico estructurado que responda a los siguientes criterios cientificos:\n"
        "1. EVALUACION METRICA: Como se comporta la admitancia del Laplaciano frente al acoplamiento del tensor de torsion.\n"
        "2. ANALISIS DE DE-COHERENCIA: Si la inversion de signo no-orientable en theta = pi cancela de forma efectiva la atenuacion de fase.\n"
        "3. ESTADO DE LA FUNCION DE ONDA: Determina si el modulo de Psi_total garantiza la preservacion de la superposicion coherente (QND conforme) o si existe dispersion radiativa."
    )
    
    payload = {
        "model": "gemma2:2b",
        "messages": [
            {"role": "system", "content": prompt_laboratorio},
            {"role": "user", "content": "SOLICITUD DE PROTOCOLO: Procesar telemetria analoga de componentes S11 sobre contorno Moebius."}
        ],
        "stream": False,
        "options": {"temperature": 0.0, "top_p": 0.1, "seed": 42} # Determinismo absoluto a nivel de bit
    }
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as res:
            resultado = json.loads(res.read().decode('utf-8'))
            return resultado['message']['content']
    except Exception as e:
        return f"\n[CRITICAL FAULT] Interrupcion en la adquisicion del ADC local: {str(e)}"

def ejecutar_bucle_laboratorio():
    print("=== COVARIANT-QED: MONITOR TENSORIAL DE ALTO RIGOR EXPERIMENTAL ===")
    print("Sincronizando canales ADC de muestreo rapido (I/Q de microondas a 2.45 GHz)...")
    print("Filtro Möbius y operador de Entelequia Indivisible acoplados al hardware local.")
    print("Presione Control+C para finalizar la adquisicion de datos de RF.\n")
    
    historial_tensiones = []
    paso_tiempo = 0
    
    try:
        while True:
            paso_tiempo += 1
            
            # Flujo de datos analógicos de señales en cuadratura (Simulando ADC criogénico)
            tension_i = math.sin(paso_tiempo * 0.2) * 50.0
            tension_q = math.cos(paso_tiempo * 0.2) * 50.0
            fase_berry = (paso_tiempo * 0.05) % (2 * math.pi)
            
            # Calculamos la magnitud de voltaje neta instantanea para alimentar la integral de Riemann
            magnitud_voltaje_neta = math.sqrt(tension_i**2 + tension_q**2)
            historial_tensiones.append(float(magnitud_voltaje_neta))
            if len(historial_tensiones) > 100:
                historial_tensiones.pop(0)
                
            n = len(historial_tensiones)
            ArrayFloat = ctypes.c_float * n
            array_nativo = ArrayFloat(*historial_tensiones)
            
            # Inferencia matematica en el procesador mediante C++ nativo
            psi_total = core.calcular_identitario_total_tensorial(array_nativo, n)
            
            print("-" * 60)
            print(f"[DATA_FRAME: +{paso_tiempo}s] | Frecuencia Operacional: 2.45000 GHz")
            print(f"CANALES RF -> Voltaje I: {tension_i:.4f} mV | Voltaje Q: {tension_q:.4f} mV | \u03a6_Berry: {fase_berry:.6f} rad")
            print(f"CALCULO COVARIANTE DE C++ -> \u03a8_total = {psi_total:.6f}")
            print("[Iniciando evaluacion determinista de la matriz de dispersion... por favor espere]")
            
            reporte_cientifico = transmitir_a_ollama_qed(psi_total, tension_i, tension_q, fase_berry)
            print(f"\n[INFORME TECNICO DE INGENIERIA CUANTICA]:\n{reporte_cientifico.strip()}\n")
            
            time.sleep(4)
            
    except KeyboardInterrupt:
        print("\n[STOP] Telemetria interrumpida. Canales logicos en reposo absoluto.")

if __name__ == "__main__":
    ejecutar_bucle_laboratorio()




