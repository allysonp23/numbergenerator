import random


def generate_phone():
    """
    Generate a fictitious Brazilian phone number in the format: "DD 9 NNNN NNNN".
    The first two digits (DD) are a random DDD, the third digit is always '9', and the remaining are random.
    """
    # Random DDD between 11 and 99
    ddd = random.randint(11, 99)
    # Always start with '9'
    third = 9
    # Generate two groups of 4 digits each
    part1 = random.randint(0, 9999)
    part2 = random.randint(0, 9999)
    # Format with leading zeros as needed
    return f"{ddd} {third} {part1:04d} {part2:04d}"
