import smtplib

print("Please login to GMail:")
fromAddr = input("Email:     ")
password = input("Password:  ")
print("Who is this to?")
toAddr = input("Email:     ")
msg = input("Message:   ")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromAddr, password)
server.sendmail(fromAddr, toAddr, msg)
server.quit()
