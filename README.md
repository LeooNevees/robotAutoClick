# robotAutoClick

<!-- 

Para iniciar é necessário realizar as seguintes etapas: 

1° No site https://imglab.in/ se faz necessário selecionar com Retângulo o objeto que está buscando nas imagens selecionadas, após isso salvar no formato DLIB XML

2° Salvar esse XML na raiz do projeto;

3° No código fonte generationSvm.py é necessário alterar a linha 7, inserindo o nome do arquivo que salvou no projeto em XML (passo 1 e 2)

4° Após gerar o SVM é só fazer a utilização para a detecção das imagens conforme código exemplo a seguir:

OBS: Necessário manter as imagens utilizadas no SVM juntamente com o projeto

for imagem in glob.glob(os.path.join("img/procurar", "print.png")):
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

 -->