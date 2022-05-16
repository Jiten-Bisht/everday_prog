import smtplib
import imaplib
import email
Your_Email = "example@gmail.com"
Your_Pass = "your-password" 
Server = "imap.gmail.com" 
Port = 993
mail = imaplib.IMAP4_SSL(Server)
mail.login(Your_Email,Your_Pass)
mail.select('inbox')
data = mail.search(None, 'ALL')
mail_ids = data[1]
ids = mail_ids[0].split()   
first_id = int(ids[0])
last_id = int(ids[-1])
for i in range(last_id,first_id, -1):
    data = mail.fetch(str(i), '(RFC822)' )
    for response in data:
        array = response[0]
        if isinstance(array, tuple):
            msg = email.message_from_string(str(array[1],'utf-8'))
            subject = msg['subject']
            mail_from = msg['from']
            print('From : ' + mail_from + '\n')
            print('Subject : ' + subject + '\n')
