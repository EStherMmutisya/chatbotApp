import sqlite3

class Database:
  """Connects to and interacts with a SQLite database."""

  def __init__(self, db_file):
    """Initializes the database connection."""
    self.conn = sqlite3.connect(db_file)
    self.cursor = self.conn.cursor()

  def create_table(self, table_name, columns):
    """Creates a table in the database."""
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"""
    self.cursor.execute(query)
    self.conn.commit()

  def insert_data(self, table_name, data):
    """Inserts data into a table."""
    placeholders = ', '.join('?' * len(data))
    query = f"""INSERT INTO {table_name} VALUES ({placeholders})"""
    self.cursor.execute(query, data)
    self.conn.commit()

  def select_data(self, table_name, condition=None, values=None):
    """Selects data from a table."""
    query = f"SELECT * FROM {table_name}"
    if condition:
      query += f" WHERE {condition}"
    self.cursor.execute(query, values if values else [])
    return self.cursor.fetchall()

  def update_data(self, table_name, data, condition, values):
    """Updates data in a table."""
    set_clause = ', '.join(f"{key} = ?" for key in data.keys())
    query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
    self.cursor.execute(query, [*data.values(), *values])
    self.conn.commit()

  def delete_data(self, table_name, condition, values=None):
    """Deletes data from a table."""
    query = f"DELETE FROM {table_name} WHERE {condition}"
    self.cursor.execute(query, values if values else [])
    self.conn.commit()

  def close_connection(self):
    """Closes the database connection."""
    self.conn.close()

# Example usage
if __name__ == "__main__":
  db = Database("chatbot.db")

  # Create a table to store user messages
  db.create_table("messages", ["user_id", "message_text", "timestamp"])

  # Insert a sample message
  db.insert_data("messages", (1, "Hello!", "2024-08-19 18:23:00"))

  # Select all messages
  messages = db.select_data("messages")
  for message in messages:
    print(f"User ID: {message[0]}, Message: {message[1]}, Timestamp: {message[2]}")

  # Close the database connection
  db.close_connection()