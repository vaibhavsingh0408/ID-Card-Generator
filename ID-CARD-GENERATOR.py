#id card generator
import cv2
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.imread('template-idcard.png')
n=input('enter name')
cv2.putText(img,n,(110,62),font,1,(143,162,0),2)
i=input('enter ID')
cv2.putText(img,i,(150,105),font,1,(143,162,0),2)
f=input('enter father name')
cv2.putText(img,f,(150,155),font,1,(143,162,0),2)
cv2.imshow('i-card',img)
cv2.imwrite("generated-id-card.png",img)
cv2.waitKey(0)
