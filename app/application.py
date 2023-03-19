# 进行路由的配置
import os
# 第三方库
import tornado.web

# 本地模块
from app.views import hello,index,article,blog
from app.handler.util import ReadConfig

# 应用类，配置路由
class Application(tornado.web.Application):
    def __init__(self):
        config = ReadConfig()
        handlers = [
            (config.get('map','test'), hello.HelloHandler), # 测试连接
            (config.get('map', 'index'), index.IndexHandler),   # 主页
            (config.get('map', 'article'), article.ArticleHandler), # 文本页
            (config.get('map', 'blog'), blog.BlogHandler),  # blog页
        ]

        settings = {
            "debug": config.get('tornado','debug'),
            "static_path": os.path.join(os.getcwd(),config.get('tornado','static')),
            "template_path": os.path.join(os.getcwd(),config.get('tornado','templates')),
            "static_url_prefix": "/static/",
        }
        print('settings:{}'.format(settings))
        super(Application,self).__init__(handlers,**settings)