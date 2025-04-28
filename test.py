import os

print('The applied environment variable valueje :')
print(os.environ.get('MY_VAR3'))
print('The applied environment variable value is:')
print(os.environ.get('ENV_FROM_FORK'))


if os.environ.get('MY_VAR3') == 'TEST':
    print('success')
else:
    print('failure')
