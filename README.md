# Automatic Spam

With this simple script you can send a message at a certain time interval automatically using your system clipboard.

## Poetry

First you will need to install Poetry to handle the project dependencies. You can follow the official documentation at: <https://python-poetry.org/docs/#installation>

## Build

Para poder crear tu propio binario ejecutable en tu sistema puedes utilizar el siguiente comando luego de instalar todas las dependencias

```bash
pyinstaller --clean main.py
```

Then you will need to copy the configuration file along with the resulting binary into `dist`

```bash
cp ./config.json ./dist/main/
```
