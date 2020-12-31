import cv2
path=r'C:\Users\DARSHAN\Downloads\documents\dhiva-krishna-yXmjBxvkoG4-unsplash.jpg'
image = cv2.imread(path)
grey_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert=cv2.bitwise_not(grey_img)
blur=cv2.GaussianBlur(invert,(21,21),0)
invertedblur=cv2.bitwise_not(blur)
sketch=cv2.divide(grey_img,invertedblur, scale=256.0)
cv2.imwrite("sketch.png",sketch)