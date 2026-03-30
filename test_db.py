import os
import psycopg2
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

def test_connection():
    try:
        # Get the URL from your .env
        db_url = os.getenv("DATABASE_URL")
        
        if not db_url:
            print("❌ Error: DATABASE_URL not found in .env file.")
            return

        # Connect to Neon
        print("Connecting to Neon...")
        conn = psycopg2.connect(db_url)
        
        # Create a cursor to perform operations
        cur = conn.cursor()
        
        # Execute a simple query
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        
        print("✅ Connection Successful!")
        print(f"Connected to: {db_version[0]}")
        
        cur.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Connection Failed: {e}")

if __name__ == "__main__":
    test_connection()