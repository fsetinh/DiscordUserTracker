from db.db_connect import exe
import datetime
import json

query = """
SELECT 
    user.discord_user, 
    user.discord_id, 
    user.creation_date, 
    user.join_date,
    user_name_history.users_change_history
FROM users user
LEFT JOIN users_history user_name_history ON user.key = user_name_history.`users_key`
"""

def parse_users(type_return: int = 1):
    response = exe(query)
    parsed_data1 = []
    parsed_data2 = []

    for entry in response:
        discord_username, discord_id, creation_date, join_date, users_change_history_str = entry

        # Parse the change history JSON
        if users_change_history_str:
            change_history = json.loads(users_change_history_str.replace("'", '"'))
        else:
            change_history = []

        # Format dates to ISO format
        join_date = join_date.isoformat()
        creation_date = creation_date.isoformat()

        # Prepare data formats
        user_data1 = {
            "current_username": discord_username,
            "discord_id": discord_id,
            "join_date": join_date,
            "creation_date": creation_date,
            "username_history": [entry['old_username'] for entry in change_history],
        }
        user_his = [
            f"{entry['old_username']} on {entry['change_date']}" for entry in change_history
        ]
        user_his_parse = ", ".join(user_his)

        user_data2 = {
            "Current Username": discord_username,
            "Discord ID": discord_id,
            "Join Date": join_date,
            "Creation Date": creation_date,
            "Username History": user_his_parse,
        }

        parsed_data1.append(user_data1)
        parsed_data2.append(user_data2)

    if type_return == 1:
        json_data = json.dumps(parsed_data1, indent=4)
        return json_data
    elif type_return == 2:
        return parsed_data2
    else:
        return 'No data returned.'
