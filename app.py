from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)
load_dotenv()
CORS(app)  # Allow requests from all origins

# Get the environment variables
app.config['API_PASSWORD'] = os.environ.get('API_PASSWORD')

def send_email(sender_email, sender_account_app_password, receiver_emails, subject, body, files=[]):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(receiver_emails)
    message['Subject'] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))

    # Attach files
    for file in files:
        attachment = MIMEBase('application', 'octet-stream')
        with open(file, "rb") as f:
            attachment.set_payload(f.read())
        encoders.encode_base64(attachment)
        filename = os.path.basename(file)  # Extracting only the filename from the full filepath
        attachment.add_header('Content-Disposition', f'attachment; filename= {filename}')
        message.attach(attachment)

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use the Gmail SMTP server
    session.starttls()  # enable security
    session.login(sender_email, sender_account_app_password)  # login with your Gmail account
    text = message.as_string()
    session.sendmail(sender_email, receiver_emails, text)
    session.quit()

@app.route('/', methods=['POST'])
def send_email_api():
    data = request.json
    sender_email = data.get('sender_email')
    sender_account_app_password = data.get('sender_account_app_password')
    receiver_emails = data.get('receiver_emails', [])  # expecting a list of receiver emails
    subject = data.get('subject')
    body = data.get('body')
    files = data.get('files', [])
    api_password = data.get('api_password')

    if(api_password != app.config['API_PASSWORD']):
        return jsonify({'error': 'wrong api_password'}), 500
    
    try:
        send_email(sender_email, sender_account_app_password, receiver_emails, subject, body, files)
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
