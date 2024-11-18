import mysql.connector
import time

# Connection to ProxySQL
conn = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
    database="testdb",
    port=6033
)


def create_table():
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INT AUTO_INCREMENT PRIMARY KEY, data VARCHAR(255));")
    conn.commit()
    cursor.close()


def write_to_master():
    cursor = conn.cursor()
    cursor.execute("INSERT INTO test_table (data) VALUES ('This is a test');")
    cursor.execute("INSERT INTO test_table (data) VALUES ('Another test entry');")
    conn.commit()
    cursor.close()


def read_from_slave():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_table;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


def update_master():
    cursor = conn.cursor()
    cursor.execute("UPDATE test_table SET data = 'Updated test entry' WHERE data = 'Another test entry';")
    conn.commit()
    cursor.close()


def delete_from_master():
    cursor = conn.cursor()
    cursor.execute("DELETE FROM test_table WHERE data = 'This is a test';")
    conn.commit()
    cursor.close()


def drop_table():
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS test_table;")
    conn.commit()
    cursor.close()


if __name__ == "__main__":
    print("Table creating ..")
    create_table()
    print("Table creation Done")

    print("Start writing to master")
    write_to_master()
    print("End writing to master")
    time.sleep(1)
    print("\nRead from slave :")
    read_from_slave()

    print("Update master :")
    update_master()
    time.sleep(1)
    print("\nAfter Update Operation:")
    read_from_slave()

    print("Delete master :")
    delete_from_master()
    time.sleep(1)
    print("\nAfter Delete Operation:")
    read_from_slave()

    print("Dropping table ...")
    drop_table()

    print("Closing connection ...")
    conn.close()
