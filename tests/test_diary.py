from lib.diary import *
from lib.diary_entry import *
from tests.helpers import *
import pytest


# __init__()
def test_empty_list_created_on_init():
    """
    On instantiation
    Ensure self.diary_entries is created as an empty list
    """
    diary = Diary()

    assert diary.diary_entries == []

# @pytest.mark.skip(reason="waiting on DiaryEntry")
# diary.add()
def test_add_diary_entry_to_diary_entries():
    """
    When given an instance of DiaryEntry
    Ensure DiaryEntry is added to self.diary_entries
    """
    diary = Diary()
    diary_entry = DiaryEntry("title", generate_contents(100))

    diary.add(diary_entry)

    assert diary_entry in diary.diary_entries


# diary.read_all()
def test_return_list_of_all_instances_of_DiaryEntry():
    """
    When called
    Return a list of DiaryEntry instances
    """
    diary = Diary()
    diary_entry1 = DiaryEntry("title1", generate_contents(250))
    diary_entry2 = DiaryEntry("title2", generate_contents(500))

    diary.add(diary_entry1)
    diary.add(diary_entry2)

    assert diary.read_all() == [diary_entry1, diary_entry2]

# @pytest.mark.skip(reason="waiting on dairy_entry.reading_time")
# # diary.read_an_entry()
def test_return_an_instance_of_DiaryEntry_to_read():
    """
    When given a reading WPM and minutes to read
    Return an instance of DiaryEntry that is closest too and does not exceed minutes given
    """
    diary = Diary()
    diary_entry1 = DiaryEntry("title1", generate_contents(498))
    diary_entry2 = DiaryEntry("title2", generate_contents(502))

    diary.add(diary_entry1)
    diary.add(diary_entry2)

    assert diary.read_an_entry(100, 5) == diary_entry1
    assert diary.read_an_entry(100, 2) == None


# diary.contacts_list()

"""
When called
Return a list of contacts from instances of DiaryEntry
"""
diary = Diary()
phone1 = generate_uk_mobile()
phone2 = generate_uk_mobile()
diary_entry1 = DiaryEntry("title1", generate_contents(10), phone1)
diary_entry2 = DiaryEntry("title2", generate_contents(100))
diary_entry3 = DiaryEntry("title3", generate_contents(4), phone2)

diary.add(diary_entry1)
diary.add(diary_entry2)
diary.add(diary_entry3)

assert diary.contacts_list() == [phone1, phone2]


# diary.add()
def test_raises_type_error_if_not_instance_of_DiaryEntry():
    """
    To ensure only instances of DiaryEntry can be passed in
    Return TypeError when entry != DiaryEntry
    """
    diary = Diary()

    with pytest.raises(TypeError) as e:
        diary.add(123)
    error_message = str(e.value)
    assert error_message == "Enter an instance of DiaryEntry"


# diary.read_an_entry()
def test_raises_type_error_if_input_not_integer():
    """
    To ensure only integers can be passed in
    Raise TypeError when wpm or minutes != int
    """
    diary = Diary()

    with pytest.raises(TypeError) as e:
        diary.read_an_entry("100", 30)
    error_message = str(e.value)
    assert error_message == "Enter an integer"


# diary.read_an_entry()
def test_raise_value_error_if_input_negative():
    """
    To ensure only positive integers can be passed in
    Raise ValueError if wmp or minutes are negative
    """
    diary = Diary()

    with pytest.raises(ValueError) as e:
        diary.read_an_entry(-400, 30)
    error_message = str(e.value)
    assert error_message == "Enter positive values only"

