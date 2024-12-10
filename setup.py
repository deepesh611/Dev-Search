import sys
import time
import platform
import subprocess


def main():
    os = platform.system()

    try:
        if os == 'Windows':
            print("\nDetected Windows Operating System. Running setup.ps1...")
            subprocess.run(['powershell', '-ExecutionPolicy', 'ByPass', '-File', 'src/setup.ps1'], check=True)

        elif os == 'Linux' or os == 'Darwin':
            print(f"\nDetected {os} Operating System. Running setup.sh...")
            subprocess.run(['bash', 'src/setup.sh'], check=True)

        else:
            print(f"Unsupported Operating System: {os}. Unable to run the setup script.")
            time.sleep(1)
            print("Please refer to the Installation Guidelines for manual setup of the application.")
            time.sleep(3)
            sys.exit(1)

    except subprocess.CalledProcessError as e:
        print(f"\nError: Setup script failed with the error code {e.returncode}.")
        sys.exit(1)

    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
