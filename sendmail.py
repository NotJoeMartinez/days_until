import smtplib, ssl
import config

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = config.sender_email 
receiver_email = config.reciver_email  
password = config.password

message = """


"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)