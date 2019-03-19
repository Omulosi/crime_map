import datetime
import dateparser
import string


CATEGORIES = ['mugging', 'break-in', 'car-jacking', 'murder', 'bank-heist']

def format_date(userdate):
    date = dateparser.parse(userdate)
    try:
        return datetime.datetime.strftime(date, '%Y-%m-%d')
    except TypeError:
        return None

def sanitize_string(userinput):
    whitelist = string.ascii_letters + string.digits + " !?$.,;:-'()&"
    sanitized_input = filter(lambda x: x in whitelist, userinput)
    # covert to string
    return ''.join(sanitized_input)
