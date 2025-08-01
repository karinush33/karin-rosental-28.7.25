import psycopg2
import psycopg2.extras


try:
    conn = psycopg2.connect(
        dbname='my_db',
        user='postgres',
        password='admin123',
        host='localhost',
        port='5432',
        cursor_factory=psycopg2.extras.RealDictCursor
    )
    print("🎉 connected successfully")
except psycopg2.Error as e:
    print("😢 connection error:", e)



try:
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            price NUMERIC(6, 2) NOT NULL,
            in_stock BOOLEAN DEFAULT TRUE
        );
    """)
    conn.commit()
    print("✅ table created successfully!")

except psycopg2.Error as e:
    print("❌table creation has failed:", e)

try:
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO products (name, price,in_stock) VALUES (%s, %s, %s)",
        ("laptop", "3200.50", "TRUE")
    )
    conn.commit()
    print("Data inserted.")
except psycopg2.Error as e:
    print("Insert error:", e)
finally:
    cur.close()

try:
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE in_stock=TRUE")
    rows = cur.fetchall()
    for row in rows:
        print(row)
except psycopg2.Error as e:
    print("Select error:", e)
finally:
    cur.close()