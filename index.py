from fileinput import close
import os
import time
import pyautogui

from services.Proccess import Proccess

try:
    classProccess = Proccess()

    while True:
        # Verificar se existe Não sou Robô na tela
        print('Iniciando análise Não Sou Robô')
        retNotRobot = classProccess.checkNotRobot()
        if(retNotRobot == False):
            raise Exception("Erro ao checar Não sou Robô")

        # Começar Assitir Anúncio
        print('Iniciando Abertura do Anúncio')
        retInit = classProccess.getObject("buttonInit.svm", 'N', 'S', 40)
        if(retInit == False):
            raise Exception(
                "Erro ao tentar localizar botão de abertura anúncio")
        if(retInit == None):
            time.sleep(2)
            continue

        # Fechar Anúncio
        time.sleep(15)
        finished = False
        contador = 0
        while(finished == False):
            time.sleep(5)
            int(contador) + 1

            print('---------Iniciando Fechamento do Anuncio---------')
            closeButton = classProccess.getObject("closeButtons.svm")
            if(closeButton == False):
                raise Exception("Erro ao tentar localizar fechamento anúncio")

            if(closeButton == None):
                print('Iniciando verificação da página de Início')
                retNewInit = classProccess.getObject(
                    "buttonInit.svm", 'N', 'N')
                if(retNewInit == True):
                    print('Botão de Iniciar anúncio encontrado. Fim do processo')
                    contador = 0
                    finished = True
                    break

                print('Iniciando verificação da página de Robô')
                retNewRobot = classProccess.verifyImNotRobot()
                if(retNewInit == True):
                    print('Verificação de Eu não sou Robô encontrado. Fim do processo')
                    contador = 0
                    finished = True
                    break

                print('Iniciando verificação da Google Play')
                retGooglePlay = classProccess.checkGooglePlay()
                if(retGooglePlay == False):
                    raise Exception("Erro no processo Google Play")

            pyautogui.moveTo(1000, 500)
            if(int(contador) == 15):
                raise Exception(
                    "Não foi encontrado nenhuma etapa do processo. Finalização forçada")

        time.sleep(2)

except Exception as error:
    print(error)
    pyautogui.screenshot('files/temp/Exception.png')
