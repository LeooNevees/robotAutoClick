import os
import dlib
import cv2
import glob
import pyautogui

# Apagar o print da tela caso exista
if(os.path.isfile("files/temp/print.png")):
    os.remove("files/temp/print.png")

# Tirar print da imagem (tela inteira)
pyautogui.screenshot("files/temp/print.png")

detector = dlib.simple_object_detector("files/closeButtons.svm")

for imagem in glob.glob(os.path.join("files/temp", "print.png")):
    img = cv2.imread(imagem)
    objetosDetectados = detector(img, 2)

    for d in objetosDetectados:
        e, t, d, b = (int(d.left()), int(d.top()), int(d.right()), int(d.bottom()))
        cv2.rectangle(img, (e,t), (d, b), (0,255,0), 2)
        print (str(e) + ' - ' + str(t))
        pyautogui.click(int(e) + 5, int(t) + 5)

    # cv2.imshow("Detector", img)
    cv2.waitKey(0)

cv2.destroyAllWindows()

