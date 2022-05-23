import re

pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

email = input('Please enter email: ')

if re.search(pattern, email):
    login = email[0:email.find('@')]
    domain = email[email.find('@') + 1:]
    print(login)
    print(domain)
else:
    print('Invalid email address.')
