import sys
import subprocess
import platform
import os


def main():
    OS = platform.system()

    # Change to the 'src' directory
    if os.path.exists('src'):
        os.chdir('src')
    else:
        print("The 'src' directory does not exist.")
        sys.exit(1)

    # Run the main.py script from the src folder
    if OS == 'Windows':
        print("\nDetected Windows Operating System. Running main.py from src folder...")
        subprocess.run(['python', 'main.py'], check=True)
    elif OS == 'Linux':
        print(f"\nDetected {OS} Operating System. Running main.py from src folder...")
        subprocess.run(['python3', 'main.py'], check=True)
    else:
        print(f"Unsupported Operating System: {OS}. Unable to run the script.")
        sys.exit(1)


if __name__ == '__main__':
    main()
