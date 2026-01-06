import datetime

def print_welcome():
    """
    Simple script to welcome new developers to the terminal.
    """
    today = datetime.date.today()
    print("--------------------------------------------------")
    print(f"   Welcome to the BrightByte Data Team Terminal!   ")
    print(f"   Current Date: {today}")
    print("   Remember: Always pull before you push!         ")
    print("--------------------------------------------------")

if __name__ == "__main__":
    print_welcome()