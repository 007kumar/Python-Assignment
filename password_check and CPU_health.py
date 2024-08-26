
import time # time modul to represent time. 
import psutil # psutil info about running process

def compUsage(cpu, bars=100):
    inPercent = (cpu/100.0) #will be divided by 100.0 to get output in .00
    cpuBars = '█' * int(inPercent*bars) + '-' * (bars -int(inPercent * bars))  

    #(((((we can provide f string to privide multiple parameters. print will 
    # show ouput of cpuBars and cpu. 2f decimal and 2 for 2 digit should be 
    # in output with floating value. Then after it will run on same line with end=""))))
    print(f"\r CPU_Usage: | | {cpuBars} | {cpu:.2f}%",end="")
    

    alert=cpu #Now alert contains cpu value and that can be used to run if condition for checking value of CPU.
    if (cpu > 80):  # now condition triggers if cpu corss 80 in cpu value 
        print("\n Alert! CPU usage has reached threshold :", cpu) #printing alert and current cpu value

while True:  # while below condition is true - to run loop continue

    compUsage(psutil.cpu_percent(),100) #cpu_percent will provide us information about cpu usage
    time.sleep(0.5) #to stop execution of loop for 0.5 seconds.


#--------------BELOW IS THE CODE TO CHECK SETTING UP PASSWORD AS PER REQUIREMENT-------------------

import re

print (""" " **  SET A MORE COMPLEX PASSWORD USING THE BELOW REQUIREMENTS   **\n
 " --- > 1) Minimum length of the password : more then 8 character\"
 " --- > 2) Use both Uppercase and Lowercase letters\"
 " --- > 3) Use at least one number (0-9)\"
 " --- > 4) Use at least one special character (eg !@#$%^&*.)} """)

def check_password_stength(password):
    print (" Set your Password using a above requirements - ")
def length(password) -> bool:
    return 8 < len(password)
def uppercase(password) -> bool:
    return bool (re.search('[A-Z]', password))
def lowercase(password) -> bool:
    return bool (re.search('[a-z]', password))
def number(password) -> bool:
    return bool (re.search('[0-9]', password))
def Special(password) -> bool:
    return bool (re.search('[~!@#$%^&*]', password))

password = input(" \n Please Set your new Password\n : ") # password input

if all([uppercase(password), lowercase(password), number(password), Special(password), length(password)]):

    print (" Password has been set Successully ")
else:
    print ("(( Increase complexity of your Password : Use information below ))")

    #every criteria will give output if not used in password using (if not)
    if not lowercase(password):
        print (" *Use at least one lowercase letter - ")
    
    if not uppercase(password):
        print (" *Use at least one uppercase letter - ")

    if not number(password):
        print (" *Use at least one number - ")

    if not Special(password):
        print (" *Use at least one special character -")
    
    if not length(password):
        print (" *Your Password must be more then 8 characters")


