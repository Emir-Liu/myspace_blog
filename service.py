# 第三方库
import tornado.web
import tornado.ioloop

from views.index import IndexHandler

def service():
    print("启动服务")
    app = tornado.web.Application(
        [
            (r'/hello',IndexHandler)
        ]
    )
    app.listen(6668)
    print("服务启动完成")
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    service()

