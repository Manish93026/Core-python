class LoginException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

Login_id = 'Admin'
Login_password = 'Admin'

try:
    if Login_id == 'Admin'and Login_password == 'Admin':
        print('login success')

    else:
        raise LoginException('login failed')

except LoginException as e:
    print('login Exception',e)
