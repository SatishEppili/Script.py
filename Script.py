import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_mail(workflow_name, repo_name):
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv('RECEIVER_EMAIL')

    subject = f"Workflow {workflow_name} failed for repo {repo_name}"
    body = f"Hi, the workflow {workflow_name} failed for repo {repo_name}. please checkthe logs for more details.\n More Details: \n Run_ID: {workflow_Run_id}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 582)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, sender_email, text)
        server.quit()

        print('Email Sent Successfully')
    except Exception as e:
        print(f'Error: {e}')

send_mail(os.getenv('WORKFLOW_NAME'), os.getenv('REPO_NAME'), os.env('WORKFLOW_RUN_ID'))
