import yagmail


def send_email():
    yag = yagmail.SMTP({"sender@gmail.com": "Sender name"}, 'password')

    contents = [
        "Okay Albert, it's time to go sleep now :)",
        #" ",
    ]
    yag.send('recipient@gmail.com', 'Bedtime', contents)
