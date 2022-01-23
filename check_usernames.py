current_users = ['joe', 'bob', 'admin', 'becky', 'JILL']
new_users = ['jackie', 'brianna', 'jill', 'miranda', 'nathan', 'bob']

for user in range(len(current_users)):
    current_users[user] = current_users[user].lower()


for new_user in new_users:
    if new_user in current_users:
        print(f'Username {new_user.title()} is taken.')
    else:
        print(f'{new_user.title()} is available.')