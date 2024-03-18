import smtplib
import email.message


def send(sender, to, subject="None", body="None", server="localhost"):
    """메시지를 전송한다."""
    message = email.message.Message()
    message["To"] = to
    message["From"] = sender
    message["Subject"] = subject
    message.set_payload(body)

    client = smtplib.SMTP(server)
    try:
        return client.sendmail(sender, to, message.as_string())
    finally:
        client.quit()
