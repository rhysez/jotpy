# Represents a note.
from typing import Self
import uuid

class Note:
    def __init__(self, id, title, content, is_important) -> None:
        self.id = id
        self.title = title
        self.content = content
        self.is_important = is_important

    @staticmethod
    def list(cursor) -> list[Self]:
        try:
            cursor.execute("SELECT id, title, content, is_important FROM notes")
            rows = cursor.fetchall()
            notes = [Note(row[0], row[1], row[2], bool(row[3])) for row in rows]
            return notes
        except Exception as e:
            print(f"Error fetching notes: {e}")
    
    @staticmethod
    def get(cursor, note_id) -> Self | None:
        try:
            cursor.execute(
                "SELECT id, title, content, is_important FROM notes WHERE id = ?",
                (note_id,)
            )
            row = cursor.fetchone()
            if row:
                return Note(row[0], row[1], row[2], bool(row[3]))
            return None
        except Exception as e:
            print(f"Error fetching note: {e}")
            return None

    def save(self, cursor) -> Self:
        try:
            cursor.execute(
                """
                INSERT INTO notes (id, title, content, is_important) 
                VALUES (?, ?, ?, ?)
                """,
                (self.id, self.title, self.content, self.is_important)
            )
            cursor.connection.commit()
        except Exception as e:
            print(f"Error saving note: {e}")

        return self

    def update(self, cursor, title, content, is_important):
        self.title = title
        self.content = content
        self.is_important = is_important
        
        try:
            cursor.execute(
                """
                UPDATE notes
                SET title = ?, content = ?, is_important = ?
                WHERE id = ?
                """,
                (self.title, self.content, self.is_important, self.id)
            )
            cursor.connection.commit()
        except Exception as e:
            print(f"Error updating note: {e}")

        return self

    def delete(self, cursor):
        try:
            cursor.execute(
                "DELETE FROM notes WHERE id = ?",
                (self.id,)
            )
            cursor.connection.commit()
        except Exception as e:
            print(f"Error deleting note: {e}")