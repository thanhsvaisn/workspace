# Streaming Account Manager

Este proyecto proporciona un ejemplo sencillo de un sistema para gestionar
cuentas de servicios de streaming. Incluye una utilidad en Python para
agregar, eliminar, actualizar y listar cuentas almacenadas en un archivo JSON.

## Requisitos

- Python 3.8 o superior

## Uso

Ejecute la interfaz de línea de comandos:

```bash
python -m streaming_manager.manager add --username usuario1 --service netflix --plan basico
python -m streaming_manager.manager list
```

Los datos se almacenan en `accounts.json` por defecto. Puede especificar otro
archivo con el parámetro `--storage`.

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
python -m unittest discover -s streaming_manager/tests
```
