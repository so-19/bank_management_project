import random
import time
def otp():
    global otp
    global otpu
    otp=random.randint(10000,99999)
    print("you will receive an OTP on the screen,Type the OTP when asked")
    print("Your ONE TIME PASSWORD IS::::",otp)
    time.sleep(5)
    otpu=int(input('Enter the OTP you received:'))
otp()
if otp==otpu:
    print("You have entered inside")
