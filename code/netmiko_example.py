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