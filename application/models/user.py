# coding: utf-8
import datetime
from ._base import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50))
    avatar = db.Column(db.String(200))
    password = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    last_read_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __setattr__(self, name, value):
        # 每当设置password时，自动进行hash
        if name == 'password':
            value = generate_password_hash(value)
        super(User, self).__setattr__(name, value)

    def check_password(self, password):
        """验证密码"""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %s>' % self.name
