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