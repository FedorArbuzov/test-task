import tornado.web
import tornado.ioloop

from config import db
from handlers import AddHandler, GetHandler, RemoveHandler, UpdateHandler, StatisticHandler


def make_app():
    return tornado.web.Application([
        (r"/api/add", AddHandler),
        (r"/api/get", GetHandler),
        (r"/api/remove", RemoveHandler),
        (r"/api/update", UpdateHandler),
        (r"/api/statistic", StatisticHandler),
    ],
    db=db
)

if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
