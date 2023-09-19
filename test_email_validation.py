import pytest
from input_validation import *


def test_is_valid_mail_1():
    #TODO: arrange
    mail = "jordan.zeng@azerbaijan.az"
    expected = True

    #TODO: act
    result = is_valid_email(mail)

    #TODO: assert
    print("\n\n" + str(result))
    assert result == expected


def test_is_valid_mail_2():
    #TODO: arrange
    mail = "jordan.zeng*#/\//||@azerbaijan.az"
    expected = False

    #TODO: act
    result = is_valid_email(mail)

    #TODO: assert
    print("\n\n" + str(result))
    assert result == expected
