import os

print('The applied environment variable value is:')
print(os.environ.get('MY_VAR3'))

if os.environ.get('MY_VAR3') == 'TEST':
    print('success')
else:
    print('failure')
