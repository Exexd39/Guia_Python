"""
==================================================================================================
Tienes un registro de quién intentó entrar al servidor. 
Tu trabajo es detectar quiénes fallaron la contraseña para reportarlos.
==================================================================================================
OBJETIVO:
Necesito que crees un patrón Regex que capture solo dos cosas de cada línea:
1.- El nombre del usuario (Ej: Exequiel).
2.- El estado (Ej: Success o Failed).
==================================================================================================
"""

# Importacion
import re

# Datos #
logs_acceso = """
[User: Exequiel] Status: Success
[User: Admin01] Status: Success
[User: Hacker123] Status: Failed
[User: GuestUser] Status: Success
[User: Bot_X99] Status: Failed
"""

# Patron #
# se debe capturar los nombres y los estados
patron_0 = r"\[.+: (\w+)] .+: (\w+)"
log_correcto = re.findall(patron_0, logs_acceso)
#print(log_correcto)

for a in log_correcto:
    usuario = a[0]
    estado = a[1]

    if (estado == "Failed"):
        print(f"ALERTA, usuario: {usuario}. Es un intruso >:c")
    else:
        print(f"Usuario {usuario} Puede pasar jeje :D")