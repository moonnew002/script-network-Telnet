import os
from dotenv import load_dotenv

# 1. Cargar las variables del archivo .env
load_dotenv()

# 2. Leer las credenciales (Si no existen, devuelve None o un error controlado)
USERNAME = os.getenv("ROUTER_USER")
PASSWORD = os.getenv("ROUTER_PASSWORD")

# 3. Definir el inventario
# Nota cómo usamos las variables USERNAME y PASSWORD en lugar de escribir "cisco"
ROUTERS = [
    {
        "hostname": "R1",
        "ip": "192.168.56.3",
        "username": USERNAME,
        "password": PASSWORD,
        "commands": [
            "configure terminal",
            "interface f1/0",
            "description Configurado desde Python Modular",
            "ip address 192.168.2.1 255.255.255.252",
            "no shutdown",
            "do show ip int brief"
        ]
    },
    {
        "hostname": "R2",
        "ip": "192.168.56.4",
        "username": USERNAME,
        "password": PASSWORD,
        "commands": [
            "configure terminal",
            "interface f1/0",
            "description Configurado desde Python Modular",
            "ip address 192.168.2.2 255.255.255.252",
            "no shutdown",
            "do show ip int brief"
        ]
    }
]