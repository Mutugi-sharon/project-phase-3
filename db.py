import sqlite3

def connect():
    # Connect to the SQLite database, creating it if necessary
    conn = sqlite3.connect('moesha_fundraising.db')
    return conn

def create_table():
    conn = connect()
    cursor = conn.cursor()
    
    # Create the donations table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS donations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            donor_name TEXT NOT NULL,
            donation_type TEXT NOT NULL,
            amount_or_quantity TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
