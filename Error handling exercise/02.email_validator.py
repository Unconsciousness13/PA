class EmailValidationError(Exception):
    pass


class NameNotFound(EmailValidationError):
    pass


class MustContainAtSymbol(EmailValidationError):
    pass


class TooManySymbols(EmailValidationError):
    pass


class NameTooShortError(EmailValidationError):
    pass


class InvalidDomainError(EmailValidationError):
    pass


ALLOWED_DOMAINS = ['.com', '.bg', '.net', '.org', '.gov']

while True:
    email = input()
    if email == 'End':
        break
    if "@" not in email:
        raise MustContainAtSymbol('Email must contain @')

    username, domain, *rest = email.split('@')

    if len(rest) > 0:
        raise TooManySymbols('the whole email must contain one only one "@" symbol')

    if len(username) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')
    if '.' + domain.split(".")[-1] not in ALLOWED_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following {'.com', '.bg', '.net', '.org', '.gov'}")

    print("Email is valid")
