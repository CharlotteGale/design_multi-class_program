from lib.diary_entry import *
from tests.helpers import *
import pytest



# __init__()
def test_empty_list_created_on_init():
    """
    On instantiation
    Take parameters and store them correctly
    """
    title1 = generate_contents(5)
    contents1 = generate_contents(100)

    title2 = generate_contents(3)
    contents2 = generate_contents(10)
    phone2 = generate_uk_mobile()

    diary_entry = DiaryEntry(title1, contents1)

    assert diary_entry.title == title1
    assert diary_entry.contents == contents1
    assert diary_entry.phone_number == None

    diary_entry = DiaryEntry(title2, contents2, phone2)
    assert diary_entry.title == title2
    assert diary_entry.contents == contents2
    assert diary_entry.phone_number == phone2



# diary_entry.reading_time()
def test_int_returned_when_wpm_passed_to_read_contents():
    """
    When a WPM is passed in
    Return an integer of how long it will take to read the contents of DiaryEntry
    """
    diary_entry = DiaryEntry("title", generate_contents(1000))

    assert diary_entry.reading_time(100) == 10


# diary_entry.reading_time()
def test_raises_type_error_if_not_int_passed():
    """
    To ensure only integers can be passed in
    Raise TypeError when wpm != int
    """
    diary_entry = DiaryEntry(generate_contents(3), generate_contents(100))

    with pytest.raises(TypeError) as e:
        diary_entry.reading_time("100")
    error_message = str(e.value)
    assert error_message == "Enter an integer"


# diary_entry.reading_time()
def test_raises_value_error_if_negative_int_passed():
    """
    To ensure only positive integers can be passed in
    Raise ValueError if wmp are negative
    """
    diary_entry = DiaryEntry(generate_contents(3), generate_contents(100))

    with pytest.raises(ValueError) as e:
        diary_entry.reading_time(-100)
    error_message = str(e.value)
    assert error_message == "Enter a positive value"

