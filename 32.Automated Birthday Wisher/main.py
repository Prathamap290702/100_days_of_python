import smtplib
from email.message import EmailMessage

MY_EMAIL = "smtptesting400@yahoo.com"
MY_PASSWORD = "RIOhR'x|F-7_K~5"

msg = EmailMessage()
msg["Subject"] = "Hello"
msg["From"] = MY_EMAIL
msg["To"] = "prathamap2002@gmail.com"
msg.set_content("Hello, this is a test email.")

try:
    with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as connection:
        # Rest of the code
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.send_message(msg)
        print("Email sent successfully!")
except smtplib.SMTPAuthenticationError:
    print("Authentication failed. Please double-check your email address and password.")
except smtplib.SMTPException as e:
    print("An error occurred while sending the email:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
