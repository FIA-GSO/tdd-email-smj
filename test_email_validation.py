import pytest
from input_validation import *


class Tests():
    def test_is_valid_mail_1(self):
        #TODO: arrange
        mail = "jordan.zeng@azerbaijan.az"
        expected = True

        #TODO: act
        result = is_valid_email(mail)

        #TODO: assert
        print("\n\n" + str(result))
        assert result == expected

    def test_is_valid_mail_2(self):
        #TODO: arrange
        mail = "jordan.zeng*#/\//||@azerbaijan.az"
        expected = False

        #TODO: act
        result = is_valid_email(mail)

        #TODO: assert
        print("\n\n" + str(result))
        assert result == expected

@pytest.mark.parametrize("email", [
    ("email@example.com")
    ("firstname.lastname@example.com")
    ("email@subdomain.example.com")
    ("firstname+lastname@example.com")
    ("email@123.123.123.123")
    ("email@[123.123.123.123]")
    ('"email"@example.com')
    ("1234567890@example.com")
    ("email@example-one.com")
        ("_______@example.com")
        ("email@example.name")
        ("email@example.museum")
        ("email@example.co.jp")
        ("firstname-lastname@example.com")
])
def test_is_valid_email__gueltige_Adressen(email):
    assert is_valid_email(email) == True


@pytest.mark.parametrize("email", [
    ("plainaddress")
    ("#@%^%#$@#$@#.com")
    ("@example.com")
    ("Joe Smith <email@example.com>")
    ("email.example.com")
    ("email@example@example.com")
    (".email@example.com")
    ("email.@example.com")
    ("email..email@example.com")
    ("あいうえお@example.com")
    ("email@example.com(Joe Smith)")
    ("email@example")
    ("email@-example.com")
    ("email@example.web")
    ("email@111.222.333.44444")
    ("email@example..com")
    ("Abc..123@example.com")
])
def test_is_valid_email__ungueltige_Adressen(email):
    assert is_valid_email(email) == False
