# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt



# Load an color image in grayscale
# img2=mpimg.imread('Banda2.png',0)
img = cv2.imread('Banda50.png',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#promedio columna
promedio = np.mean(img, axis=0)
plt.figure(1)
plt.plot(promedio)
plt.show()
#deteccion de bordes
d=np.diff(promedio);
plt.plot(d)
plt.show()
tam=len(d)-1
k=1
D=[0]*tam
for i in range(1,tam):
    if d[i]*d[i-1]>0:
        D[k]=D[k]+d[i]
    else:
        k=i
"Obteniendo el umbral "
uj=img.min(0);
vi=img.min(1);
 
dau=np.mean(promedio-uj);
dav=np.mean(promedio)-np.mean(vi);
"Se crea un array para seleccionar el minimo"
minimos=np.array([dau,dav]);
minimo=minimos.min();
umbral=np.mean(promedio)-minimo;

Mat=np.copy(img);
Mat[img>umbral]=1;
Mat[img<umbral]=0;
plt.figure(2)
plt.imshow(img,cmap='gray')
plt.figure(3)
plt.imshow(Mat,cmap='hot')

#pruebas
