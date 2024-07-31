import re

# Basic regex patterns for sensitive data
regex_patterns = {
    'credit_card': r'\b(?:\d[ -]*?){13,16}\b',  # Basic regex for credit card numbers
    'ssn': r'\b\d{3}-\d{2}-\d{4}\b',            # Basic regex for Social Security Numbers
    'email': r'\b[a-z0-9._%\+\-—|]+@[a-z0-9.\-—|]+\.[a-z|]{2,6}\b',    # Basic regex for Email Need to recheck
    'IPv4': r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',   #Basic regex for IPv4
    'UK_Number': r'\b([0O]?[1lI][1lI])?[4A][4A][\dOIlZEASB]{10,11}\b'   #Basic regex for UK Phone Number Need data to verify
}

def sensitive_data_check(text):
    found_data = {}
    for labels, rgx_pattern in regex_patterns.items():
        matches = re.findall(rgx_pattern, text)
        if matches:
            found_data[labels] = matches
    return found_data