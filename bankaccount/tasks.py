from celery import shared_task

from .utils import generate_bankaccount


@shared_task
def generate_bankaccount_task():
    """
    Celery task to generate a fictional bank account number.
    """
    return generate_bankaccount()
