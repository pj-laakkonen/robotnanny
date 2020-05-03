import yagmail


def send_email():
    yag = yagmail.SMTP({"sender@gmail.com": "Sender name"}, 'password')

    contents = [
        "Okay Albert, it's time to go sleep now :)",
        "---------------------------------------------------------------",
        "Mobile data and wifi will be blocked after 15 minutes at 23.",
        "Blocks will be removed in the morning at 7.",
        "---------------------------------------------------------------",
        "Good night",
    ]
    yag.send('recipient@gmail.com', 'Bedtime', contents)
