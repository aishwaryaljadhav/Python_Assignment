def is_valid_email(s):
    if s.count('@') != 1:
        return False

    username, rest = s.split('@')

    if rest.count('.') != 1:
        return False

    website, extension = rest.split('.')


    for ch in username:
        if not (ch.isalnum() or ch in ['-', '_']):
            return False

    if not website.isalnum():
        return False

    if not extension.isalpha() or len(extension) > 3:
        return False

    return True


def filter_mail(emails):
    return sorted(list(filter(is_valid_email, emails)))
