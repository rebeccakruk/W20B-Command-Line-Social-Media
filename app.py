import mariadb
from dbhelpers import connect_db, execute_statement, close_connection

def login():
    print("Welcome to the brag page")
    alias = input("Please enter your alias: ")
    password = input("Please key in your password: ")
    cursor = connect_db()
    if cursor == None:
        print("Something went wrong with the connection. Please try again later")
    else:
        result = execute_statement(cursor, "CALL user_creds(?,?)", [alias, password])
    if len(result) != 0:
        for id in result:
            print("Hi {}!".format(id[0]))
            user_id = id[2]
            return options(user_id)
    else:
        print("No such alias/password combination. Please enter the correct alias and password")

def options(user_id):
    while True:
        print("Please make a selection: \
            \n1. Enter a new exploit\
            \n2. View your exploits\
            \n3. See everyone else's exploits for inspiration\
            \n4. Quit")
        selection = input("You picked: ")
        if selection == "1":
            new_exploit(user_id)
        elif selection == "2":
            mine(user_id)
        elif selection == "3":
            view(user_id)
        elif selection == "4":
            print("Thanks for visiting, goodbye!")
            break
        else:
            print("Please try again")


def new_exploit(user_id): 
    content = input("New exploit: ")
    cursor = connect_db()
    cursor.execute("CALL new_exploit(?,?)", [content, user_id])
    print("New exploit successfully recorded")

def mine(user_id : int):
    input = user_id
    cursor = connect_db()
    cursor.execute("CALL view_exploits(?)", [input])
    results = cursor.fetchall()
    print("Your exploits: ", results)

def view(user_id):
    input = user_id
    cursor = connect_db()
    cursor.execute("CALL others_exploits(?)", [input])
    results = cursor.fetchall()
    print("Others' exploits: ", results)



login()