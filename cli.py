import argparse
from main import main   # Import your main function

def parse_arguments():
  """Parses command-line arguments."""
  parser = argparse.ArgumentParser(description="Chatbot CLI")
  parser.add_argument("-d", "--database", type=str, default="chatbot.db",
                      help="Path to the database file (default: chatbot.db)")
  return parser.parse_args()

def main_cli():
  """Entry point for the CLI."""
  args = parse_arguments()
  main(database_path=args.database)  # Pass database path to main function

if __name__ == "__main__":
  main_cli()