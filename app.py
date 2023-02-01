import mariadb
from dbhelpers import connect_db, execute_statement, close_connection

def options():
    print("Please make a selection: ")
# If a user with a specific alias and password exist, the length of the list sent back from the select procedure will be 1, otherwise will be 0

hackers = []
print("Welcome to the brag page")
alias = input("Please enter your alias: ")
password = input("Please key in your password: ")
cursor = connect_db()
# if cursor == None:
#     print("Something went wrong with the connection. Please try again later")
# else:
hackers = execute_statement(cursor, "CALL user_creds(?,?)", [alias, password])
if (alias, password) in hackers:
    print("Hi {}!".format(alias))
    options()
else:
    print("No such alias/password combination. Please enter the correct alias and password")
