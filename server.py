# 第三方库
import tornado.web
import tornado.ioloop
import os

# 本地库
from handler.util import ReadConfig
from application import Application

class Service():
    def __init__(self):
        pass

    def run(self):
        pass

def service():
    print("启动服务")

    app = Application()
    config = ReadConfig()
    config.BASE_DIR = os.path.dirname(__file__)
    print("base_dir:{}".format(config.BASE_DIR))
    port = config.get('url','port')
    app.listen(port)
    print("服务启动完成")
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    service()

