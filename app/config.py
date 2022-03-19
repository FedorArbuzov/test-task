import yaml
from tornado_sqlalchemy import SQLAlchemy


config_obj = yaml.load(open('config.yaml'), Loader=yaml.Loader)

db = SQLAlchemy(config_obj['SQLALCHEMY_DATABASE_URI'])
