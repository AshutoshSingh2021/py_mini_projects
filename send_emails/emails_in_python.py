import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

email_id = os.environ.get("EMAIL")
email_password = os.environ.get("PASSWORD")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp: # 587 is the port number
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_id, email_password)

    subject = "Exploring Opportunities at..."
    body = "Hey, please consider my resume for any software developer role if I meet the requirements."
    message = f"Subject: {subject} \n\n\n{body}"

    smtp.sendmail(email_id, "email@gmail.com", message)