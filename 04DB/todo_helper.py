import sqlite3

db= "my_todos.db"

# making connection
conn = sqlite3.connect(db)

# creating a cursor to execute all commands
cur = conn.cursor()


# TODO: Create a Table
def create_table():
    # create table if not exists table_name (id integer primary key autoincrement ,taskname text)
    sql = 'CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT ,taskname TEXT) '
    cur.execute(sql)
    cur.execute("pragma table_info('todos')");

# TODO: Enter a todo

def data_entry(todo):
    # insert into table_name (column_name) values (column_values)
    cur.execute("INSERT INTO todos (taskname) values(?)",[todo])
    print("todo added successfully")
    print(cur.execute("pragma table_info('todos')"));
    conn.commit()

# TODO: Read todos
def read_todos():
    #select * from table_name
    # select column_name from table_name
    cur.execute('SELECT taskname from todos')
    for row in cur.fetchall():
        # print(f"{row[0]} ----> {row[1]}")
        print(row)

# TODO: Update a todo
def update_todo(ind,updated_todo):
    # update table_name set column_name=new_value where ID=index

    cur.execute("UPDATE todos SET taskname = (?) where id = (?)",[updated_todo,ind])
    print("todo updated successfully")
    conn.commit()
# TODO: Delete a todo

def delete_todo(ind):
    # delete from table_name where id = index
    cur.execute("DELETE FROM todos WHERE id = ind")
    print("Todo deleted successfully")
    conn.commit()


# TODO: close the connection
def close_connection():
    cur.close()
    conn.close()