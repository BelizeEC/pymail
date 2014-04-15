import imaplib

# Had an error. setting this variable on my own fixes it
imaplib._MAXLINE = 1000000

print("Please login:")
username = input("Email:     ")
password = input("Password:  ")

server = imaplib.IMAP4_SSL("imap.gmail.com")
server.login(username, password)
server.list()
server.select("inbox")

result, data = server.search(None, "ALL")
ids = data[0]
id_list = ids.split()
latest_email_id = id_list[-1]

result, data = server.fetch(latest_email_id, "(RFC822)")

raw_email = data[0][1]

print(raw_email)
