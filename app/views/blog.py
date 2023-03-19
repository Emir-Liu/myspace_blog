# 文章页面
import json
import tornado.web
import tornado.escape
from app.handler.util import Logging,Article

class BlogHandler(tornado.web.RequestHandler):
    # 为了能够在浏览器上直接显示结果，增加get方法
    def get(self,*kwards):
        data = self.request.arguments
        article_name = data['article_name'][0].decode()
        logger = Logging().getlogger()
        logger.debug('接收到参数:{}'.format(data))
        article_info = Article().getonearticle(article_name=article_name)
        self.render('./article.html',article=article_info)

    def post(self,*kwards):
        data = self.request.body
        logger = Logging().getlogger()
        logger.debug('接收到参数:{}'.format(data))
        article_info = Article().getonearticle(article_name=data['article_name'])
        self.write(article_info)