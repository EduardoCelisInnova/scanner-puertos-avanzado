import socket

def pruebaPuerto(host, port):
    # (tu función actual, no la toques)
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(5)
    # Devuelve True si está abierto, False si no
    try:
        cliente.connect((host, port))
        print(f"El puerto {port} en {host} esta ABIERTO")
        return True
    
            
    except:
        print(f"El puerto {port} en {host} esta CERRADO.")
        return False
    
    finally:
        cliente.close()

# Pedir IP
ip = input("Ingrese direccion IP que desea escanear: ")

# Pedir puerto_inicial
puertoInicial = int(input("Ingrese puerto inicial para escanear: "))

# Pedir puerto_final
puertoFinal = int(input("Ingrese puerto final para escanear: "))
listarPuertos = puertoInicial, puertoFinal

abiertos = []  # lista vacía para guardar resultados

print("--- INICIANDO ESCANEO ---")

# Bucle for desde inicial hasta final
for puerto in range (puertoInicial, puertoFinal +1):
#   llamar a pruebaPuerto
    if pruebaPuerto(ip, puerto):
        print(f"Puerto {puerto} ABIERTO")
        abiertos.append(puerto)
    
# Al final, mostrar cuántos abiertos encontraste (len(abiertos))
print(f"Total de puertos abiertos: {len(abiertos)}")

# Guardar abiertos en un archivo
with open('resultados.txt', 'w', encoding='utf-8') as archivo:
    for p in abiertos:
        archivo.write(str(p)+"\n")
        
    print("Resultados guardados en resultados.txt")

print("--- FINALIZACION DEL ESCANEO ---")

    
