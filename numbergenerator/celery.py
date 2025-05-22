import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'numbergenerator.settings')

app = Celery('numbergenerator')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
