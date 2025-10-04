from core import main
# Application entry point.

# /-- Program psuedocode --/
# 1. Display welcome message, current date/time, and menu of options.
# 2. If creating a note, prompt for title, content, and importance, and then create an entry in SQLite DB.
# 3. If viewing notes, fetch and display all notes from SQLite DB.

# __name__ variable set to "__main__" when the script is executed directly.
if __name__ == "__main__":
    main()