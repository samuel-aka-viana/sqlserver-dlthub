import pyodbc
import time


def test_sql_server_connection():
    # Wait a bit to ensure SQL Server is ready
    print("Waiting for SQL Server to be ready...")
    time.sleep(10)

    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost,1433;"
        "DATABASE=SampleDB;"
        "UID=sa;"
        "PWD=StrongPassword123!;"
        "TrustServerCertificate=yes;"
        "Encrypt=no;"
        "Connection Timeout=30;"
        "Login Timeout=30;"
    )

    try:
        print("Attempting to connect to SQL Server...")
        conn = pyodbc.connect(connection_string)
        print("✅ Connection successful!")

        # Test a simple query
        cursor = conn.cursor()
        cursor.execute("SELECT 1 as test")
        result = cursor.fetchone()
        print(f"✅ Query successful: {result}")

        # Check if our database exists
        cursor.execute("SELECT name FROM sys.databases WHERE name = 'SampleDB'")
        db_result = cursor.fetchone()
        if db_result:
            print("✅ SampleDB database found")
        else:
            print("❌ SampleDB database not found")

        # Check if our tables exist
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_CATALOG = 'SampleDB'")
        tables = cursor.fetchall()
        print(f"📋 Tables found: {[table[0] for table in tables]}")

        conn.close()

    except pyodbc.Error as e:
        print(f"❌ Connection failed: {e}")
        return False

    return True


if __name__ == "__main__":
    test_sql_server_connection()