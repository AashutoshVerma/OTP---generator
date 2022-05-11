import time # to use the time at which the script is executed
import smtplib # To use mail-sending protocol
from email.message import EmailMessage # to add the contents to the mail


otp=[]
mess=""
t=time.localtime()
hr=t.tm_hour
min=t.tm_min
sec=t.tm_sec
if(hr<10 ):
    hr=str(hr)
    hr=(hr+"0")
if( min<10 ):
    min=str(min)
    min=(min+"0")
if( sec<10):
    sec=str(sec)
    sec=(sec+"0")
hr=int(hr)
min=int(min)

int(sec)
otp.append(str(hr+min))
otp.append(str(min))
otp.append(str(sec+hr))

mess=mess.join(otp)

# The basic logic behind generating the OTP which is used in above function is that it uses the time at which 
# the script is generated and alters it with some algorithm(it's simple you will get see the code carefully :) )
    



# for i in range(20): # Here's the fun part if you want to prank your friend just uncomment this for-loop and ident the below codes, and boom it will shower OTP for your friend. 

msg=EmailMessage()
msg['Subject']='Test OTP'   
msg['From']='From-email'
msg['To']='To-email'
msg.set_content(f'Your OTP :{mess} is successfully delivered!!')
server= smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("From-email","password")
server.send_message(msg)
server.quit()


        
