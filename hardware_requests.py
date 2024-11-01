import sqlite3
from datetime import datetime

# Function to initialize the database and create a table
def create_table():
    conn = sqlite3.connect('hardware_requests.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS requests (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      mechanic_name TEXT NOT NULL,
                      hardware_item TEXT NOT NULL,
                      quantity INTEGER NOT NULL,
                      request_date TEXT NOT NULL,
                      status TEXT DEFAULT 'Pending')''')
    conn.commit()
    conn.close()

# Function to submit a new hardware request
def submit_request(mechanic_name, hardware_item, quantity):
    conn = sqlite3.connect('hardware_requests.db')
    cursor = conn.cursor()
    request_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''INSERT INTO requests (mechanic_name, hardware_item, quantity, request_date)
                      VALUES (?, ?, ?, ?)''', (mechanic_name, hardware_item, quantity, request_date))
    conn.commit()
    conn.close()
    print(f"Request for {quantity} {hardware_item}(s) submitted successfully.")

# Function to retrieve all hardware requests
def view_requests():
    conn = sqlite3.connect('hardware_requests.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM requests')
    requests = cursor.fetchall()
    conn.close()
    return requests

# Function to update the status of a request
def update_status(request_id, new_status):
    conn = sqlite3.connect('hardware_requests.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE requests SET status = ? WHERE id = ?''', (new_status, request_id))
    conn.commit()
    conn.close()
    print(f"Request ID {request_id} status updated to '{new_status}'.")

# Main function to demonstrate functionality
if __name__ == "__main__":
    # Initialize database and create table if not exists
    create_table()

    # Mechanics submit requests
    submit_request('John Doe', 'Screwdriver', 5)
    submit_request('Jane Smith', 'Wrench', 3)

    # View all requests (Admin)
    print("\nAll Requests:")
    all_requests = view_requests()
    for request in all_requests:
        print(request)

    # Update the status of a specific request
    update_status(1, 'Approved')  # Update request ID 1 to "Approved"

    # View all requests after updating
    print("\nUpdated Requests:")
    updated_requests = view_requests()
    for request in updated_requests:
        print(request)
