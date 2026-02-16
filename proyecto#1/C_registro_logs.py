from datetime import datetime

def registrar_evento(tipo, mensaje):
    
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    linea = f"[{fecha}] [{tipo}] {mensaje}\n"

    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(linea)