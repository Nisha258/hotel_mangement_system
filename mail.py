import smtplib
# creates SMTP session

s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("nishasenjaliya19@gmail.com", "ycgd ztwg fmjr tvlu")
# message to be sent
message = "hello!! welcpme to Urban Hotel"
# sending the mail
s.sendmail("nishasenjaliya19@gmail.com", "nishaapatel40@gmail.com", message)
# terminating the session
s.quit()
