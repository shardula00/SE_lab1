import random
import smtplib
from email.message import EmailMessage


# for i in range(6):
#     otp += str(random.randint(0,9))
# Generate a random OTP with 4 to 8 digits
otp = str(random.randint(1000, 99999999))


server=smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

from_mail='ankushpagarwar5@gmail.com'
server.login(from_mail,'dlej ezot frtl sqbc')
to_mail=input("Enter your email: ")
msg=EmailMessage()
msg['Subject']="OTP Verification"
msg['From'] =from_mail
msg['To'] =to_mail
msg.set_content("Your OTP is : "+otp)
server.send_message(msg)
print("Verify OTP")
input_otp=input("Enter your OTP: ")
if input_otp==otp:
    print("OTP Verified")
else :
    print("Invalid OTP")