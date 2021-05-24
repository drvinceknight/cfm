"""
A script to send feedback to students for their submissions

Reads from `gmail.py` which must contain two variables:

gmail_user = vincent.knight
gmail_pwd = XXXXXX
"""
import smtplib
from email.mime.text import MIMEText
import pathlib
import re
import pandas as pd

import gmail

SUBJECT = "DO NOTE REPLY - Coursework mark and feedback"
FEEDBACK_SUFFIX = "-feedback.md"
SUBMISSIONS_PATH = pathlib.Path("./submissions/")
STUDENT_ID_PATTERN = re.compile("submissions/Coursework_(.*)_attempt")


def create_server(gmail_user, gmail_pwd):
    """
    Create an ssl server by logging in to my gmail account.
    """
    # SMTP_SSL Example
    server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server_ssl.login(gmail_user, gmail_pwd)
    return server_ssl


def create_message(sender, recipient, text, subject):
    message = MIMEText(text)
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = recipient
    return message


def send_message(server_ssl, sender, recipient, message):
    """
    Send an email using a given server
    """
    server_ssl.sendmail(from_addr=sender, to_addrs=recipient, msg=message.as_string())
    # server_ssl.quit()
    print(f"successfully sent the mail to {recipient}")


def close_server(server_ssl):
    """
    Close a given server_ssl
    """
    server_ssl.close()


def main():
    try:
        with open("sent.txt", "r") as f:
            sent = f.read()
    except FileNotFoundError:
        sent = ""
    sender = "knightva@cardiff.ac.uk"
    recipient = "knightva@cardiff.ac.uk"
    server_ssl = create_server(gmail_user=gmail.gmail_user, gmail_pwd=gmail.gmail_pwd)

    df = pd.read_csv("./data.csv")
    for _, row in df.iterrows():
        path = row["Submission filepath"]
        score = row["Score"]
        maximum_score = row["Maximum score"]

        feedback = pathlib.Path(path + FEEDBACK_SUFFIX).read_text()
        match = re.match(pattern=STUDENT_ID_PATTERN, string=path)
        student_id = match.group(1)

        if student_id not in sent:

            recipient = f"{student_id}@cardiff.ac.uk"

            text = f"""{student_id}

    Your obtained {score} / {maximum_score} on your coursework.

    Below is the automatically generated feedback for your coursework. If you have
    any questions email "knightva@cardiff.ac.uk" (DO NOT REPLY TO THIS EMAIL).

    {feedback}
    """

            message = create_message(
                sender=sender, recipient=recipient, text=text, subject=SUBJECT
            )

            send_message(
                server_ssl=server_ssl,
                sender=sender,
                recipient=recipient,
                message=message,
            )

    close_server(server_ssl=server_ssl)


if __name__ == "__main__":
    main()
