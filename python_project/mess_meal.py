import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('mess_management.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        room_number TEXT,
        dietary_preference TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS meals (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        date DATE,
        meal_type TEXT,
        cost REAL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

# Function to add a new user
def add_user(name, room_number, dietary_preference):
    cursor.execute('INSERT INTO users (name, room_number, dietary_preference) VALUES (?, ?, ?)',
                   (name, room_number, dietary_preference))
    conn.commit()

# Function to add a meal
def add_meal(user_id, date, meal_type, cost):
    cursor.execute('INSERT INTO meals (user_id, date, meal_type, cost) VALUES (?, ?, ?, ?)',
                   (user_id, date, meal_type, cost))
    conn.commit()

# Function to generate an expense report
def generate_expense_report(user_id, start_date, end_date):
    cursor.execute('SELECT date, meal_type, cost FROM meals WHERE user_id = ? AND date BETWEEN ? AND ?',
                   (user_id, start_date, end_date))
    expenses = cursor.fetchall()
    
    total_cost = sum(expense[2] for expense in expenses)
    
    print(f"Expense report for user {user_id} from {start_date} to {end_date}:")
    for expense in expenses:
        print(f"{expense[0]} - {expense[1]}: ${expense[2]}")
    print(f"Total Cost: ${total_cost}")

# Example usage
add_user("John Doe", "A101", "Vegetarian")
add_user("Jane Smith", "B202", "Non-Vegetarian")

add_meal(1, "2023-08-30", "Lunch", 5.0)
add_meal(1, "2023-08-30", "Dinner", 6.5)
add_meal(2, "2023-08-30", "Lunch", 6.0)

generate_expense_report(1, "2023-08-01", "2023-08-31")

# Close the connection to the database
conn.close()
