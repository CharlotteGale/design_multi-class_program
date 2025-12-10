class DiaryEntry:
    def __init__(self, title, contents, phone_number=None):
        self.title = title
        self.contents = contents
        self.phone_number = phone_number

    def reading_time(self, wpm):
        return len(self.contents.split()) / wpm