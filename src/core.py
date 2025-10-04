import uuid
import datetime
import sqlite3
from classes.note import Note
from classes.process import Process
from utils.menu import eval_menu_input
from utils.menu import display_menu_options


# Program entry point.
# Handles database connection and bootstrapping if necessary.
def main() -> int:
    session = True
    db = db_connect()
    connection = db[0]
    cursor = db[1]

    print("Initializing database...")
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS notes (id TEXT PRIMARY KEY, title TEXT, content TEXT, is_important BOOLEAN)")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
        return 1

    print("Welcome to JotPy!")
    print(f"Today is {datetime.datetime.now().strftime('%A %d %B %Y')}")

    display_menu_options()
    run_session(session, cursor)
    
    return 0

# The main application loop where user requests are processed.
def run_session(session: bool, cursor: sqlite3.Cursor) -> None:
    while session:
        user_response = eval_menu_input()
        process = Process(user_response) if user_response in [p.value for p in Process] else None
        if process in ["5", "exit", "quit"] or process is None:
            session = False
            print("Exiting JotPy. Goodbye!")
        else:
            try:
                process_map[process](cursor)
            except KeyError:
                print("Invalid option. Please try again.")

def db_connect():
    try:
        connection = sqlite3.connect("jotpy.db")
        cursor = connection.cursor()
        return connection, cursor
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None, None


def process_create(cursor: sqlite3.Cursor) -> None:
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    is_important = input("Is this note important? (y/n): ").lower()
    is_important = is_important in ["y", "yes"]

    note = Note(str(uuid.uuid4()), title, content, is_important)
    note.save(cursor)

    print(f"Successfully created note '{note.title}'.")
    display_menu_options()

def process_view(cursor: sqlite3.Cursor) -> None:
    notes = Note.list(cursor)
    if not notes:
        print("No notes found.")
    else:
        for note in notes:
            importance = "Important" if note.is_important else "Normal"
            print(f"ID: {note.id} | Title: {note.title} | Importance: {importance}\nContent: {note.content}\n---")

    display_menu_options()

def process_update(cursor: sqlite3.Cursor) -> None:
    note_id = input("Enter the ID of the note to update: ")

    # We're checking if the note exists before attempting to update.
    note = Note.get(cursor, note_id)
    if not note:
        print("Error: Could not find a note with this ID.")
        display_menu_options()
        return

    title = input("Enter new note title: ")
    content = input("Enter new note content: ")
    is_important = input("Is this note important? (y/n): ").lower()
    is_important = is_important in ["y", "yes"]

    note.update(cursor, title, content, is_important)
    print(f"Successfully updated note '{note.title}'.")

    display_menu_options()

def process_delete(cursor: sqlite3.Cursor) -> None:
    note_id = input("Enter the ID of the note to delete: ")

    # We're checking if the note exists before attempting to delete.
    note = Note.get(cursor, note_id)
    if not note:
        print("Error: Could not find a note with this ID.")
        display_menu_options()
        return

    note.delete(cursor)
    print(f"Successfully deleted note '{note.title}'.")

    display_menu_options()

# Maps user input to processing functions.
# Uses the Process enum for clarity.
process_map = {
    Process.CREATE: process_create,
    Process.VIEW: process_view,
    Process.UPDATE: process_update,
    Process.DELETE: process_delete,
}