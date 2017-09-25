# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("mailmefriends95@gmail.com", "priyan5143")

# message to be sent
message = "hello"

# sending the mail
s.sendmail("mailmefriends95@gmail.com", "helloitspriyan@gmail.com", message)

# terminating the session
s.quit()
