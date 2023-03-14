# importing necessary modules
import math
import random
import smtplib


# generating random 6-digit otp
digits = "0123456789"
OTP = ""
for i in range(6):
    OTP = OTP + digits[math.floor(random.random()*10)]
message = OTP + " is your OTP"


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("thecoderguy111@gmail.com", "qnqv vkit aijs zhsz")
email = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&', email, message)


# verifying otp
passcode = input("Enter your OTP: ")
if passcode == OTP:
    print("Verified")
else:
    print("Invalid OTP")