# Design and Test Drive a Multi-Class Program

## User Stories
### User Story 1
>As a user      
>So that I can record my experiences
>I want to keep a regular diary

### User Story 2
>As a user      
>So that I can reflect on my experiences        
>I want to read my past diary entries

### User Story 3
>As a user      
>So that I can reflect on my experiences in my busy day     
>I want to select diary entries to read based on how much time I have and my reading speed

### User Story 4
>As a user      
>So that I can keep track of my tasks       
>I want to keep a todo list along with my diary

### User Story 5
>As a user      
>So that I can keep track of my contacts        
>I want to see a list of all of the mobile phone numbers in all my diary entries

## Notes on Behaviour/Interaction
- `ToDo()` is a separate, unrelated class
- `Diary()` relies on `DiaryEntry()`
- **Unit tests** can be carried out on *all* `DiaryEntry()` and `ToDo()` methods.
- `Diary()` requires **integration tests** 

## Class Hierarchy 
![Architecture Diagram](images/architecture_diagram.png)

## Class Interfaces
```python
class ToDo:
    def __init__(self):
        # Parameters:
        #   None
        # Returns:
        #   Nothing
        # Side Effects:
        #   None
        # Internal State:
        #   self.task_list = [] : empty list to store tasks
        pass

    def add_task(self, task):
        # Parameters:
        #   task: string
        # Returns:
        #   Nothing
        # Side Effects:
        #   adds task to self.task_list
        # Internal State:
        #   N/A
        pass
```

```python
class Diary:
    def __init__(self):
        # Parameters:
        #   None
        # Returns:
        #   Nothing
        # Side Effects:
        #   None
        # Internal State:
        #   self.diary_entries = [] : empty list to store instances of DiaryEntry
        pass

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side Effects:
        #   Adds an instance of DiaryEntry to self.diary_entries
        pass

    def read_all(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of DiaryEntry instances
        pass

    def read_an_entry(self, wpm, minutes):
        # Parameters:
        #   wpm: int representing words per minute user can read
        #   minutes: int representing how long user has to read
        # Returns:
        #   An instance of DiaryEntry that is closest too and does not exceed  minutes given
        pass
    
    def contacts_list(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of contacts
        pass
```

```python
class DiaryEntry:
    def __init__(self, title, contents, phone_number=None):
        # Parameters:
        #   title: string
        #   contents: string
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: int representing reading words per minutes
        # Returns:
        #   An integer representing how long it will take to read the contents of DiaryEntry
        pass
```

## Plan for Testing
### Unit Tests
1. `ToDo.__init__()`
2. `ToDo.add_task()`
3. `Diary.__init__()`
4. `DiaryEntry.__init__()`
5. `DiaryEntry.reading_time()`

### Integration Tests
1. `Diary.add()`
2. `Diary.read_all()`
3. `Diary.read_an_entry()`
4. `Diary.contacts_list()`

### Validation Tests
`ToDo.add_task()`
- TypeError to ensure only strings can be passed in
- ValueError to ensure no empty strings get passed in

`Diary.add()`
- TypeError to ensure only an instance of DiaryEntry can be passed in

`Diary.read_an_entry()`
- TypeError to ensure only `int` can be passed in
- ValueError to ensure only positive integers can be passed in

`DiaryEntry.__init__()`
- TypeError to ensure only strings can be passed in (for title and contents)
- ValueError to ensure no empty strings get passed in (for title and contents)
- TypeError to ensure phone_number is either None or a string
- ValueError to ensure phone_number matches valid UK mobile format (if provided)

`DiaryEntry.reading_time()`
- TypeError to ensure only `int` can be passed in
- ValueError to ensure only positive integers can be passed in

## Test Cases
### `ToDo()`
```python
# __init__()
"""
On instantiation
Ensure self.task_list is created as an empty list
"""
todo = ToDo()

assert todo.task_list == []
```

```python
# todo.add()
"""
When adding a task
Ensure task is added to self.task_list
"""
todo = ToDo()

todo.add_task("Here's a task")
assert  todo.task_list == ["Here's a task"]

todo.add_task("Here's another task")
assert todo.task_list == ["Here's a task", "Here's another task"]
```

```python
# todo.add()
"""
When an int etc is passed into todo.add()
Return a TypeError
"""
todo = ToDo()
with pytest.raises(TypeError) as e:
    todo.add(123)
error_message = str(e.value)
assert error_message == "Enter a valid task string"
```

```python
# todo.add()
"""
Ensure empty strings cannot be passed in
Return a ValueError
"""
todo = ToDo()
with pytest.raises(ValueError) as e:
    todo.add("")
error_message = str(e.value)
assert error_message == "Enter a task"
```

### `Diary()`
```python
# __init__()
"""
On instantiation
Ensure self.diary_entries is created as an empty list
"""
diary = Diary()

assert diary.diary_entries == []
```

```python
# diary.add()
"""
When given an instance of DiaryEntry
Ensure DiaryEntry is added to self.diary_entries
"""
diary = Diary()
diary_entry = DiaryEntry("title", "contents of 100 words")

diary.add(diary_entry)

assert diary_entry in diary.diary_entries
```

```python
# diary.read_all()
"""
When called
Return a list of DiaryEntry instances
"""
diary = Diary()
diary_entry1 = DiaryEntry("title1", "contents of 250 words")
diary_entry2 = DiaryEntry("title2", "contents of 500 words")

diary.add(diary_entry1)
diary.add(diary_entry2)

assert diary.read_all() == [diary_entry1, diary_entry2]
```

```python
# diary.read_an_entry()
"""
When given a reading WPM and minutes to read
Return an instance of DiaryEntry that is closest too and does not exceed minutes given
"""
diary = Diary()
diary_entry1 = DiaryEntry("title1", "contents of 498 words")
diary_entry2 = DiaryEntry("title2", "contents of 502 words")

diary.add(diary_entry1)
diary.add(diary_entry2)

assert diary.read_an_entry(100, 5) == diary_entry1
assert diary.read_an_entry(100, 2) == None
```

```python
# diary.contacts_list()
"""
When called
Return a list of contacts from instances of DiaryEntry
"""
diary = Diary()
diary_entry1 = DiaryEntry("title1", "short sentence", "07123456789")
diary_entry2 = DiaryEntry("title2", "contents of 100 words")
diary_entry3 = DiaryEntry("title3", "short sentence", "07223456789")

diary.add(diary_entry1)
diary.add(diary_entry2)
diary.add(diary_entry3)

assert diary.contacts_list() == ["07123456789", "07223456789"]
```

```python
# diary.add()
"""
To ensure only instances of DiaryEntry can be passed in
Return TypeError when entry != DiaryEntry
"""
diary = Diary()

with pytest.raises(TypeError) as e:
    diary.add(123)
error_message = str(e.value)
assert error_message == "Enter an instance of DiaryEntry"
```

```python
# diary.read_an_entry()
"""
To ensure only integers can be passed in
Raise TypeError when wpm or minutes != int
"""
diary = Diary()

with pytest.raises(TypeError) as e:
    diary.read_an_entry("100", 30)
error_message = str(e.value)
assert error_message == "Enter an integer"
```

```python
# diary.read_an_entry()
"""
To ensure only positive integers can be passed in
Raise ValueError if wmp or minutes are negative
"""
diary = Diary()

with pytest.raises(ValueError) as e:
    diary.read_an_entry(-400, 30)
error_message = str(e.value)
assert error_message == "Enter positive values only"
```

### `DiaryEntry()`
```python
# __init__()
"""
On instantiation
Take parameters and store them correctly
"""
diary_entry = DiaryEntry("title", "contents of 100 words")

assert diary_entry.title == "title"
assert diary_entry.contents == "contents of 100 words"
assert diary_entry.phone_number == None

diary_entry = DiaryEntry("Monday", "Phone Bill", "07711222333")
assert diary_entry.title == "Monday"
assert diary_entry.contents == "Phone Bill"
assert diary_entry.phone_number == "07711222333"
```

```python
# diary_entry.reading_time()
"""
When a WPM is passed in
Return an integer of how long it will take to read the contents of DiaryEntry
"""
diary_entry = DiaryEntry("title", "contents of 1000 words")

assert diary_entry.reading_time(100) == 10
```

```python
# diary_entry.reading_time()
"""
To ensure only integers can be passed in
Raise TypeError when wpm != int
"""
diary_entry = DiaryEntry()

with pytest.raises(TypeError) as e:
    diary_entry.reading_time("100")
error_message = str(e.value)
assert error_message == "Enter an integer"
```

```python
# diary_entry.reading_time()
"""
To ensure only positive integers can be passed in
Raise ValueError if wmp are negative
"""
diary_entry = DiaryEntry()

with pytest.raises(TypeError) as e:
    diary_entry.reading_time(-100)
error_message = str(e.value)
assert error_message == "Enter a positive value"
```