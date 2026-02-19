from src.assignment15.util import is_valid_email, filter_mail

def test_valid_email():
    assert is_valid_email("abc-def_123@website.com") is True


def test_filter_mail():
    emails = [
        "abc@site.com",
        "invalid@@site.com",
        "user@site.org"
    ]

    assert filter_mail(emails) == ["abc@site.com", "user@site.org"]
