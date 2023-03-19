# 主页面

import re

# 第三方库
import tornado.web

from app.handler.util import Article,Logging

class IndexHandler(tornado.web.RequestHandler):
    # 用于页面访问
    def get(self,*kwards):
        self.render('./index.html',article_list=self.process())

    # 用于测试
    def post(self,*kwards):
        self.write(str(self.process()))

    # 处理部分
    def process(self):
        logger = Logging().getlogger()
        logger.debug('接收到请求')
        article_list = Article().getallarticle()
        # 下面需要将内部有格式的文本内容转化为无格式的内容
        for article in article_list:
            article['content'] = re.sub('<[^<]+?>','', article['content'])[0:100]
        return article_list
