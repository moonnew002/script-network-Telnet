## Configuración automática de la red mediante Telnet 


Script en Python para automatizar la configuración básica de routers mediante Telnet usando programación asíncrona.  
Proyecto académico desarrollado para la materia "Temas Selectos de Redes de Computadoras"

Telnet se usa solo con fines educativos. En entornos reales debe preferirse SSH.

## Características

- Automatización de configuración de múltiples routers.
- Conexiones Telnet concurrentes usando 'asyncio'.
- Manejo seguro de credenciales mediante variables de entorno.
- Arquitectura modular ('inventory' + 'executor')


## Instalación:

Crea un entorno virtual:

python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

Instala dependencias:

pip install -r requirements.txt

## Configuración de credenciales:

1. Copia el archivo de ejemplo:
cp .env.example .env

2. Edita .env:
ROUTER_USER=usuario
ROUTER_PASSWORD=contraseña

3. Ejecución:
Desde la raíz del proyecto:
python -m src.script_telnet
El script conectará a cada router definido en inventory.py y ejecutará la lista de comandos.

## Licencia:

MIT License.

## Autor

Erick Luna.
Estudiante de computación.
Proyecto académico.


