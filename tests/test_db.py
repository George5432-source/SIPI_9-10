import unittest
import pandas as pd
import sqlite3
import os
from unittest.mock import patch, MagicMock
import streamlit as st
import pages.page2 as page2  # ✅ Proper import


class TestFlatFilter(unittest.TestCase):

    def setUp(self):
        # Setup: create test database
        self.test_db = "test_flats.db"
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS flats (
            price REAL,
            level INTEGER,
            levels INTEGER,
            rooms INTEGER,
            area REAL,
            kitchen_area REAL
        )
        """)
        cursor.executemany("INSERT INTO flats VALUES (?, ?, ?, ?, ?, ?)", [
            (1000, 2, 5, 2, 50.0, 10.0),
            (2000, 3, 5, 3, 70.0, 15.0),
            (1500, 1, 3, 1, 40.0, 8.0),
        ])
        conn.commit()
        conn.close()

        # Patch the DB_PATH in page2 to use test DB
        page2.DB_PATH = self.test_db

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_sql_injection_protection(self):
        query = "SELECT * FROM flats WHERE price > ?"
        malicious_input = "1000; DROP TABLE flats"
        try:
            df = page2.load_filtered_data(query, [malicious_input])
            self.assertIsNotNone(df)  # Проверка, что не возникло исключений
        except Exception as e:
            self.fail(f"SQL injection raised an error: {e}")

    def test_load_filtered_data_no_conditions(self):
        query = "SELECT * FROM flats WHERE 1=1"
        df = page2.load_filtered_data(query, [])
        self.assertEqual(len(df), 3)

    def test_load_filtered_data_with_condition(self):
        query = "SELECT * FROM flats WHERE price > ?"
        df = page2.load_filtered_data(query, [1200])
        self.assertTrue(all(df["price"] > 1200))

    def test_operator_functions(self):
        df = pd.DataFrame({"price": [100, 200, 300]})
        cond = page2.OPERATORS[">"](df, "price", 150)
        self.assertFalse(cond.iloc[0])
        self.assertTrue(cond.iloc[1])
        self.assertTrue(cond.iloc[2])

    def test_add_condition_to_session_state(self):
        st.session_state.conditions = []
        st.session_state.conditions.append(("price", ">", 1000))
        self.assertIn(("price", ">", 1000), st.session_state.conditions)

    @patch('pages.page2.load_filtered_data')
    def test_search_button_functionality(self, mock_load):
        mock_load.return_value = pd.DataFrame({
            "price": [1500],
            "level": [2],
            "levels": [5],
            "rooms": [2],
            "area": [55.0],
            "kitchen_area": [10.0]
        })

        st.session_state.conditions = [("price", ">", 1000)]

        query = "SELECT * FROM flats WHERE 1=1"
        params = []
        for field, op, value in st.session_state.conditions:
            query += f" AND {field} {op} ?"
            params.append(value)

        df = page2.load_filtered_data(query, params)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["price"], 1500)



if __name__ == '__main__':
    unittest.main()
