import mysql.connector
import time

# Master connection for writing
master_conn = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
    database="testdb",
    port=3306
)

# Slave connection for reading
slave_conn = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
    database="testdb",
    port=3307,
    use_pure=True,
)


def create_table():
    cursor = master_conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INT AUTO_INCREMENT PRIMARY KEY, data VARCHAR(255));")
    master_conn.commit()
    cursor.close()


def write_to_master():
    cursor = master_conn.cursor()
    cursor.execute("INSERT INTO test_table (data) VALUES ('This is a test');")
    cursor.execute("INSERT INTO test_table (data) VALUES ('Another test entry');")
    master_conn.commit()
    cursor.close()


def read_from_slave():
    cursor = slave_conn.cursor()
    cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
    cursor.execute("SELECT * FROM test_table;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


def update_master():
    cursor = master_conn.cursor()
    cursor.execute("UPDATE test_table SET data = 'Updated test entry' WHERE data = 'Another test entry';")
    master_conn.commit()
    cursor.close()


def delete_from_master():
    cursor = master_conn.cursor()
    cursor.execute("DELETE FROM test_table WHERE data = 'This is a test';")
    master_conn.commit()
    cursor.close()


def drop_table():
    cursor = master_conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS test_table;")
    master_conn.commit()
    cursor.close()


if __name__ == "__main__":

    print("Table creating ..")
    create_table()  # Ensure table exists
    print("Table creation Done")

    print("Start writing to master")
    write_to_master()  # Create
    print("End writing to master")
    time.sleep(1)
    print("\nRead from slave :")
    read_from_slave()  # Read

    print("Update master :")
    update_master()  # Update
    time.sleep(1)
    print("\nAfter Update Operation:")
    read_from_slave()  # Read

    print("Delete master :")
    delete_from_master()  # Delete
    time.sleep(1)
    print("\nAfter Delete Operation:")
    read_from_slave()  # Read

    print("Dropping table ...")
    drop_table()  # Drop table

    print("Closing connection ...")
    master_conn.close()
    slave_conn.close()
