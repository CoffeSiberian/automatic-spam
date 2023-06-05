from pyautogui import press, hotkey
from pyperclip import copy
from time import sleep
from json import loads

def openConfig():
    with open('config.json', 'r', encoding='utf-8') as json_file:
        data = loads(json_file.read())
        json_file.close()
        return data

def bucle(msj: str, time: int):
    while True:
        sleep(time*60)
        try:
            press("y")
            copy(msj)
            hotkey('ctrl', 'v')
            press("enter")
        except:
            break

def main():
    configs = openConfig()
    print(f'''
*************************
Simple SPAM BOT
By: SiberianCoffe#1172
https://github.com/CoffeSiberian
*************************

Mensaje a enviar: {configs["msj"]}

Cada {configs["delay"]} minutos
    ''')

    bucle(configs["msj"], configs["delay"])

if __name__ == "__main__":
    try:
        main()
    except:
        exit()