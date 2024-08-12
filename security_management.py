# SECURITY MANAGEMENT PROJECT 

import string      # to generate the password  
import random      # to generate secure and random password 
import cv2         # to use image in face detection 

print("SECURITY MANAGEMENT \n 1. PASSWORD GENERATOR \n 2.FACE DETECTION \n \n")

print("\nWelcome to PASSWORD GENERATOR:)")

letters=int(input("How many letters do you want ? "))

digit=int(input("How many digit do you want ? "))

symbol=int(input("How many symbol do you want ? "))

def gen():           
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation

    passlen = (letters + digit + symbol )   # taking input from user 
    print("Lenght of the password is-" , passlen)

    password_list= []

    for i in range(1,letters+1):
        char=random.choice(s1)
        password_list += char

    for i in range(1,digit+1):
        int =random.choice(s2)
        password_list += int
 
    for i in range(1,symbol+1):
        char =random.choice(s3)
        password_list += char

    random.shuffle(password_list)   
    password=''
    for char in password_list:           # converting list into string 
        password += char
    print("The auto generated password is :" ,password)     # the auto generated secure and random password as an output 

gen()

print(" \n \n \n  ")
print("FACE DETECTION APP")
print("\n")
print("Wait for 5 seconds :)")
print("Press space to exit")
print("\n")

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
print("Face Detected!")
print("Presentesd by SANYA AGARWAL")
