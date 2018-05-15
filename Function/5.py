input_id = input("Please input your ID.\n")


def login(_id):
    members = ['egoing', 'jeongjin', 'leezche']
    for member in members:
        if member == _id:
            return True
    return False


if login(input_id):
    print('Hello, ' + input_id)
else:
    print('Who are you?')
