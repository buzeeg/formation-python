import MySQLdb


class DatabaseManager:

    def __init__(self):
        self.connection = MySQLdb.connect(host="localhost", port=3306, db="WebStore", user="root", passwd="")

    def getTableData(self, tableName):
        cursor = self.connection.cursor()

        indexColumnName = 0

        cursor.execute("describe " + tableName)
        headerNames = []
        for columnData in cursor.fetchall():
            headerNames.append(columnData[indexColumnName])

        cursor.execute("select * from " + tableName)
        data = cursor.fetchall()

        return headerNames, data

    def getAllTableNames(self):
        cursor = self.connection.cursor()
        cursor.execute('show tables')
        allTableNames = []
        for tableMetaData in cursor.fetchall():
            allTableNames.append(tableMetaData[0])

        return allTableNames

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    database = DatabaseManager()
    print(database.getAllTableNames())
    print(database.getTableData("T_Users"))
    database.close()
