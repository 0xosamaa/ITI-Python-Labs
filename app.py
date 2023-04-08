import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_labs")

cursor = db.cursor()


def home_menu():
    home_menu_input = int(input("0 => Register\n1 => Login\n"))
    return home_menu_input

def login():
    email = input("Enter your email: ")
    while not email:
        email = input("Enter your phone number: ")
    password = input("Enter password: ")
    while not password:
        password = input("Enter password: ")
    sql = "SELECT * FROM users WHERE email = %s and password = %s"
    val = (email, password)
    cursor.execute(sql, val)

    global user
    user = cursor.fetchone()

    if user:
        print(f'\nUser Authenticated: {user[1]} {user[2]}\n')
        logged_menu()

    else:
        print("Incorrect email or password.")


def logged_menu():
    print('Project Details:')

    title = input("Enter title: ")
    while not title:
        title = input("Enter title: ")

    details = input("Enter Details: ")
    while not details:
        details = input("Enter Details: ")
    
    total_target = input("Enter Total Target: ")
    while not total_target:
        total_target = input("Enter Total Target: ")
    


def register():
    first_name = input("Enter first name: ")
    while not first_name:
        first_name = input("Enter first name: ")

    last_name = input("Enter last name: ")
    while not last_name:
        last_name = input("Enter last name: ")

    email = input("Enter your email: ")
    while not email:
        email = input("Enter your phone number: ")

    phone_no = input("Enter your phone number: ")
    while not phone_no:
        phone_no = input("Enter your phone number: ")

    password = input("Enter password: ")
    while not password:
        password = input("Enter password: ")

    confirm_password = input("Confirm password: ")
    while not confirm_password:
        confirm_password = input("Confirm password: ")

    while password != confirm_password:
        password = input("Enter password: ")
        confirm_password = input("Confirm password: ")
    sql = "INSERT INTO users (first_name, last_name, email, password, phone_no) VALUES (%s, %s, %s, %s, %s)"
    val = (first_name, last_name, email, password, phone_no)
    cursor.execute(sql, val)
    return (first_name, last_name, email, password, phone_no,)


while True:
    option = home_menu()
    if option == 0:
        register()
    elif option == 1:
        login()
