# Represents a note.
from typing import Self

class Note:
    def __init__(self, title, content, is_important) -> None:
        self.title = title
        self.content = content
        self.is_important = is_important

    def save(self) -> Self:
        # Logic to save the note to DB.
        return self

    def update(self, title, content, is_important):
        self.title = title
        self.content = content
        self.is_important = is_important
        # Logic to update the note in DB.
        return self

    def delete(self):
        # Logic to delete the note from DB.
        return self

    @staticmethod
    def list():
        # Logic to list all notes from DB.
        return []