from flask import Flask
from config import DevConfig

app = Flask(__name__)

#Get the config from object of DevConfig
app.config.from_object(DevConfig)

#指定URL='/'的路由规则
#当访问HTTP://server_ip/GET时，call home()
@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

if __name__=='__main__':
    #Entry the application
    app.run