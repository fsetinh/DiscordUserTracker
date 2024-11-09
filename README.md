
# Discord Tracker

This application uses multiple Discord user accounts to scan and track the username history of members in servers. The project is currently a work in progress.

## Project Structure

```plaintext
discord_logger/
├── db/
│   ├── __init__.py
│   ├── db_connect.py         # Handles database connections and queries
│   ├── display_table.py      # Displays database tables and data
│   └── user_data_parse.py    # Parses user data, including username history
│
├── listeners/
│   ├── __init__.py
│   └── main.py               # Main event listeners for Discord interactions
│
└── README.md                 # Project overview and documentation
```

### Folder Details

- **db**: Contains modules related to database operations.
  - **db_connect.py**: Handles connecting to the database, including executing queries.
  - **display_table.py**: Provides functionality to display tables and relevant data from the database.
  - **user_data_parse.py**: Parses user data, particularly focusing on username history tracking.

- **listeners**: Contains modules that manage event listeners.
  - **main.py**: Handles main Discord events and interactions, such as scanning members in servers.

## Requirements

- Python 3.x
- Required packages (listed in `requirements.txt`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/fsetinh/discordusertracker.git
   cd Discord_Tracker
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure your database connection in `db/db_connect.py`.

## Usage

1. Run the main program:

   ```bash
   python listeners/main.py
   ```

   This will start the bot, which will use the Discord user accounts to scan and track username history in the servers it's connected to.

2. View tracked data using the `display_table.py` module for quick insights.

## Contributing

This project is a work in progress. Contributions are welcome to improve functionality and add features.
