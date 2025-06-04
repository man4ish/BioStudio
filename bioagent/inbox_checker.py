import imaplib
import email
from email.header import decode_header
import os
from responder import send_ai_response

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")

def check_inbox():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")

    status, messages = mail.search(None, '(UNSEEN SUBJECT "Re: BioStudio: File Uploaded")')
    email_ids = messages[0].split()

    for eid in email_ids:
        status, msg_data = mail.fetch(eid, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                sender = email.utils.parseaddr(msg['From'])[1]
                subject = msg['Subject']

                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            send_ai_response(sender, body)
                else:
                    body = msg.get_payload(decode=True).decode()
                    send_ai_response(sender, body)

    mail.logout()

if __name__ == "__main__":
    check_inbox()