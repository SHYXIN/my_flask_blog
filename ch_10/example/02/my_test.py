# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80))

# # 创建所有表
# with app.app_context():
#     ddl = db.get_ddl(db.metadata)
#     print(ddl)
#     db.create_all()


# from sqlalchemy import create_engine

# # 创建 Engine 对象
# engine = create_engine("sqlite:///example.db")

# # 创建 Item 表
# db.create_all(engine)

# # 查看 DDL 语句
# results = db.session.execute("SELECT sql FROM sqlite_master WHERE name = 'item'")

# # 打印 DDL 语句
# for result in results:
#     print(result[0])

