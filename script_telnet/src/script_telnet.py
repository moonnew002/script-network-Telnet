import asyncio
import telnetlib3
from asyncio import timeout
from telnetlib3 import telnetlib

from inventory import ROUTERS

async def configurar_routers(router):
    print(f"Configurando {router['hostname']}")
    try:
        reader, writer = await telnetlib3.open_connection(router["ip"], 23)
        salida_texto = ""
        await reader.readuntil(b"Username:")
        writer.write(router["username"] + "\r")

        await reader.readuntil(b"Password:")
        writer.write(router["password"] + "\r")

        try:
            await asyncio.wait_for(reader.readuntil(b">"), timeout=2.0)

            print(f"Login exitoso para el router {router['hostname']}")

            # await reader.readuntil(b">")
            writer.write("enable\r")

            await reader.readuntil(b"Password:")
            writer.write(router["password"] + "\r") # debido a que se configuro enable secret cisco

            await reader.readuntil(b"#")

            for comando in router["commands"]:

                print(f"{router['hostname']} - Enviando {comando}")
                writer.write(comando + "\r")

                salida_bytes = await reader.readuntil(b"#")
                await asyncio.sleep(0.5)
                salida_texto = salida_bytes.decode('ascii', errors='ignore')

            print(f"{router['hostname']} - Terminando")
            print(salida_texto)
            writer.close()

        except asyncio.TimeoutError:
            print(f"Autenticación fallida para {router['hostname']} verifique su usuario/contraseña")

        #writer.write("terminal length 0\r")
        #await reader.readuntil(b"#")
    except Exception as e:
        print(f"Error en {router['hostname']}: {e} - Verifique si el router tiene habilitado el servicio de Telnet o si la dirección IP es correcta")

async def main():
    tareas = []
    for router in ROUTERS:
        tarea = configurar_routers(router)
        tareas.append(tarea)
    print("Iniciando todas las configuraciones")
    await asyncio.gather(*tareas)

if __name__ == "__main__":
    asyncio.run(main())
