import cv2
import numpy as np

img = np.zeros((400,600), dtype=np.uint8)
img[100:300,200:400] = 255
img2 = np.zeros((400,600),dtype=np.uint8)
img2 = cv2.circle(img2,(300,200),125,(255), -1)

AND = cv2.bitwise_and(img,img2)
NOT = cv2.bitwise_not(img2)
OR = cv2.bitwise_or(img, img2)
XOR = cv2.bitwise_xor(img, img2)


cv2.imshow('IMAGEN 1', img)
cv2.imshow('IMAGEN 2', img2)
cv2.imshow('AND SOBRE LAS DOS IMAGENES', AND)
cv2.imshow('NOT SOBRE LA IMAGEN 2', NOT)
cv2.imshow('OR SOBRE LAS DOS IMAGENES',OR)
cv2.imshow('XOR SOBRE LAS DOS IMAGENES', XOR)
cv2.waitKey(0)
cv2.destroyAllWindows()