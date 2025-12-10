class DiaryEntry:
    def __init__(self, title, contents, phone_number=None):
        self.title = title
        self.contents = contents
        self.phone_number = phone_number

    def reading_time(self, wpm):
        if not isinstance(wpm, int):
            raise TypeError("Enter an integer")
        
        if wpm <= 0:
            raise ValueError("Enter a positive value")

        return len(self.contents.split()) / wpm