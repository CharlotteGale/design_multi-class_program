from lib.diary_entry import *

class Diary:
    def __init__(self):
        self.diary_entries = []

    def add(self, entry):
        if not isinstance(entry, DiaryEntry):
            raise TypeError("Enter an instance of DiaryEntry")
        self.diary_entries.append(entry)

    def read_all(self):
        return self.diary_entries
    
    def read_an_entry(self, wpm, minutes):
        if not isinstance(wpm, int) or not isinstance(minutes, int):
            raise TypeError("Enter an integer")
        
        if wpm <= 0 or minutes <= 0:
            raise ValueError("Enter positive values only")

        best_entry = None

        for entry in self.diary_entries:
            if entry.reading_time(wpm) <= minutes:
                if best_entry == None:
                    best_entry = entry
                else:
                    if entry > best_entry:
                        best_entry = entry
        
        return best_entry
    
    def contacts_list(self):
        phone_numbers_from_entries = []

        for entry in self.diary_entries:
            if entry.phone_number:
                phone_numbers_from_entries.append(entry.phone_number)
        
        return phone_numbers_from_entries