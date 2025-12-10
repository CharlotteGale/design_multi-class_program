from lib.todo import *
from tests.helpers import *
import pytest


# __init__()
def test_empty_list_created_on_init():
    """
    On instantiation
    Ensure self.task_list is created as an empty list
    """
    todo = ToDo()

    assert todo.task_list == []


# todo.add_task()
def test_task_added_to_list():
    """
    When adding a task
    Ensure task is added to self.task_list
    """
    todo = ToDo()

    todo.add_task("Here's a task")
    assert  todo.task_list == ["Here's a task"]

    todo.add_task("Here's another task")
    assert todo.task_list == ["Here's a task", "Here's another task"]


# todo.add_task()
def test_return_type_error():
    """
    When an int etc is passed into todo.add()
    Return a TypeError
    """
    todo = ToDo()
    with pytest.raises(TypeError) as e:
        todo.add_task(123)
    error_message = str(e.value)
    assert error_message == "Enter a valid task string"


# todo.add()
def test_return_value_error_on_empty_string():
    """
    Ensure empty strings cannot be passed in
    Return a ValueError
    """
    todo = ToDo()
    with pytest.raises(ValueError) as e:
        todo.add_task("")
    error_message = str(e.value)
    assert error_message == "Enter a task"