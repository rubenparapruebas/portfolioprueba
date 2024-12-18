---
layout: page
title: "Automatización con Netmiko"
permalink: /applications/netmiko-example/
---

# Automatización de Configuración de Routers con Netmiko

Esta aplicación es un script en Python que utiliza la biblioteca Netmiko para conectarse a un router Cisco y ejecutar comandos automáticamente.

## ¿Qué hace esta aplicación?
1. Se conecta a un router mediante SSH.
2. Ejecuta una serie de comandos predefinidos (por ejemplo, mostrar la configuración o aplicar cambios).
3. Guarda los resultados en un archivo local para revisión.

### Valor añadido
- **Eficiencia**: Ahorra tiempo al evitar configuraciones manuales.
- **Consistencia**: Reduce errores al aplicar configuraciones uniformes.
- **Escalabilidad**: Puede ampliarse para gestionar múltiples dispositivos.

Puedes descargar el código desde [GitHub aquí](https://github.com/rubenparapruebas/netmiko-example/blob/main/netmiko_example.py).

---

### **3. Crear el Código de la Aplicación**
Crea un archivo `netmiko_example.py` con el siguiente contenido:

```python
from netmiko import ConnectHandler

# Detalles del dispositivo
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',  # Cambia esto a la IP del router
    'username': 'hakai',
    'password': 'Changeme_123',
}

# Conexión al dispositivo
try:
    connection = ConnectHandler(**device)
    print(f"Conectado a {device['host']}")

    # Ejecutar comandos
    output = connection.send_command('show running-config')
    print("Configuración actual obtenida.")
    
    # Guardar la configuración en un archivo
    with open('running_config.txt', 'w') as file:
        file.write(output)
    print("La configuración se ha guardado en 'running_config.txt'.")

    # Cerrar la conexión
    connection.disconnect()
    print("Conexión cerrada.")

except Exception as e:
    print(f"Error: {e}")
