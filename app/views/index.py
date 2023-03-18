
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self,*kwards):
        self.render('./index.html')