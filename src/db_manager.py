import sqlite3

class DBManager:
    def __init__(self, db_path="db/lms_library.sqlite3"):
        """Initialize and maintain a persistent connection."""
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """Ensure the connection remains open."""
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row
        return self.connection

    def execute_query(self, query, values=None):
        """Execute INSERT, UPDATE, DELETE queries using persistent connection."""
        conn = self.connect()
        cursor = conn.cursor()
        try:
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            conn.commit()
        except sqlite3.Error as e:
            print(f"SQLite Error: {e}")
        finally:
            cursor.close()

    def fetch_data(self, query, values=None):
        """Fetch and return data using persistent connection."""
        conn = self.connect()
        cursor = conn.cursor()
        try:
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            results = cursor.fetchall()
            return [dict(row) for row in results]
        except sqlite3.Error as e:
            print(f"SQLite Error: {e}")
            return None
        finally:
            cursor.close()

    def create_tables(self):
        """Ensure all required tables exist."""
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_addbook (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publisher TEXT NOT NULL,
            isAvail BOOLEAN DEFAULT TRUE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_addmember (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            mobile TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_issue (
            bookID INTEGER,
            memberID INTEGER,
            issueTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            renewCount INTEGER DEFAULT 0,
            FOREIGN KEY (bookID) REFERENCES tbl_addbook(id),
            FOREIGN KEY (memberID) REFERENCES tbl_addmember(id)
        )
        """)

        conn.commit()
        print("Tables created successfully!")

    def reset_tables(self):
        """Removes all data from all tables while keeping the schema intact."""
        conn = self.connect()
        cursor = conn.cursor()

        try:
            tables = ["tbl_addbook", "tbl_addmember", "tbl_issue"]  # List of tables to reset
            for table in tables:
                cursor.execute(f"DELETE FROM {table}")  # Deletes all rows

            conn.commit()
            print("All tables have been cleared successfully!")

        except sqlite3.Error as e:
            print(f"SQLite Error while resetting tables: {e}")

        finally:
            cursor.close()

    def close_connection(self):
        """Close the database connection when the app shuts down."""
        if self.connection:
            self.connection.close()
            self.connection = None


db_manager = DBManager()

# db_manager.create_tables()
# db_manager.reset_tables()
