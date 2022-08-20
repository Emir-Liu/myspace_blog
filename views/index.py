import tornado
import tornado.web
class HelloHandler(tornado.web.RequestHandler):
    def get(self,*kwards):
        print("接受到请求")
        self.write("hello")

class RedirectHandler(tornado.web.RequestHandler):
    def get(self,*kwards):
        self.redirect('/hello')
