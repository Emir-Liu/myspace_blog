# 第三方库
import tornado.web

# 本地模块
from views import index

# 应用类，配置路由
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/hello',index.HelloHandler),# 测试连接
            (r'/helloworld',index.RedirectHandler) # 重定向连接测试
        ]
        super(Application,self).__init__(handlers)

