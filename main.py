import cv2
#loadind cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#reading the input image
img = cv2.imread('abba.png')
#detecting face
faces = face_cascade.detectMultiScale(image=img, scaleFactor=1.1, minNeighbors=4)
#face cover
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w, y+h),(255,0,0),2)

#result
cv2.imwrite("face_detected.png",img)
print("successfully saved")