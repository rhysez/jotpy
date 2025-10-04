def display_menu_options() -> None:
    print("Menu Options:")
    print("1. Create Note")
    print("2. View Notes")
    print("3. Update Note")
    print("4. Delete Note")
    print("5. Exit")

def get_user_input(prompt: str) -> str:
    return input(prompt)