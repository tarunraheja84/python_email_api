
<h2>Tarun's Python Email API</h1>

This is a simple Python Flask API for sending emails conveniently using a POST request. It's built to make sending emails programmatically easy and hassle-free.

<h3>How to Use</h3>

<h4>Endpoint</h4>

POST <a href="https://python-email-api.vercel.app" target="_blank" rel="noopener noreferrer">`https://python-email-api.vercel.app/`</a>

<h4>Request Body</h4>

The API expects a JSON object with the following fields:
<ul>
  <li><b>sender_email:</b> Your email address.</li>

  <li><b>sender_account_app_password:</b> Your email account "app password". Note: Please turn on 2-factor authentication and then visit here <a href="https://myaccount.google.com/apppasswords" target="_blank" rel="noopener noreferrer">`https://myaccount.google.com/apppasswords`</a> to create an app password for your account.</li>

  <li><b>receiver_emails:</b> Array of Email address of recipients.</li>

  <li><b>subject:</b> Subject of the email.</li>

  <li><b>body:</b> Body content of the email.</li>

  <li><b>files (optional):</b> Array of path of files to attach with the email. Please specify correct paths, files will be sent with their filenames and not file path.</li>
</ul>

Here's an example request body:

    {

      sender_email: "your_email@gmail.com",
  
      sender_account_app_password: "your_sender_account_app_password",
  
      receiver_emails: ["recipient@example.com", "recipient2@example.com"],
  
      subject: "Test Email",
  
      body: "This is a test email sent from Python Flask API.",
  
      files: ["/Users/mac/desktop/file1.txt", "file2.pdf"]
  
    }
