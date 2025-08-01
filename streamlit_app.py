import streamlit as st
import psycopg2
import psycopg2.extras


st.title("👩‍💻 Karin's Streamlit Calculator App")

num1 = st.text_input("Enter first number:")
num2 = st.text_input("Enter second number:")

if st.button("add"):
    try:
        result = float(num1) + float(num2)
        st.success(f"The result is: {result}")
    except ValueError:
        st.error("Please enter valid numbers.")

st.subheader("Available Products")


if st.button("Show Products"):
    try:
        conn = psycopg2.connect(
            dbname='my_db',
            user='postgres',
            password='admin123',
            host='localhost',
            port='5432',
            cursor_factory=psycopg2.extras.RealDictCursor
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE in_stock = TRUE")
        rows = cur.fetchall()
        for row in rows:
            st.markdown(f"""
            📦 **{row['name']}**
            - 💰 Price: {row['price']} ₪  
            - ✅ In Stock: {row['in_stock']}
            --- 
            """)
    except psycopg2.Error as e:
        st.error(f"Database error: {e}")
    finally:
        cur.close()
        conn.close()