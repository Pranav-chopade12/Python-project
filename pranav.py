import re
import dns.resolver

def is_valid_email(email):
    """
    Validates the format of the email using a regular expression.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email) is not None

def check_mx_record(domain):
    """
    Checks if the domain of the email has valid MX (Mail Exchange) records.
    """
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        return len(mx_records) > 0
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        return False

def validate_email(email):
    """
    Validates an email address by format and domain MX record.
    """
    if not is_valid_email(email):
        return "Invalid email format."

    domain = email.split('@')[1]
    if not check_mx_record(domain):
        return "Email domain is not valid (no MX record found)."

    return "Email is valid!"

def main():
    print("Email Validation Program")
    print("------------------------")
    
    while True:
        email = input("Enter an email address to validate (or 'exit' to quit): ").strip()
        if email.lower() == 'exit':
            print("Exiting the program.")
            break
        
        result = validate_email(email)
        print(result)
        print()

if __name__ == "__main__":
    main()
