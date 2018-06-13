from flask_script import Manager
from app import app
manager = Manager(app)


@manager.command
def runserver():
    print('开启服务器')
    



manager.add_command('db', DBManager)


if __name__ == '__main__':
    manager.run()