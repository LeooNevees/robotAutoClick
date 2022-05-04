from queue import Empty
from tabnanny import check
import pyautogui
import time

def getImage(file, moveMouse = 'N', click = 'S'):
    button = pyautogui.locateOnScreen(file)
    if button == None:
        return False

    localizationButton = pyautogui.center(button)
    x, y = localizationButton

    if moveMouse == 'S':
        pyautogui.moveTo(x, y)

    if click == 'S':
        pyautogui.click(x, y) 

    return True

def checkNotRobot():
    print('Iniciou Checagem Robo')
    retRobot = getImage('naoSouRobo.png', 'N', 'N')
    if retRobot == True:
        print('Tem Robo para Checar')
        retCheckRobot = getImage('checkNaoSouRobo.png')

        time.sleep(2)
        retVerify = getImage('verificarCheck.png')
    
    return True

def getPosition():
    sc = pyautogui.screenshot(region=(2030,60,490,180))
    width, height = sc.size

    positionX = False;
    positionY = False;

    for x in range(0, width, 1):
        for y in range(0, height, 1):
            r, g, b = sc.getpixel((x, y))
            if (r == 250 or r == 255) and (g == 250 or g == 255):
                positionX = 2030+x
                positionY = 60+y
                break 

    return positionX, positionY

while True:
    checkNotRobot()

    # Começar Assitir Anúncio
    retInit = getImage('botaoAssitirVideo.png')
    if retInit == False:
        time.sleep(2)
        continue

    # Fechar Anúncio
    print('Iniciando Fechamento do Anuncio')
    contador = 0
    finished = False
    while(finished == False):
        time.sleep(5)

        x, y = getPosition();
        print(x, y)
        if(x == False or y == False):
            print('Nao encontrado X')
            retInit = getImage('botaoAssitirVideo.png')
            if retInit == False:
                continue

            finished = True
            continue

        print('Encontrado X')
        pyautogui.click(x, y)
        contador = contador + 1

        if(contador == 2):
            finished = True

        continue

    time.sleep(2)