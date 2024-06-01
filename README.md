# NBA Connections

NBA Connections is a Python application that scrapes data from Basketball Reference to create unique groups of NBA players based on different criteria. The application uses a Tkinter GUI to allow users to interact with the player groups and verify if their selections match predefined groups.

## Features

- Scrapes player data from Basketball Reference based on different criteria (birthplace, birth year, college, teams played for).
- Randomly selects criteria (year, state, college, teams) to create diverse groups.
- Ensures unique groups of players for each run.
- Provides a user-friendly Tkinter GUI for interacting with player groups.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/NBA-Connections.git
    cd NBA-Connections
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have `get_Players.py` which contains the `get_unique_player_groups` function.

## Usage

1. Run the application:

    ```bash
    python main.py
    ```

2. The Tkinter GUI will open, displaying buttons for each player. Select players to form a group and click "Submit" to verify if the selected players form a correct group.

## File Structure

- `main.py`: The main application script that sets up the Tkinter GUI and handles user interactions.
- `get_Players.py`: Contains the functions to scrape data from Basketball Reference and create unique player groups.
- `requirements.txt`: Lists the required Python packages.

## Code Explanation

### main.py

This script initializes the Tkinter GUI, retrieves unique player groups, and handles user interactions to verify player selections.

### get_Players.py

This script contains functions to:
- Scrape player data from Basketball Reference (`scrape_basketball_reference`).
- Randomly select criteria and create URLs (`get_random_urls`).
- Ensure unique player groups (`ensure_unique_groups`).
- Retrieve unique player groups (`get_unique_player_groups`).

## Example Output

```plaintext
Group 1 (NBA and ABA Players who played for Alabama): ['Player1', 'Player2', 'Player3', 'Player4']
Group 2 (NBA and ABA Players who played for Auburn): ['Player5', 'Player6', 'Player7', 'Player8']
...
