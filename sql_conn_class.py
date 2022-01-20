import pyodbc


class sql():
    def __init__(self):

        return self.conniction()


    def conniction(self):
        global conn
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-AUJHRJE\MSSQLSERVER01;'
                              'Database=test;'
                              'Trusted_Connection=yes;')

    def insert(self):

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM test.dbo.login')
        cursor.execute('''INSERT INTO test.dbo.login (username, password)
                            VALUES
                            ('Bob','55'),
                            ('Jenny','66'),
                            ('jafar','96')''')


        conn.commit()

    def select(self,selectstatment):
        cursor = conn.cursor()
        cursor.execute(selectstatment)



        for row in cursor:

            print(row)


        conn.commit()

    def isExist(self,selectstatment):
        cursor = conn.cursor()
        cursor.execute(selectstatment)

        if cursor.fetchone():
            return True
        else:
            return False



    def delete(self):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM test.dbo.login')
        cursor.execute('''
                        DELETE FROM login 
                        WHERE username in ('Bob','Jenny') and 
                        password in ('55','66')
                       ''')

        conn.commit()








