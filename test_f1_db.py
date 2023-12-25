import unittest
import sqlite3
from f1_db import *

class TestF1DB(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

    def tearDown(self):
        self.con.close()

    def test_create_tables(self):
        # Check if the tables are created
        self.cur.execute(f"SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.cur.fetchall()
        table_names = [table[0] for table in tables]
        self.assertIn(t_std_name, table_names)
        self.assertIn(t_std_sub, table_names)
        self.assertIn(t_std_mark, table_names)

    def test_insert_data(self):
        # Check if the sample data is inserted
        self.cur.execute(f"SELECT * FROM {t_std_name}")
        std_name_data = self.cur.fetchall()
        self.assertEqual(len(std_name_data), 1)
        self.assertEqual(std_name_data[0][0], sample_std[0])
        self.assertEqual(std_name_data[0][1], sample_std[1])
        self.assertEqual(std_name_data[0][2], sample_std[2])

        self.cur.execute(f"SELECT * FROM {t_std_sub}")
        std_sub_data = self.cur.fetchall()
        self.assertEqual(len(std_sub_data), 1)
        self.assertEqual(std_sub_data[0][0], ssub[0])
        self.assertEqual(std_sub_data[0][1], ssub[1])
        self.assertEqual(std_sub_data[0][2], ssub[2])
        self.assertEqual(std_sub_data[0][3], ssub[3])
        self.assertEqual(std_sub_data[0][4], ssub[4])

        self.cur.execute(f"SELECT * FROM {t_std_mark}")
        std_mark_data = self.cur.fetchall()
        self.assertEqual(len(std_mark_data), 1)
        self.assertEqual(std_mark_data[0][0], sout[0])
        self.assertEqual(std_mark_data[0][1], sout[1])
        self.assertEqual(std_mark_data[0][2], sout[2])
        self.assertEqual(std_mark_data[0][3], sout[3])
        self.assertEqual(std_mark_data[0][4], sout[4])
        self.assertEqual(std_mark_data[0][5], sout[5])

if __name__ == '__main__':
    unittest.main()