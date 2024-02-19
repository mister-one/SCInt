import re

def main(merchant_name):
    # Remove non-alphanumeric characters and extra spaces
    cleaned_name = re.sub(r'[^a-zA-Z0-9\s]+', '', merchant_name)
    cleaned_name = re.sub(r'\s+', ' ', cleaned_name).strip().lower()
    return cleaned_name