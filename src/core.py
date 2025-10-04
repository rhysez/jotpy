import uuid
from classes.note import Note
from utils.input import eval_user_input
from utils.menu import display_menu_options
import datetime
import sqlite3

# Program entry point.
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

def run_session(session: bool, cursor: sqlite3.Cursor) -> None:
    while session:
        user_response = eval_user_input()
        if user_response in ["5", "exit", "quit"] or user_response is None:
            session = False
            print("Exiting JotPy. Goodbye!")
        else:
            try:
                process_map[user_response](cursor)
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

process_map = {
    "1": process_create,
    "2": process_view,
}