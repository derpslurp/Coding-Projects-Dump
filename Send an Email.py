import smtplib

sender = 'Isaac.ang12211@gmail.com'
receiver = 'ChingChongBingBong1221@gmail.com'
password = 'Chickenwing1221'
subject = 'Python email test'
body = '*farts*'

message = f"""From: Snoop Dogg{sender}
To: Tom Holland{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

try:
    server.login(sender,password)
    print('Logged in...')
    server.sendmail(sender,receiver,message)
    print('Email has been sent')
except smtplib.SMTPAuthenticationError:
    print('Unable to sign in')