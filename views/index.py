import tornado
import tornado.web
class IndexHandler(tornado.web.RequestHandler):
    def get(self,*kwards):
        print("接受到请求")
        self.write("hello")

