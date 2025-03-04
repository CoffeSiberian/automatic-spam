from pyautogui import press, hotkey
from pyperclip import copy
from time import sleep
from json import loads

def openConfig():
    with open('config.json', 'r', encoding='utf-8') as json_file:
        data = loads(json_file.read())
        json_file.close()
        return data
    
def printConfig(msj1: str, msj2: str, time: int):
        print(f'''
*************************
Simple SPAM BOT
By: SiberianCoffe
https://github.com/CoffeSiberian
*************************

Message to send 1: {msj1}
Message to send 2: {msj2}

Each {time} minutes
    ''')

def process(msj1: str, msj2: str, time: int):
    second_active_message = False

    while True:
        if second_active_message:
            copy(msj2)
            second_active_message = False
        else:
            copy(msj1)
            second_active_message = True

        sleep(time*60)
        try:
            press("y", interval=0.5)
            hotkey('ctrl', 'v', interval=0.5)
            press("enter", interval=0.5)
        except Exception as e:
            print(f"An error occurred: {e}")
            break

def main():
    configs = openConfig()

    printConfig(configs["msj1"], configs["msj2"], configs["delay"])
    process(configs["msj1"], configs["msj2"], configs["delay"])

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()