import random
from .models import GivenName, Surname

def generate_name(gender=None):
    """
    Generate a fictitious Portuguese full name: first name (male or female) + two distinct surnames.

    :param gender: 'male' or 'female' (optional, random if not specified)
    :return: string with full name
    """
    gender = (gender or '').lower()
    if gender not in ('male', 'female'):
        gender = random.choice(['male', 'female'])
    # Map to model gender values
    gender_code = 'M' if gender == 'male' else 'F'
    # Fetch a random first name from the DB
    first_qs = GivenName.objects.filter(gender=gender_code).values_list('name', flat=True)
    first = random.choice(list(first_qs)) if first_qs else ''
    # Fetch two random surnames from the DB
    surname_qs = Surname.objects.all().values_list('name', flat=True)
    surnames = random.sample(list(surname_qs), 2) if surname_qs else ['', '']
    return f"{first} {surnames[0]} {surnames[1]}"
