# Escáner de Puertos Avanzado

Escáner de puertos que permite escanear un rango de puertos en una IP específica.

## Características

- Escanea un rango de puertos (inicial a final)
- Muestra solo los puertos abiertos
- Guarda los resultados en `resultados.txt`
- Timeout de 5 segundos por puerto

## Cómo usarlo

```bash
python escanearPuertosActualizado.py

## EJEMPLO

Ingrese direccion IP que desea escanear: 127.0.0.1
Ingrese puerto inicial para escanear: 135
Ingrese puerto final para escanear: 140

--- INICIANDO ESCANEO ---
El puerto 135 en 127.0.0.1 esta ABIERTO
Puerto 135 ABIERTO
Total de puertos abiertos: 1
Resultados guardados en resultados.txt
--- FINALIZACION DEL ESCANEO ---

Requisitos

    Python 3.x

    Módulo socket (incluido)

Autor

[Ing. Eduardo Celis]
