def eval_user_input() -> str | None:
    try:
        line = input("JotPy> ")   
        return line
    except Exception as e:
        print(f"Error: {e}")
        return None