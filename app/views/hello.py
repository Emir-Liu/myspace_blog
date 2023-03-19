# 测试页面
import tornado
import tornado.web

from app.handler.util import Logging
class HelloHandler(tornado.web.RequestHandler):
    def get(self,*kwards):
        logger = Logging().getlogger()
        logger.debug('接收到请求')
        self.write("hello")