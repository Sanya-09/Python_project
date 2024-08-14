import cv2

imgcapture = cv2.VideoCapture(0)
result = True

while(result):
    ret, frame = imgcapture.read()
    cv2.imwrite("pic.jpg", frame)
    result = False
    print("Image Captured...")

imgcapture.release()
