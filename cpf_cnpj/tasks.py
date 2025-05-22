from celery import shared_task

from .utils import get_cpf, get_cnpj


@shared_task
def generate_cpf_task(mask_param=None):
    """
    Celery task to generate CPF synchronously.
    """
    return get_cpf(mask_param)


@shared_task
def generate_cnpj_task(mask_param=None):
    """
    Celery task to generate CNPJ synchronously.
    """
    return get_cnpj(mask_param)
