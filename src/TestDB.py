import MySQLdb


class TestDB:
    def __init__(self):
        db = MySQLdb.connect(host="localhost", port=3306, db="WebStore", user="root", passwd="")
        cursor = db.cursor()
        cursor.execute("select * from t_users")
        results = cursor.fetchall()
        print(results)


if __name__ == '__main__':
    TestDB()
