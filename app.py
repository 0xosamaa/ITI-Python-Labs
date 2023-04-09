import mysql.connector
from getpass import getpass


def login():
    print("\n*** Login ***\n")

    email = input("Email: ")
    while not email:
        email = input("Phone number: ")
    password = getpass("Password: ")
    while not password:
        password = getpass("Password: ")
    sql = "SELECT * FROM users WHERE email = %s and password = %s;"
    val = (email, password)
    cursor.execute(sql, val)

    global user
    user = cursor.fetchone()

    if user:
        print(f'\nUser Authenticated: {user[1]} {user[2]}\n')
        while user:
            option = logged_in_menu()
            if option == 0:
                add_project()
            elif option == 1:
                show_projects()
            elif option == 2:
                keyword = input("Search: ")
                search_projects(keyword)
            elif option == 3:
                id = input("Project id: ")
                edit_project(id)
            elif option == 4:
                id = input("Project id: ")
                delete_project(id)
            elif option == 5:
                logout()
            input("\nPress any button to go back...\n")

    else:
        print("Incorrect email or password.")


def register():
    print("\n*** Register ***\n")

    first_name = input("First name: ")
    while not first_name:
        first_name = input("First name: ")

    last_name = input("Last name: ")
    while not last_name:
        last_name = input("Last name: ")

    email = input("Email: ")
    while not email:
        email = input("Phone number: ")

    phone_no = input("Phone number: ")
    while not phone_no:
        phone_no = input("Phone number: ")

    password = getpass()
    while not password:
        password = getpass()

    confirm_password = getpass("Confirm Password: ")
    while not confirm_password:
        confirm_password = getpass("Confirm Password: ")

    while password != confirm_password:
        password = getpass()
        confirm_password = getpass("Confirm Password: ")
    sql = "INSERT INTO users (first_name, last_name, email, password, phone_no) VALUES (%s, %s, %s, %s, %s);"
    val = (first_name, last_name, email, password, phone_no)
    cursor.execute(sql, val)
    return (first_name, last_name, email, password, phone_no)


def add_project():
    print('*** Add Project ***\n')

    title = input("Title: ")
    while not title:
        title = input("Title: ")

    details = input("Details: ")
    while not details:
        details = input("Details: ")

    total_target = input("Total Target: ")
    while not total_target:
        total_target = input("Total Target: ")

    end_date = input("End Date: ")
    while not end_date:
        end_date = input("End Date: ")

    sql = "INSERT INTO projects (user_id, title, details, total_target, end_date) VALUES (%s, %s, %s, %s, %s);"
    val = (user[0], title, details, total_target, end_date)
    cursor.execute(sql, val)
    print("*** Project Added Successfully ***")
    return (user[0], title, details, total_target, end_date)


def show_projects():
    print("\n*** Show Projects ***\n")
    sql = "SELECT * FROM projects WHERE user_id = %s;"
    val = (user[0],)
    cursor.execute(sql, val)

    results = cursor.fetchall()

    for x in results:
        print(
            f"id: {x[0]}, user_id: {x[1]}, title: {x[2]}, details: {x[3]}, total_target: {x[4]}, start_date: {x[5]}, end_date: {x[6]}")


def search_projects(keyword):
    print("\n*** Search Projects ***\n")
    sql = f"SELECT * FROM projects WHERE user_id = {user[0]} AND (title LIKE '%{keyword}%' OR details LIKE '%{keyword}%' OR start_date LIKE '%{keyword}%' OR end_date LIKE '%{keyword}%');"
    cursor.execute(sql)

    results = cursor.fetchall()

    if not results:
        print("No projects found.")
        return

    print("\n*** Search Results ***\n")
    for x in results:
        print(
            f"id: {x[0]}, user_id: {x[1]}, title: {x[2]}, details: {x[3]}, total_target: {x[4]}, start_date: {x[5]}, end_date: {x[6]}")


def edit_project(id):
    print("\n*** Edit Project ***\n")
    sql = "SELECT * FROM projects WHERE user_id = %s AND id = %s;"
    val = (user[0], id)
    cursor.execute(sql, val)

    result = cursor.fetchone()
    if not result:
        print("No projects found with the given id.")
        return

    print(
        f"id: {result[0]}, user_id: {result[1]}, title: {result[2]}, details: {result[3]}, total_target: {result[4]}, start_date: {result[5]}, end_date: {result[6]}")

    print("\n*** Edit Project Details ***\n")

    title = input("Title: ")
    if not title:
        title = {result[2]}

    details = input("Details: ")
    if not details:
        details = {result[3]}

    total_target = input("Total Target: ")
    if not total_target:
        total_target = {result[4]}

    end_date = input("End Date: ")
    if not end_date:
        end_date = {result[6]}

    sql = "UPDATE projects SET title = %s, details = %s, total_target = %s, end_date = %s WHERE id = %s AND user_id = %s;"
    val = (title, details, total_target, end_date, id, user[0])
    cursor.execute(sql, val)

    print("\n*** Project Updated Successfully ***\n")

    print("\n*** Updated Project ***\n")
    sql = "SELECT * FROM projects WHERE user_id = %s AND id = %s;"
    val = (user[0], id)
    cursor.execute(sql, val)

    result = cursor.fetchone()

    print(
        f"id: {result[0]}, user_id: {result[1]}, title: {result[2]}, details: {result[3]}, total_target: {result[4]}, start_date: {result[5]}, end_date: {result[6]}")


def delete_project(id):
    sql = "SELECT * FROM projects WHERE user_id = %s and id = %s;"
    val = (user[0], id)
    cursor.execute(sql, val)

    print("\n*** Delete Project ***\n")

    result = cursor.fetchone()
    if not result:
        print("No projects found with then given id.")
        return

    print(f"id: {result[0]}, user_id: {result[1]}, title: {result[2]}, details: {result[3]}, total_target: {result[4]}, start_date: {result[5]}, end_date: {result[6]}")

    confirm_delete = input(
        "\nAre you sure you want to delete this project?[Y/n]\n")

    if confirm_delete == "Y" or confirm_delete == "y":
        sql = "DELETE FROM projects WHERE user_id = %s and id = %s;"
        val = (user[0], id)
        cursor.execute(sql, val)
        print("Project deleted successfully")
    else:
        return


def logout():
    global user
    user = None
    print("Logged out.")


def home_menu():
    home_menu_input = input("0 => Register\n1 => Login\n2 => Exit\n")
    return home_menu_input


def logged_in_menu():
    logged_in_input = int(input(
        "0 => Add Project\n1 => Show Projects\n2 => Search Projects\n3 => Edit Project\n4 => Delete Project\n5 => Logout\n"))
    return logged_in_input


def start():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_labs")

    global cursor
    global user

    cursor = db.cursor()
    user = None

    while not user:
        option = home_menu()
        if option == "0":
            register()
        elif option == "1":
            login()
        elif option == "2":
            exit()
        else:
            continue


if __name__ == "__main__":
    start()
