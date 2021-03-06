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
    retRobot = getImage('naoSouRobo.png', 'N', 'N')
    if retRobot == True:
        print('Tem Robo para Checar')
        retCheckRobot = getImage('checkNaoSouRobo.png')

        time.sleep(2)
        retVerify = getImage('verificarCheck.png')
    
    return True

def getPositionInit():
    sc = pyautogui.screenshot(region=(2000,300,450,200))
    width, height = sc.size

    positionX = False;
    positionY = False;

    for x in range(0, width, 1):
        for y in range(0, height, 1):
            r, g, b = sc.getpixel((x, y))
            if r == 0 and g == 179 and b == 60:
                positionX = 2000+x
                positionY = 300+y
                break 

    return positionX, positionY

def getPositionClose():
    sc = pyautogui.screenshot(region=(1930,70,570,70))
    width, height = sc.size

    positionX = False;
    positionY = False;

    for x in range(0, width, 1):
        for y in range(0, height, 1):
            r, g, b = sc.getpixel((x, y))
            if (r == 250 or r == 255) and (g == 250 or g == 255):
                positionX = 1930+x
                positionY = 70+y
                break 

    return positionX, positionY

while True:
    # pyautogui.displayMousePosition()
    # sc = pyautogui.screenshot(region=(1930,70,570,70))
    # sc.save('novoImagem.png')
    # print('FINALIZOU PRINT')
    # time.sleep(5)
    
    print('Inalisando Não sou Robô')
    # checkNotRobot()

    # Começar Assitir Anúncio
    print('Iniciando Abertura do Anúncio')
    x, y = getPositionInit()
    if x == False or y == False:
        time.sleep(2)
        continue
    pyautogui.click(x, y)

    # Fechar Anúncio
    time.sleep(15)
    print('Iniciando Fechamento do Anuncio')
    finished = False
    while(finished == False):
        time.sleep(5)

        x, y = getPositionClose();
        if(x == False or y == False):
            print('Nao encontrado X')
            posX, posY = getPositionInit()
            if posX == False and posY == False:
                continue
            
            finished = True
            continue

        print('Encontrado X')
        pyautogui.click(x, y)
        continue

    time.sleep(2)