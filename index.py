from queue import Empty
import string
from tabnanny import check
from tokenize import String
import pyautogui
import time


def getImage(file, moveMouse='N', click='S'):
    button = pyautogui.locateOnScreen("img/"+str(file))
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


try:

    while True:
        # Verificar se existe Não sou Robô na tela
        checkNotRobot()

        # Começar Assitir Anúncio
        retInit = getImage('botaoAssitirVideo.png')
        if retInit == False:
            time.sleep(2)
            continue

        # Fechar Anúncio
        time.sleep(15)
        print('Iniciando Fechamento do Anuncio')
        finished = False
        while(finished == False):
            time.sleep(5)

            for a in [1, 2, 3]:
                nameImage = ">>" + str(a)
                print('Buscando a imagem: ' + str(nameImage))
                retFirstStage = getImage(str(nameImage) + '.png')
                if retFirstStage == True:
                    print('Imagem >> encontrado. Finalizando processo')
                    break

            time.sleep(5)
            pyautogui.moveTo(1000, 500)

            for a in [1, 2, 3, 4]:
                nameImage = "x" + str(a)
                print('Buscando a imagem: ' + str(nameImage))
                retSecondStage = getImage(str(nameImage) + '.png')
                if retSecondStage == True:
                    print('Imagem x encontrado. Finalizando processo')
                    finished = True
                    break

            continue

        time.sleep(2)

except Exception as error:
    print('Erro: ', error)
    pyautogui.screenshot('Exception.png')
