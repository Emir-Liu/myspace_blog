# 第三方库
import requests

# 测试对象
from handler.util import Logging,Markdown

# 测试类
class Test():
    # 对页面连接进行测试
    def test_connection(self):
        url = 'localhost'
        ans = requests.get('http://localhost:9090/hello')
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

    def test_all(self):
        pass

if __name__ == '__main__':
    # Test().test_connection()
    # Test().test_logging()
    Test().test_markdown()
