import math

import tornado
from sqlalchemy import func
from tornado.escape import json_decode
from tornado_sqlalchemy import SessionMixin

from model import Requests
from base64_coding import dict_to_base64


class AddHandler(SessionMixin, tornado.web.RequestHandler):
    def post(self):
        request_info = json_decode(self.request.body)
        code = dict_to_base64(request_info)
        with self.make_session() as session:
            request_data = session.query(Requests).filter_by(code=code).first()
            if request_data:
                request_data.duplicates = Requests.duplicates + 1
                session.commit()
                self.write({'code': request_data.code, 
                            'info': request_data.info,
                            'duplicates': request_data.duplicates})
            else:
                request_data = Requests(code=code, info=request_info, duplicates=0)
                session.add(request_data)
                session.commit()
                self.write({"code": code,
                            'info': request_data.info,
                            'duplicates': request_data.duplicates })


class GetHandler(SessionMixin, tornado.web.RequestHandler):
    def get(self):
        request_key = self.get_argument('key')
        with self.make_session() as session:
            request_data = session.query(Requests).filter_by(code=request_key).first()
            if request_data:
                self.write({'code': request_data.code, 
                            'info': request_data.info,
                            'duplicates': request_data.duplicates})
            else:
                self.write({"message": "no such request"})


class RemoveHandler(SessionMixin, tornado.web.RequestHandler):
    def delete(self):
        request_key = self.get_argument('key')
        with self.make_session() as session:
            request_data = session.query(Requests).filter_by(code=request_key).first()
            if request_data:
                session.delete(request_data)
                session.commit()
                self.write({"message": "delete request"})
            else:
                self.write({"message": "no such request" })


class UpdateHandler(SessionMixin, tornado.web.RequestHandler):
    def put(self):
        request_key = self.get_argument('key')
        request_info = json_decode(self.request.body)
        code = dict_to_base64(request_info)
        with self.make_session() as session:
            request_data = session.query(Requests).filter_by(code=request_key).first()
            if request_data:
                request_data.duplicates = 0
                request_data.code = code
                request_data.info = request_info
                session.commit()
                self.write({'code': request_data.code, 
                            'info': request_data.info,
                            'duplicates': request_data.duplicates})
            else:
                self.write({"message": "no such request"})


class StatisticHandler(SessionMixin, tornado.web.RequestHandler):
    def get(self):
        with self.make_session() as session:
            query = session.query(func.sum(Requests.duplicates), func.count(Requests.duplicates))
            results = [row for row in session.execute(query)]
            print(results)
            total_sum = results[0][0]
            total_count = results[0][1]
            persent = 0
            # if count equal to 0 than there is no rows in a table
            if total_count != 0:
                persent = math.floor(total_sum/(total_sum+total_count)*100)
            self.write({'persent': persent})