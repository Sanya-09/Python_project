import cv2
face_cascade_name = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier()
if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print("Error loading xml file")
def detect():
    cap = cv2.VideoCapture(0)

    while True:
        _,img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        face = face_cascade.detectMultiScale(gray, 1.1 , 4)

        for(x,y,w,h) in face:
            cv2.rectangle(img, (x,y), (x+w , y+h), (255,0,0), 2)

        cv2.imshow("Face Detect", img)

        key = cv2.waitKey(0)
        if key == ord(' '):
            break 

    cap.release()

detect()
