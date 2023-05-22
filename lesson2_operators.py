user_login = "adam"
user_pass = "1234"

login = input('Login: ')
password = input('Password: ')

if login == user_login and password == user_pass:
    print("Secret")
else:
    print("Locked")

crit1 = "red"
crit2 = "lock"

color = input("Color: ")
feature = input("Feature: ")

if color == crit1 or feature == crit2:
    print("Ok")
else:
    print("Хрен")