# Represents a note.
from typing import Self
import uuid

class Note:
    def __init__(self, id, title, content, is_important) -> None:
        self.id = id
        self.title = title
        self.content = content
        self.is_important = is_important

    def save(self, cursor) -> Self:
        # Logic to save the note to DB.
        try:
            cursor.execute(
                "INSERT INTO notes (id, title, content, is_important) VALUES (?, ?, ?, ?)",
                (self.id, self.title, self.content, self.is_important)
            )
            cursor.connection.commit()
        except Exception as e:
            print(f"Error saving note: {e}")

        return self

    # TODO: Implement method.
    def update(self, cursor, title, content, is_important):
        self.title = title
        self.content = content
        self.is_important = is_important
        # Logic to update the note in DB.
        return self

    # TODO: Implement method.
    def delete(self, cursor):
        # Logic to delete the note from DB.
        return self

    @staticmethod
    def list(cursor) -> list[Self]:
        # Logic to list all notes from DB.
        try:
            cursor.execute("SELECT id, title, content, is_important FROM notes")
            rows = cursor.fetchall()
            notes = [Note(row[0], row[1], row[2], bool(row[3])) for row in rows]
            return notes
        except Exception as e:
            print(f"Error fetching notes: {e}")