import cv2 as cv
import numpy as np
img = cv.imread(r'comida.jpg')
if img is None:
    print('Erro ao abrir a imagem.')
    exit()
print(f'Dimensões originais da imagem: {img.shape}')
max_dimension = 400
if img.shape[0] > max_dimension or img.shape[1] > max_dimension:
    scale = max_dimension / max(img.shape[0], img.shape[1])
    img = cv.resize(img, (int(img.shape[1] * scale), int(img.shape[0] * scale)))
    print(f'Imagem redimensionada para: {img.shape}')

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # converte para escala de cinza
suave = cv.GaussianBlur(img, (7, 7), 0) # aplica blur  
(T,bin) = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
(T, binI) = cv.threshold(suave, 160, 255, cv.THRESH_BINARY_INV) 
resultado = np.vstack([ np.hstack([suave, bin]), np.hstack([binI, cv.bitwise_and(img, img, mask = binI)]) ])  
cv.imshow(f'Imagem com aplicacao da escala de cinza e binarizacao', resultado)
cv.waitKey(0)
