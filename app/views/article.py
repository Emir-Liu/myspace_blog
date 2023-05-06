# 文章页面
import json
import tornado.web
from app.handler.util import Logging,Article

class ArticleHandler(tornado.web.RequestHandler):

    # 用于页面访问
    def get(self,*kwards):
        data = self.request.arguments
        article_name = data['title'][0].decode()
        logger = Logging().getlogger()
        logger.debug('接收到参数:{}'.format(data))
        article_info = Article().getonearticle(article_title=article_name)
        self.render('./article.html',article_info=article_info)

    # 用于测试
    def post(self,*kwards):
        data = json.loads(self.request.body)
        logger = Logging().getlogger()
        logger.debug('接收到参数:{}'.format(data))
        article_info = Article().getonearticle(article_title=data['title'])
        self.write(article_info)
