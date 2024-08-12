import string      # to generate the password  
import random      # to generate secure and random password 

print("Welcome to PASSWORD GENERATOR:)")
letters=int(input("How many letters do you want ? \n"))
digit=int(input("How many digit do you want ? \n"))
symbol=int(input("How many symbol do you want ? \n"))

def gen():           
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation

    passlen = (letters + digit + symbol )   # taking input from user 
 
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
