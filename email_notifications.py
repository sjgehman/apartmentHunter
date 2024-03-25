import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Change sender address, password, and receiver address below. 
#For gmail, you need a 16 digit app password rather than your standard password. Go to myaccount.google.com/apppasswords
def send_email(units):
    # Email setup
    sender_address = ''
    sender_pass = ''
    receiver_address = ''
    
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Apartments Available!'
    
    # The body and the attachments for the mail
    mail_content = "Hello,\nHere are the apartment details:\n\n"
    for unit in units:
        mail_content += f"Unit: {unit['name']}, Price: ${unit['price']}, Bedrooms: {unit['bedrooms']}, Link: {unit['link']}\n"
    message.attach(MIMEText(mail_content, 'plain'))
    
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')