from classes.process import Process

def display_menu_options() -> None:
    print("Menu Options:")
    print("1. Create Note")
    print("2. View Notes")
    print("3. Update Note")
    print("4. Delete Note")
    print("5. Exit")

def eval_menu_input() -> str | None:
    try:
        line = input("JotPy> ")
        return line
    except Exception as e:
        print(f"Error: {e}")
        return None