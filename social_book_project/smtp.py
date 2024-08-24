import smtplib
from email.mime.text import MIMEText

# Email details
sender_email = 'arun@gmail.com'  # Replace with your Gmail address
password = '122112211'         # Replace with your App Password
receiver_email = 'arunn'  # Replace with recipient's email
subject = 'Test Email'
body = 'This is a test email from Django.'

# Create the email message
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    print('Email sent successfully!')
except Exception as e:
    print(f'Error: {e}')
