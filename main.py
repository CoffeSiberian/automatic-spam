from pyautogui import press, hotkey
from pyperclip import copy
from time import sleep
from json import loads

def openConfig():
    with open('config.json', 'r', encoding='utf-8') as json_file:
        data = loads(json_file.read())
        json_file.close()
        return data

def process(msj: str, time: int):
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
By: SiberianCoffe
https://github.com/CoffeSiberian
*************************

Message to send: {configs["msj"]}

Each {configs["delay"]} minutes
    ''')

    process(configs["msj"], configs["delay"])

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()