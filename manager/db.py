from flask_script import Manager

DBmanager = Manager()

@DBManager.command
def init():
    print('数据库初始化')
    
@DBManager.command
def migrate():
    print('数据库迁移成功')