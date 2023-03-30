import sqlite3

def hw(db_name):

    products = None
    try:
        products = sqlite3.connect(db_name)

    except sqlite3.Error as not_work:
        print(not_work)
    return products


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as not_work:
        print(not_work)


def create_products(connection, products):
    try:
        sql = '''INSERT INTO products (product_title, price , quantity)
        VALUES (?, ?, ?)'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as not_work:
        print(not_work)


def select_products(connection):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as not_work:
        print(not_work)


def update_products(connection, id):
    try:
        sql = '''UPDATE products SET quantity = ?, price = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, id)
        connection.commit()
    except sqlite3.Error as not_work:
        print(not_work)


def delete_products(connection, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as not_work:
        print(not_work)


data_base_name = 'Nazira_28_1.db'

sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0.)
'''

connection_to_db = hw(data_base_name)
if connection_to_db is not None:
    print('Every things ok!')
    # create_products(connection_to_db, ('Milk', 25, 45))
    # create_products(connection_to_db, ('Apple', 46.5, 100))
    # create_products(connection_to_db, ('Snickers', 65, 59))
    # create_products(connection_to_db, ('Yogurt', 35.75, 30))
    # create_products(connection_to_db, ('Rice', 128, 72))
    # create_products(connection_to_db, ('Spaghetti', 47, 47))
    # create_products(connection_to_db, ('Tea', 82, 45))
    # create_products(connection_to_db, ('Coffee', 300, 35))
    # create_products(connection_to_db, ('Sunflower Oil', 148, 65))
    # create_products(connection_to_db, ('Shampoo', 230, 96))
    # create_products(connection_to_db, ('Bread', 34.5, 45))
    # create_products(connection_to_db, ('Soup', 63.6, 15))
    # create_products(connection_to_db, ('Orange Juice', 86, 57))
    # create_products(connection_to_db, ('Ice creme', 45, 105))
    # create_products(connection_to_db, ('Solt', 15, 30))

    select_products(connection_to_db)
    update_products(connection_to_db, (45 , 100,))
    connection_to_db.close()
    print('DONE')


