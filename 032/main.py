from smtplib import SMTP

# from email.mime.text import MIMEText

subject = "Email Subject"
body = "This is the body of the text message"
recipients = ["dev.hamanovich@yahoo.com"]
sender = "dev.hamanovich@yahoo.com"
password = "###"


# def send_email(subject, body, sender, recipients, password):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender
#     msg['To'] = ', '.join(recipients)
#     with SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
#        smtp_server.login(sender, password)
#        smtp_server.sendmail(sender, recipients, msg.as_string())
#     print("Message sent!")


# send_email(subject, body, sender, recipients, password)

with SMTP("smtp.mail.yahoo.com", 587) as connection:
    connection.starttls()
    connection.login(user=sender, password=password)
    connection.sendmail(
        from_addr=sender,
        to_addrs=recipients[0],
        msg="Subject:Hello\n\nThis is the body of my email."
    )
