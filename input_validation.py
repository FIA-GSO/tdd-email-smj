import re   #regular Expressions


def is_valid_email(email: str) -> bool:
    """
    Uses regular expression to validate email.

    Returns:
    True -- email is valid 
    False -- email is not valid
    """

    username_pattern = r'^[\w\.-]'
    domain_patttern  =  r'[\w\.-]'
    country_patttern  = r'w+$'

    pattern = fr'{username_pattern}+@{domain_pattern}+\.\{country_patttern}'

    if re.match(pattern, email):
        return True
    else:
        return False


