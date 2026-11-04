# K9 Rescue Cam — Perchera de exploracion canina 

> **Semestre:** ago-dic-2026
> **Materia:** Sistemas Programables — ISC TecNM León
> **Integrantes:**

| Nombre | Matrícula | Rol | GitHub | 
| ----- | ----- | ----- | ----- | 
| Monserrat Lagos Guerrero | 23240348 | 🔧 Firmware ESP32 / 🔩 Hardware y Carcasa / 📝 Documentación | MonserratLagosGuerrero| 
| Ian Alberto Vargas Martínez | 23240371 | 🧠 Servidor Python/IA / ☁️ Firebase e Interfaz / 📝 Documentación | 23240371-hub | 


## 📌 Descripción General

**K9-Locate & Care** ayuda a los dueños de mascotas a proteger y localizar a sus perros cuando se asustan o se extravían fuera de casa. Resuelve el problema de la pérdida de ubicación y el desconocimiento del estado físico y ambiental del canino mediante el monitoreo continuo de su geolocalización GPS, temperatura ambiental, nivel de actividad y ritmo cardiaco para detectar estrés elevado. A diferencia de los collares rastreadores convencionales, este chaleco inteligente IoT integra visión artificial en vivo mediante una ESP32-CAM para identificar si el perro se encuentra cerca de personas y permite interactuar físicamente a distancia mediante comandos táctiles de vibración, llamados sonoros y un dispensador automático de premios al retornar.


# Tabla ESP32 Principal
| Tópico | Pin / Cable Componente | Pin ESP32 (GPIO) | Tipo de Pin / Función | Notas de Alimentación / Conexión |
|---|---|---|---|---|
| Servomotor SG90 | Señal (Naranja / Amarillo) | GPIO 4 (D4) | Salida PWM | Frecuencia 50Hz para control de ángulo (0° - 90°) |
| Servomotor SG90 | VCC (Rojo) | VIN (5V) | Alimentación 5V | Requiere 5V. Recomendable alimentar de línea de 5V |
| Servomotor SG90 | GND (Marrón / Negro) | VIN (5V) | Alimentación 5V | Requiere 5V. Recomendable alimentar de línea de 5V |
| Buzzer Pasivo | Positivo (+ / Señal) | GPIO 0 (D0) | Salida PWM | Se activa a 2000Hz (duty 512) |
| Buzzer Pasivo | Negativo (- / GND) | GND | Tierra Común | Conectar a cualquier pin GND |

# Tabla ESP32-CAM
| Componente           | Pin / Cable Componente | Pin ESP32-CAM         | Tipo de Pin / Función   | Notas de Alimentación / Modo   |
|----------------------|------------------------|-----------------------|-------------------------|------------------------------------------------------------|
| Cámara OV2640        | Flex Ribbon 24-pin     | Conector FPC Dedicado | Bus Paralelo Cámara     | Asegurar seguro marrón/negro del socket                    |
| Módulo Alimentación  | VCC / 5V (+)           | 5V / VCC              | Alimentación 5V Directa | CRÍTICO: Alimentar con 5V reales (mín. 500mA - 1A)         |
| Módulo Alimentación  | GND (-)                | GND                   | Tierra Común            | Conectar a GND general del sistema                         |
| Programador FTDI USB | TX (FTDI)              | U0RX / GPIO 3         | Comunicación Serial RX  | Para carga de código / logs seriales (115200 baudios)      |
| Programador FTDI USB | RX (FTDI)              | U0TX / GPIO 1         | Comunicación Serial TX  | Para carga de código / logs seriales                       |
| Modo Flasheo (Opcional)| GPIO 0               | GND                   | Modo Bootloader         | Puente a GND SOLO para flashear. Desconectar en uso normal |

# Tabla de Componentes
| Ítem | Componente / Módulo | Cantidad | Función en el Sistema K9-Locate | Especificaciones Recomendadas | Costo |
|---|---|---|---|---|---|
| 1 | Tarjeta ESP32 WROOM-32 | 1 | Controlador Principal de Sensores y Actuadores | 30 Pines, microUSB / USB-C | $120 |
| 2 | Tarjeta ESP32-CAM OV2640 | 1 | Transmisión de Video MJPEG en tiempo real | Incluye cámara OV2640 con conector FPC | $250 |
| 3 | Módulo GPS NEO-6M | 1 | Geolocalización y seguimiento en tiempo real | Comunicación UART, antena cerámica incluida | $95 |
| 4 | Sensor Ritmo Cardíaco MAX30102 | 1 | Medición de pulso / ritmo cardíaco | Interfaz I2C, sensor óptico de pulso | $85 |
| 5 | Motor de Vibración Moneda | 1 | Retroalimentación háptica / vibración en arnés | 3V - 5V DC, pin GPIO 16 | $15 |
| 6 | Servomotor SG90 9g | 1 | Compuerta dispensadora de premios | 5V, Frecuencia 50Hz, torque 1.8 kg-cm | $45 |
| 7 | Buzzer Pasivo 5V | 1 | Silbato auditivo / Alerta sonora | Tono de 2000 Hz por PWM | $10 |
| 8 | Sensor DHT11 | 1 | Monitoreo de Temperatura y Humedad | Módulo con resistencia pull-up integrada | $35 |
| 9 | Sensor MPU-6050 (GY-521) | 1 | Detección de Movimiento / Inclinación (Acelerómetro) | I2C (SDA/SCL), 3.3V | $40 |
| 10 | Fuente / Cable USB 5V (2A) | 1 | Alimentación estable para ambas placas | Evita caídas de voltaje en arranque de cámara/servo | $150 |
| 11 | Cables Jumper Dupont | 1 | Conexiones físicas del arnés | Hembra-Hembra y Macho-Hembra | $45 |
