import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = "Konstantin Orlov"
email['to'] = "example@ya.ru"
email['subject'] = "You won a tonn of money"

email.set_content(html.substitute({'name' : 'Alexey'}), 'html')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('example@gmail.com', 'password')
    smtp.send_message(email)
    print('done')

# ======================
# email = EmailMessage()
# email['from'] = "Konstantin Orlov"
# email['to'] = "example@ya.ru"
# email['subject'] = "You won a tonn of money"
#
# email.set_content('Message of the letter')
#
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('example@gmail.com', 'password')
#     smtp.send_message(email)
#     print('done')