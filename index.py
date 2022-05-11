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
        pyautogui.moveTo(1000, 500)
        print('Retorno do botao iniciar')
        print(retInit)
        if(retInit == False):
            raise Exception("Erro ao tentar localizar botão de abertura anúncio")
        if(retInit == None):
            time.sleep(2)
            continue
        

        # Fechar Anúncio
        print('Iniciando Fechamento do Anuncio')
        time.sleep(15)

        finished = False
        while(finished == False):
            time.sleep(5)

            closeButton = classProccess.getObject("closeButtons.svm")
            print('Retorno Busca por Botão de Fechar')
            print(closeButton)
            if(closeButton == False):
                raise Exception("Erro ao tentar localizar fechamento anúncio")

            if(closeButton == None):
                print('Entrou no if do closeButton = NONE')
                retNewInit = classProccess.getObject("buttonInit.svm", 'N', 'N')
                print('Retorno Busca por Botão de INICIAR')
                print(retNewInit)
                if(retNewInit == True):
                    print('Entrou no IF de botão de iniciar TRUE')
                    finished = True
                    break
                continue

            pyautogui.moveTo(1000, 500)

        time.sleep(2)

except Exception as error:
    print(error)
    # pyautogui.screenshot('files/Exception.png')
