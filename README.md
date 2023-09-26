yagmail — for sending email

celery — for queueing the tasks

pip install eventlet

Before start sending email asynchronously, you have to start the celery worker.

To start celery on cmd/terminal on the project directory where the
‘send_email.py’ file is located and activate the virtual environment if any.


(celery -A send_mail worker -l=info -P eventlet 

or

celery -A send_email worker -l info -P threads)

.

celery -A send_email beat (for scheduled mails)