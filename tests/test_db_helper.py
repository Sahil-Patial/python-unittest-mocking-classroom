import mysql.connector as connection
import unittest
from src.db_helper import DbHelper

mdb =connection.connect(host="localhost", user="root", passwd="20102001Sp$",database = "employees")
mycur=mdb.cursor(buffered=True)

class TestDbHelper(unittest.TestCase):
    def setUp(self):
        self.db=DbHelper()

    def test_max_salary_is_greater_than_min_salary(self):
        dbhelper=DbHelper()
        max_salary=dbhelper.get_maximum_salary(mycur)
        min_salary=dbhelper.get_minimum_salary(mycur)
        self.assertGreater(max_salary,min_salary)
