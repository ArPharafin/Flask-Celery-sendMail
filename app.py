# app.py
# importing libraries
from flask import Flask
import send_email

app = Flask(__name__)


@app.route("/")
def index():
    recipients = ['receivermail1', 'receivermail2']
    subject = 'Subject'
    content = 'Bu mail 30 saniye sonra geldi'
    send_email.send_without_attachment.delay(recipients, subject, content)
    return 'Sent'


if __name__ == '__main__':
    app.run(debug=True)
