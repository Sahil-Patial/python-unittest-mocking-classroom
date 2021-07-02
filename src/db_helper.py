import mysql.connector as connection

class DbHelper:
    def get_maximum_salary(self,mycur):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        mycur.execute("select max(salary) from salaries")

        return mycur.fetchone()

    def get_minimum_salary(self,mycur):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        mycur.execute("select min(salary) from salaries")
        return mycur.fetchone()

if __name__ == "__main__":
    mdb =connection.connect(host="localhost", user="root", passwd="20102001Sp$",database = "employees")
    mycur=mdb.cursor(buffered=True)

    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary(mycur)
    max_salary = db_helper.get_maximum_salary(mycur)
    print(max_salary)
    print(min_salary)