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
    def __init__(self, title, contents):
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
- TypeError to ensure only strings can be passed in
- ValueError to ensure no empty strings get passed in

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
diary_entry1 = DiaryEntry("title1", "contains 3 contacts information")
diary_entry2 = DiaryEntry("title2", "contains 0 contancts information")
diary_entry3 = DiaryEntry("title3", "contants 1 contacts information")

diary.add(diary_entry1)
diary.add(diary_entry2)
diary.add(diary_entry3)

assert diary.contacts_list() == [["name1", "07123456789"], ["name2", "07223456789"], ["name3", "07323456789"], ["name4", "07423456789"]]
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
