import json

with open('config.json', 'r') as f:
    config_file = f.read()
    config = json.loads(config_file)


class Config:
    SECRET_KEY = config['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = config['SQLALCHEMY_DATABASE_URI']
