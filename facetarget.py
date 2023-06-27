import serial
import numpy as np 
import cv2
import time

vid = cv2.VideoCapture(1)
ArduinoSerial=serial.Serial('COM3',9600,timeout=0.1)
time.sleep(1)

yuz_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while(True):    
    ret,frame = vid.read()
    gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    yuzler = yuz_cascade.detectMultiScale(gray,1.3,5)

    print(yuzler)

    for (x,y,w,h) in yuzler:
       #location = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),2)
       location ='X{0:d}Y{1:d}'.format((x+w//2),(y+h//2))
       ArduinoSerial.write(location.encode('utf-8'))
       cv2.circle(frame,(x+w//2,y+h//2),2,(255,255,255),2)
       cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
       cv2.putText(frame, 'FACE TARGET ' ,(370,50),cv2.FONT_HERSHEY_COMPLEX,  1,(255,255,255),2,cv2.LINE_AA)
       
    cv2.imshow('Melih OZASLAN',frame)
    
    if(cv2.waitKey(1) & 0xFF == ord('a')):
        break

vid.release()
cv2.destroyAllWindows()
