import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
#img = cv2.imread('test.png')
cap = cv2.VideoCapture('http://192.168.1.44/jpg/image.jpg')

while cap.isOpened():

    cap = cv2.VideoCapture('http://192.168.1.44/jpg/image.jpg')
    ret, img = cap.read()

    faces = face_cascade.detectMultiScale(img, 1.1, 4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 1)

    # Display the output
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()


while(True):
    cap = cv2.VideoCapture('http://192.168.1.44/jpg/image.jpg')
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break