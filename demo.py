import sqlite3

# In-memory DB for demo
conn = sqlite3.connect(":memory:")
c = conn.cursor()

# Setup
c.execute("CREATE TABLE users (username TEXT, password TEXT)")
c.execute("INSERT INTO users VALUES ('admin','password123')")
conn.commit()

def unsafe_login(user, pwd):
    # Vulnerable string concatenation (DO NOT USE)
    query = f"SELECT * FROM users WHERE username='{user}' AND password='{pwd}'"
    print("[UNSAFE QUERY]:", query)
    try:
        return c.execute(query).fetchone()
    except sqlite3.Error as e:
        print("Error:", e)
        return None

def safe_login(user, pwd):
    # Parameterized query (Safe)
    query = "SELECT * FROM users WHERE username=? AND password=?"
    print("[SAFE QUERY]:", query)
    return c.execute(query, (user, pwd)).fetchone()

if __name__ == "__main__":
    print("Attempting SQL injection on UNSAFE login:")
    result_unsafe = unsafe_login("admin", "' OR '1'='1")
    print("Unsafe result:", result_unsafe)

    print("\nAttempting SQL injection on SAFE login:")
    result_safe = safe_login("admin", "' OR '1'='1")
    print("Safe result:", result_safe)
