def login(_id):
    members = ['egoing', 'jeongjin', 'leezche']
    for member in members:
        if member == _id:
            return True
    return False
