from config import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSON


class Requests(db.Model):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, nullable=False)
    info = Column(JSON)
    duplicates = Column(Integer)