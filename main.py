import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# Set up the SMTP server and use port 587 with starttls() for secure communication
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()  # Secure the connection
server.ehlo()      # Identify ourselves to the server

# Read the password from a file
with open('password.txt', 'r') as f:
    password = f.read().strip()

# Login to the server with your email and the read password
server.login('your_email@gmail.com', password)

# Create the email message
msg = MIMEMultipart()
msg['From'] = 'Your Name'
msg['To'] = 'recipient_email@gmail.com'
msg['Subject'] = 'Your Subject Here'

# Read the email body from a file
with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

# Attach a file to the email
filename = 'dragon.jpg'
with open(filename, 'rb') as attachment:
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

# Convert the message to a string and send the email
text = msg.as_string()
server.sendmail('your_email@gmail.com', 'recipient_email@gmail.com', text)

# Close the server connection
server.quit()
