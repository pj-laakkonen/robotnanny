from jobs import set_blocks
from sendemail import send_email


def gotosleep():
    contract = "12345678"  # Elisa's contract number
    bedtime = True
    set_blocks(contract, bedtime)
    send_email()
