import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formataddr
from email.mime.base import MIMEBase
from email import encoders
from django.conf import settings
import os
from django.conf import settings
from decouple import config

smtp_password = settings.EMAIL_HOST_PASSWORD
smtp_user = settings.EMAIL_HOST_USER
smtp_port = settings.EMAIL_PORT
smtp_server = settings.EMAIL_HOST
sender_email = config("SENDER_EMAIL")
sender_name = config("SMTP_SENDER_NAME")


# Function to send email
def send_email(
        subject,
        receiver_name, 
        message,
        receiver_email=config("RECEIVER_EMAIL"),
    ):
    # Create the root message
    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = formataddr((receiver_name, receiver_email))
    
    # Create the HTML part
    html = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f6f6f6;
            }}
            .email-container {{
                max-width: 600px;
                margin: 20px auto;
                background-color: #ffffff;
                padding: 20px;
                border: 1px solid #e0e0e0;
            }}
            .header {{
                text-align: center;
                padding: 20px 0;
            }}
            .content {{
                font-size: 16px;
                line-height: 1.5;
                color: #333333;
            }}
            .footer {{
                text-align: center;
                font-size: 12px;
                color: #aaaaaa;
                padding: 20px 0;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            
            <div class="content">
                <p>Dear {receiver_name},</p>
                <p>{message}</p>
                <p>Best regards,<br>E-Vote</p>
            </div>
            <div class="footer">
                <p>&copy; E-Vote 2024. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """
    msg_html = MIMEText(html, 'html')
    msg.attach(msg_html)
    # try:
    
    # Send the email via SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(smtp_user, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Mail is sending")




