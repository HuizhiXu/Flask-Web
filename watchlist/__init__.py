

import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABASE_FILE', 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    from watchlist.models import User
    user = User.query.get(int(user_id))
    return user


login_manager.login_view = 'login'
# login_manager.login_message = 'Your custom message'


@app.context_processor
def inject_user():
    from watchlist.models import User
    user = User.query.first()
    return dict(user=user)


from watchlist import views, errors, commands

"""
关于为什么在最后导入：https://discuss.helloflask.com/t/topic/600/3

调用 flask run 启动程序的时候 Flask 会根据给出的 FLASK_APP 环境变量找到对应的程序实例，也就是构造文件里的 app 对象，这时的 app 实例上没有注册任何路由或其他回调函数。

如果这样程序就直接启动，那么就没有任何路由注册到程序实例上，因为没有触发其他模块，比如包含视图函数的 views 模块。而如果在这里导入 views 模块，那么 Python 就会执行 views 模块的顶层代码，这样所有视图函数的装饰器 @app.route 就会被执行，从而把路由注册到 app 实例上，这样启动的程序就包含了这些路由信息。

你可以具体了解一下 Python 的 导入机制，只要导入某个模块，Python 解释器就会执行这个模块的顶层代码。
"""