import smtplib
import os
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body):
    sender_email = os.getenv('GMAIL_USER')
    password = os.getenv('GMAIL_PASS')
    recipient_email = os.getenv('RECIPIENT_EMAIL')
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

if __name__ == "__main__":
    import sys
    input_data = json.loads(sys.stdin.read())
    
    name = input_data.get('client_payload', {}).get('name', 'No Name')
    mobile = input_data.get('client_payload', {}).get('mobile', 'No Mobile')
    email = input_data.get('client_payload', {}).get('email', 'No Email')
    message = input_data.get('client_payload', {}).get('message', 'No Message')
    
    subject = f"Contact Form Submission from {name}"
    body = f"Name: {name}\nMobile: {mobile}\nEmail: {email}\nMessage:\n{message}"
    
    send_email(subject, body)
