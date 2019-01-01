import smtplib

content=" shankar's first mail through interpreter"
mail=smtplib.SMTP("smtp.gmail.com",587)#or use port 465
mail.ehlo()
mail.starttls()
mail.login("email","password")
mail.sendmail("senders id","receivers id",content)
mail.close()

