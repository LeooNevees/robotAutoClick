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
        retInit = classProccess.getObject("buttonInit.svm", 'N', 'S', 50)
        if(retInit == False):
            raise Exception("Erro ao tentar localizar botão de abertura anúncio")
        if(retInit == None):
            time.sleep(2)
            continue
        
        # Fechar Anúncio
        time.sleep(15)
        finished = False
        while(finished == False):
            time.sleep(5)

            print('Iniciando Fechamento do Anuncio')
            closeButton = classProccess.getObject("closeButtons.svm")
            if(closeButton == False):
                raise Exception("Erro ao tentar localizar fechamento anúncio")

            if(closeButton == None):
                print('Iniciando verificação da página de Início')
                retNewInit = classProccess.getObject("buttonInit.svm", 'N', 'N')
                if(retNewInit == True):
                    print('Botão de Iniciar anúncio encontrado. Fim do processo')
                    finished = True
                    break

                print('Iniciando verificação da página de Robô')
                retNewRobot = classProccess.verifyImNotRobot()
                if(retNewInit == True):
                    print('Verificação de Eu não sou Robô encontrado. Fim do processo')
                    finished = True
                    break
                
                continue

            pyautogui.moveTo(1000, 500)

        time.sleep(2)

except Exception as error:
    print(error)
    # pyautogui.screenshot('files/Exception.png')
