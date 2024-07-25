import datetime
from django.utils.crypto import get_random_string



def generate_vendor_code():
    date_str = datetime.datetime.now().strftime('%Y%m%d')
    random_str = get_random_string(length=4, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    prefix = "VND"
    return f"{prefix}-{date_str}-{random_str}"
