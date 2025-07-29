import cv2

cap= cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    small_frame = cv2.resize(frame, (640, 400))
    cv2.imshow('Webcam Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break       

cap.release()
cv2.destroyAllWindows()
