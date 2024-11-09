from db.user_data_parse import parse_users
import pandas as pd
from rich.console import Console
from rich.table import Table

def show_table():
    data = parse_users(2)
    df = pd.DataFrame(data)

    table = Table(title="User Data")
    columns = df.columns.tolist()
    rows = df.values.tolist()

    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*[str(el) for el in row], style="bright_green")

    console = Console()
    console.print(table)