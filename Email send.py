import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, login, password):
    """
    Sends an email with the specified subject and body.

    Parameters:
    subject (str): The subject of the email.
    body (str): The body content of the email.
    to_email (str): The recipient's email address.
    from_email (str): The sender's email address.
    smtp_server (str): The SMTP server address.
    smtp_port (int): The port number for the SMTP server.
    login (str): The login username (usually the sender's email address).
    password (str): The password for the email account.
    """
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body to the email
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(login, password)
            server.send_message(msg)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Email details
    subject = "50000"
    body = "kon hai bhai tuuu"


    to_email = "chavdajay415@gmail.com"    
    
    
    from_email = "chavdakundan59@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    login = "chavdakundan59@gmail.com"
    password = "kprb fssh jsbt lzdx"  

    send_email(subject, body, to_email, from_email, smtp_server, smtp_port, login, password)

if __name__ == "__main__":
    main()
