import nltk
from nltk.tokenize import word_tokenize

# Import your database class
from database import Database

# Download required NLTK resources (comment out if already downloaded)
nltk.download('punkt')

# Define some basic responses
greetings = ["hello", "hi", "hey"]
farewells = ["bye", "goodbye", "see you later"]
thanks = ["thank you", "thanks"]


def main():
  # Initialize the database connection
  db = Database("chatbot.db")

  # Get user input
  while True:
    user_input = input("You: ")
    user_input = user_input.lower()

    # Process user input (basic tokenization)
    words = word_tokenize(user_input)

    # Check for greetings, farewells, and thanks
    if any(word in words for word in greetings):
      response = "Hello there! How can I help you today?"
    elif any(word in words for word in farewells):
      response = "Goodbye! Have a nice day."
      break  # Exit the loop on farewell
    elif any(word in words for word in thanks):
      response = "You're welcome!"
    else:
      # Simple echo response (can be replaced with more sophisticated logic)
      response = f"You said: {user_input}"

    # Store user message in the database
    db.insert_data("messages", (user_input, ))

    print(f"Chatbot: {response}")

  # Close the database connection
  db.close_connection()


if __name__ == "__main__":
  main()