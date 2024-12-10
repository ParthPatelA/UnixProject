import os
import time

# Define the path to the Lektor project directory
PROJECT_DIR = "/home/parth/project2"
LKT_PROJECT_FILE = os.path.join(PROJECT_DIR, "project2.lektorproject")

# List of themes to rotate
THEMES = ["nix", "terminal", "simple-strap", "resume"]

# Time interval for switching themes (in seconds)
INTERVAL = 60

# Ensure the project file exists
if not os.path.exists(LKT_PROJECT_FILE):
    print(f"Error: Project file '{LKT_PROJECT_FILE}' does not exist!")
    exit(1)


def switch_theme(current_theme_index):
    """Switch to the next theme and restart the Lektor server."""
    next_theme = THEMES[current_theme_index]

    # Update the theme in the lektorproject file
    with open(LKT_PROJECT_FILE, "r") as file:
        lines = file.readlines()

    with open(LKT_PROJECT_FILE, "w") as file:
        for line in lines:
            if line.startswith("theme ="):
                file.write(f"theme = {next_theme}\n")
            else:
                file.write(line)

    print(f"Switched to theme: {next_theme}")

    # Restart the Lektor server
    os.system("pkill -f 'lektor server'")  # Kill any running Lektor server
    os.system(f"nohup lektor server -f {PROJECT_DIR} &")  # Restart the server


def main():
    current_theme_index = 0

    while True:
        # Switch to the next theme
        switch_theme(current_theme_index)

        # Update the index for the next theme
        current_theme_index = (current_theme_index + 1) % len(THEMES)

        # Wait for the specified interval
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
