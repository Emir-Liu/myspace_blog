import unittest
# 第三方库
import requests

# 测试对象
from app.handler.util import Logging,Markdown,ReadConfig

config = ReadConfig()

# 测试类
class Test():
    # 对页面连接进行测试
    def test_connection(self):
        ans = requests.get('http://localhost:'+config.get('url','port')+config.get('map','test'))
        print(ans.content)
        return 0

    # 对日志进行测试
    def test_logging(self):
        logger = Logging().getlogger()
        logger.debug('debug test')
        logger.info('info test')
        logger.warning('warning test')
        logger.error('error test')
        logger.critical('critical test')

    # 对markdown解析进行测试
    def test_markdown(self):
        html = Markdown().gethtml('./blog/article/README.md')
        print(html)

    # 对网页显示markdown进行测试
    def test_article(self):
        article_name='README.md'
        json = {
            'article_name':'README'
        }
        ans = requests.post(url='http://localhost:'+config.get('url','port')+config.get('map','article'),
                            data=json)
        print('ans:{}'.format(ans))
        return ans
    def test_all(self):
        pass

if __name__ == '__main__':
    # Test().test_connection()
    Test().test_article()
    # Test().test_logging()
    # Test().test_markdown()
