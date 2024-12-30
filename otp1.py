import random
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def is_valid_email(email):
    # Regular expression to validate email
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

def generate_otp():
    # Generate a random OTP with 4 to 8 digits
    return str(random.randint(1000, 99999999))

def send_otp(email):
    if not is_valid_email(email):
        print("Invalid email address.")
        return

    otp = generate_otp()
    
    # SMTP configuration (use your email service provider's details)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "ankushpagarwar5@gmail.com"
    sender_password = "blus flvn dhfq yutq"

    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = email
        message["Subject"] = "Your One-Time Password (OTP)"

        body = f"Your one-time password (OTP) is: {otp}\n\nPlease do not share this OTP with anyone."
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message.as_string())
        server.quit()

        print(f"OTP sent successfully to {email}")
        print("Verify OTP")
        input_otp=input("Enter your OTP: ")
        if input_otp==otp:
          print("OTP Verified")
        else :
         print("Invalid OTP")
        
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    recipient_email = input("Enter the recipient's email address: ")
    send_otp(recipient_email)
