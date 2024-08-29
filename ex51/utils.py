import re
import os
from datetime import datetime
from collections import OrderedDict

DATE_FORMATS = {"reporting_period": "%B %Y", "report_date": "%d%b%Y"}


def is_pdf(path_string):
    return os.path.exists(path_string) and path_string.lower().endswith(".pdf")


def parse_to_iso_date(date_string, date_format=DATE_FORMATS["reporting_period"]):
    """Take a date string and return the  ISO 8601 format e.g. 'YYYY-MM-DD'"""
    if date_format in DATE_FORMATS.values():
        date_object = datetime.strptime(date_string.strip(), date_format)
        return date_object.date().isoformat()
    else:
        raise KeyError("Not a valid date format.")


def to_snake_case(str1):
    str1 = str1.lower()
    str1 = re.sub(r"[\s\-]+", "_", str1)
    str1 = re.sub(r"[^\w_]", "", str1)
    return str1


def to_capitalized(str1):
    """Turn a snake case string into a capitalized one."""
    words = str1.split("_")
    capitalized_words = [word.capitalize() for word in words]
    capitalized_string = " ".join(capitalized_words)

    return capitalized_string


def generate_data_dict(*args):
    """Consolidate a variable amount of dictionaries into one OrderedDict."""
    data = OrderedDict()

    for arg in args:
        try:
            if isinstance(arg, dict):
                data.update(arg)
            else:
                raise TypeError("Argument must be a dictionary.")
        except TypeError as e:
            print(e)

    return data
