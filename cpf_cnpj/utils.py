import random


def calculate_cpf_check_digits(digits):
    """
    Calculate the two CPF check digits for a list of 9 digits.
    """
    def calc(digs, weights):
        s = sum(d * w for d, w in zip(digs, weights))
        r = s % 11
        return 0 if r < 2 else 11 - r

    d1 = calc(digits, range(10, 1, -1))
    d2 = calc(digits + [d1], range(11, 1, -1))
    return d1, d2


def generate_cpf(mask=True):
    """
    Generate a valid CPF. If mask is True, returns formatted string XXX.XXX.XXX-XX.
    """
    base = [random.randint(0, 9) for _ in range(9)]
    d1, d2 = calculate_cpf_check_digits(base)
    nums = base + [d1, d2]
    if mask:
        return f"{nums[0]}{nums[1]}{nums[2]}.{nums[3]}{nums[4]}{nums[5]}.{nums[6]}{nums[7]}{nums[8]}-{nums[9]}{nums[10]}"
    return "".join(map(str, nums))


def calculate_cnpj_check_digits(digits):
    """
    Calculate the two CNPJ check digits for a list of 12 digits.
    """
    def calc(digs, weights):
        s = sum(d * w for d, w in zip(digs, weights))
        r = s % 11
        return 0 if r < 2 else 11 - r

    weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    weights2 = [6] + weights1
    d1 = calc(digits, weights1)
    d2 = calc(digits + [d1], weights2)
    return d1, d2


def generate_cnpj(mask=True):
    """
    Generate a valid CNPJ. If mask is True, returns formatted string XX.XXX.XXX/XXXX-XX.
    """
    base = [random.randint(0, 9) for _ in range(12)]
    d1, d2 = calculate_cnpj_check_digits(base)
    nums = base + [d1, d2]
    if mask:
        return f"{nums[0]}{nums[1]}.{nums[2]}{nums[3]}{nums[4]}.{nums[5]}{nums[6]}{nums[7]}/{nums[8]}{nums[9]}{nums[10]}{nums[11]}-{nums[12]}{nums[13]}"
    return "".join(map(str, nums))


def get_cpf(mask_param=None):
    """
    Return a generated CPF, parsing mask_param ('true'/'false') into boolean.
    """
    mask = True if mask_param is None else str(mask_param).lower() == 'true'
    return generate_cpf(mask=mask)


def get_cnpj(mask_param=None):
    """
    Return a generated CNPJ, parsing mask_param ('true'/'false') into boolean.
    """
    mask = True if mask_param is None else str(mask_param).lower() == 'true'
    return generate_cnpj(mask=mask)
