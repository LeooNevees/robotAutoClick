import pyautogui
import time
import os
import dlib
import cv2
import glob

class Proccess:

    def getObject(self, svm, moveMouse = 'N', click = 'S', increment = 5):
        try:
            print('Iniciou GetObject')
            fileSvm = "files/" + str(svm)
            filePrint = "files/temp/print.png"

            # Detectando o SVM fornecido
            if(os.path.isfile(fileSvm) == False):
                raise Exception("Arquivo SVM não encontrado: " + str(svm))

            # Apagar o print da tela caso exista
            if(os.path.isfile(filePrint)):
                os.remove(filePrint)

            # Tirar print da imagem (tela inteira)
            pyautogui.screenshot(filePrint)

            detector = dlib.simple_object_detector(fileSvm)

            for imagem in glob.glob(os.path.join("files/temp", "print.png")):
                img = cv2.imread(imagem)
                objetosDetectados = detector(img, 2)
                if not objetosDetectados:
                    return None

                for d in objetosDetectados:
                    e, t, d, b = (int(d.left()), int(d.top()),
                                int(d.right()), int(d.bottom()))
                    # cv2.rectangle(img, (e, t), (d, b), (0, 255, 0), 2)
                    # print(str(e) + ' - ' + str(t))
                    # pyautogui.click(int(e) + 5, int(t) + 5)
                    x = int(e) + int(increment)
                    y = int(t) + int(increment)
                    if moveMouse == 'S':
                        pyautogui.moveTo(x, y)

                    if click == 'S':
                        pyautogui.click(x, y) 
                    print('Finalizou GetObject')

                # cv2.imshow("Detector", img)
                # cv2.waitKey(0)

            # cv2.destroyAllWindows()

            return True
        except Exception as error:
            print('Erro Método getObject: ', error)
            return False

    def getImage(self, file, moveMouse = 'N', click = 'S'):
        try:
            img = cv2.imread("files/" + str(file)) 
            button = pyautogui.locateOnScreen(img)
            if button == None:
                return None

            localizationButton = pyautogui.center(button)
            x, y = localizationButton

            if moveMouse == 'S':
                pyautogui.moveTo(x, y)

            if click == 'S':
                pyautogui.click(x, y) 

            return True
        except Exception as error:
            print('Erro Método getImage: ', error)
            return False

    def checkNotRobot(self):
        try:
            # retRobot = self.getObject("imNotRobot.svm")
            # if(retRobot == False):
            #     raise Exception("Não foi possível identificar se possui robô para checar")
            
            # if(retRobot == None):
            #     return True

            # retCheckRobot = self.getImage('checkImNotRobot.png')
            # if(retCheckRobot != True):
            #     raise Exception("Não identificado check Robô")

            time.sleep(5)
            retVerify = self.getObject("verifyCheckRobot.svm", 'N', 'S', 40)
            if(retVerify != True):
                raise Exception("Não encontrado botão de Verificar")

            return True
        except Exception as error:
            print('Erro Método checkNotRobot: ', error)
            return False

