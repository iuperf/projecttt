import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from боты.config import email_pass, email_log


def send_message(to_email, text):
    msg = MIMEMultipart()
    to_email = to_email
    message = text
    msg.attach((MIMEText(message, 'plain')))
    if to_email.endswith('gmail.com'):
        server = smtplib.SMTP('smtp.gmail.com: 587')
    elif to_email.endswith('mail.ru'):
        server = smtplib.SMTP(f'smtp.mail.ru: 25')
    elif to_email.endswith('yandex.com'):
        server = smtplib.SMTP(f'smtp.yandex.com: 465')

    else:
        return 'Неправильный ввод'
    server.starttls()
    server.login(email_log, email_pass)
    server.sendmail(email_log, to_email, msg.as_string())
    server.quit()
    return 'Успех'
