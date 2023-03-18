import json
import tornado.web
import tornado.escape
from app.handler.util import Logging,Markdown,Fileoperation

class ArticleHandler(tornado.web.RequestHandler):
    # 为了能够在浏览器上直接显示结果，增加get方法
    def get(self,*kwards):
        data = self.request.arguments
        article_name = data['article_name'][0].decode()+'.md'
        logger = Logging().getlogger()
        logger.debug('接收到参数:{}'.format(data))
        # 下面根据文件名寻找对应的文件
        article_file = Fileoperation().transfile(article_name)

        # 下面对文档进行转化
        article = Markdown().gethtml(article_file).encode('utf8')
        self.render('./article.html',article=article)

    def post(self,*kwards):
        logger = Logging().getlogger()
        data = json.loads(self.request.body)
        logger.info('接收到参数:{}'.format(data))
        self.render('./article.html',article_name=data['article_name'])