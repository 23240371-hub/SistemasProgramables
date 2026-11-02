# ============================================
# Proyecto: K9-Locate & Care
# Archivo: mqtt_bridge.py
# Objetivo: Suscribirse a los topicos MQTT del proyecto e imprimir lecturas en consola
# Equipo: Monserrat Lagos Guerrero, Ian Alberto Vargas Martínez (Colocar matrículas)
# Materia: Sistemas Programables — ISC TecNM León
# Semestre: ago-dic-2026
# ============================================

import paho.mqtt.client as mqtt

# Configuración del broker local
BROKER = "localhost"
PUERTO = 1883

# Lista de tópicos de suscripción (soporta formato HAL y formato Plantilla)
TOPICOS = [
    ("proyecto/s1", 0),           # DHT11 (Temperatura)
    ("proyecto/s2", 0),           # MAX30102 (Pulso cardiaco)
    ("proyecto/s3", 0),           # MPU-6050 (Actividad / IMU)
    ("proyecto/s4", 0),           # GPS NEO-6M (Ubicación)
    ("proyecto/sensor1", 0),      # Alias de plantilla
    ("proyecto/sensor2", 0),
    ("proyecto/sensor3", 0),
    ("proyecto/cam/frame", 0),    # Frames de ESP32-CAM
    ("proyecto/+/cmd", 0)         # Monitoreo de comandos a actuadores
]

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado exitosamente al broker Mosquitto")
        client.subscribe(TOPICOS)
        print("📡 Escuchando tópicos de K9-Locate & Care en espera de datos...")
    else:
        print(f"❌ Error al conectar con código: {rc}")

def on_message(client, userdata, msg):
    topico = msg.topic
    # Si es un frame de cámara, mostramos el tamaño en bytes en lugar de texto binario
    if topico == "proyecto/cam/frame":
        print(f"📷 [{topico}] Frame JPEG recibido ({len(msg.payload)} bytes)")
    else:
        mensaje = msg.payload.decode("utf-8", errors="ignore")
        print(f"📩 [{topico}] -> Lectura: {mensaje}")

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    print(f"Conectando a {BROKER}:{PUERTO}...")
    client.connect(BROKER, PUERTO, 60)
    
    # Mantiene el script corriendo y escuchando en consola
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nDesconectando del broker...")
        client.disconnect()

if __name__ == "__main__":
    main()