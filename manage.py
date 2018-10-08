#import Flask Script object
from flask_script import Manager,Server
import main

#Init manager object via app object
manager = Manager(main.app)

#Create a new command:server
#This command will be run the Flask development_env server
manager.add_command("server",Server())

@manager.shell
def make_shell_context():
    """Create a python CLI.
    return:Default import object
    type:'Dict'"""
    #确保有导入Flask app object，否则启动的CLI上下文中仍然没有app对象
    return dict(app=main.app)

if __name__=='__main__':
    manager.run()