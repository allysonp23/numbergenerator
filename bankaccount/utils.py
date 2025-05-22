import random

def generate_bankaccount():
    """
    Generate a fictional bank account number in format CCC AAA-A NNNNNNN-N.
    """
    # CCC: 3-digit branch code
    ccc = ''.join(str(random.randint(0, 9)) for _ in range(3))
    # AAA-A: 3 digits + dash + 1 digit
    aaa = ''.join(str(random.randint(0, 9)) for _ in range(3))
    a_digit = str(random.randint(0, 9))
    # NNNNNNN-N: 7 digits + dash + 1 digit
    n_seq = ''.join(str(random.randint(0, 9)) for _ in range(7))
    n_digit = str(random.randint(0, 9))
    return f"{ccc} {aaa}-{a_digit} {n_seq}-{n_digit}"
