from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)

def send_email(sender_email, sender_password, receiver_email, subject, body, files=[]):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))

    # Attach files
    for file in files:
        attachment = MIMEBase('application', 'octet-stream')
        with open(file, "rb") as f:
            attachment.set_payload(f.read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', f'attachment; filename= {file}')
        message.attach(attachment)

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use the Gmail SMTP server
    session.starttls()  # enable security
    session.login(sender_email, sender_password)  # login with your Gmail account
    text = message.as_string()
    session.sendmail(sender_email, receiver_email, text)
    session.quit()

@app.route('/', methods=['POST'])
def send_email_api():
    data = request.json
    sender_email = data.get('sender_email')
    sender_password = data.get('sender_password')
    receiver_email = data.get('receiver_email')
    subject = data.get('subject')
    body = data.get('body')
    files = data.get('files', [])

    try:
        send_email(sender_email, sender_password, receiver_email, subject, body, files)
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
