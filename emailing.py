import smtplib
import imghdr
from email.message import EmailMessage
from functions import get_cred

get_cred = get_cred()
PASSWORD = get_cred["PASSWORD_WEBCAM_APP"]
SENDER = get_cred["SENDER_WEBCAM_APP"]
RECEIVER = get_cred["RECEIVER_WEBCAM_APP"]


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up! "
    email_message.set_content("Hey, We saw a new customer !")

    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email(image_path="images/50.png")
