
<h2>Python Email API</h1>

This is a simple Python Flask API for sending emails conveniently using a POST request. It's built to make sending emails programmatically easy and hassle-free.

<h3>How to Use</h3>

<h4>Endpoint</h4>

POST <a href="https://python-email-api.vercel.app" target="_blank">https://python-email-api.vercel.app</a>

<h4>Request Body</h4>

The API expects a JSON object with the following fields:
<ul>
  <li><b>sender_email:</b> Your email address.</li>

  <li><b>sender_password:</b> Your email account password. Note: Please use this feature with caution and consider using a dedicated email account with limited privileges for security reasons.</li>

  <li><b>receiver_email:</b> Email address of the recipient.</li>

  <li><b>subject:</b> Subject of the email.</li>

  <li><b>body:</b> Body content of the email.</li>

  <li><b>files (optional):</b> List of file names to attach with the email. Ensure the files are present and accessible to the API.</li>
</ul>

Here's an example request body:

    {

      "sender_email": "your_email@gmail.com",
  
      "sender_password": "your_email_password",
  
      "receiver_email": "recipient@example.com",
  
      "subject": "Test Email",
  
      "body": "This is a test email sent from Python.",
  
      "files": ["file1.txt", "file2.pdf"]
  
    }
