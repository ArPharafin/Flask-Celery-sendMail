# send_email.py
# importing modules
from builtins import set
from datetime import timedelta

import yagmail
from celery import Celery

MAIL_ID = 'sender mail'
MAIL_PASSWORD = 'sender password'

yag = yagmail.SMTP(MAIL_ID, MAIL_PASSWORD)

app = Celery('send_email', broker='amqp://guest:guest@localhost:5672//',
             CELERY_IMPORTS=("send_email", "app"))

app.conf.beat_schedule = {
    'send-email-task': {
        'task': 'send_email.send_without_attachment',
        'schedule': timedelta(seconds=30),  # 5 dakika sonra çalıştır
        'args': (['omerylmaz346@gmail.com'], 'Subject', 'Text'),
    },
}


@app.task
def send_with_attachment(to, subject, content, attachment):
    yag.send(
        to=to,
        subject=subject,
        contents=content,
        attachments=attachment,
    )


@app.task
def send_without_attachment(to, subject, content):
    yag.send(
        to=to,
        subject=subject,
        contents=content
    )
