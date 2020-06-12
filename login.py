user_s = 'username'
password_s = '******'
attempts = 3

while True:
    if attempts < 0:
        print("You've reached the limits of attempts. Please try again later. ")
        break

    user_f = input('User: ')
    user_f = user_f.lower()
    if len(user_f) > 15 or len(user_f) < 5:
        print('Invalid number of characters! ')
        continue

    password_f = input('Password: ')
    if not password_f.isdigit():
        print('Invalid type of characters! ')
        continue

    if user_f == user_s and password_f == password_s:
        print("Welcome! You're logged in!" )
        break
    else:
        if user_f != user_s or password_f != password_s:
            print('The user or the password are incorrect. Please, try again.')
        print()
        attempts -= 1
        continue
