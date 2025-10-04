from classes.note import Note
from utils.input import eval_user_input
from utils.menu import display_menu_options
import datetime

# Program entry point.
def main() -> int:
    session = True

    print("Welcome to JotPy!")
    print(f"Today is {datetime.datetime.now().strftime('%A %d %B %Y')}")

    display_menu_options()
    run_session(session)
    
    return 0

def run_session(session: bool) -> None:
    while session:
        user_response = eval_user_input()
        if user_response in ["5", "exit", "quit"] or user_response is None:
            session = False
            print("Exiting JotPy. Goodbye!")
        else:
            try:
                process_map[user_response]()
            except KeyError:
                print("Invalid option. Please try again.")

def process_create() -> None:
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    is_important = input("Is this note important? (y/n): ").lower()
    is_important = is_important in ["y", "yes"]

    note = Note(title, content, is_important)
    note.save()

    print(f"Successfully created note '{note.title}'.")
    display_menu_options()

process_map = {
    "1": process_create,
}