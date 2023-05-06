import logging
import os

# 第三方库
import tornado.web
import tornado.ioloop

# 本地库
from app.handler.util import ReadConfig,Logging
from app.application import Application


def service():
    logger.info("开始启动服务")
    app = Application()
    config = ReadConfig()
    config.BASE_DIR = os.path.dirname(__file__)
    logger.debug("base_dir:{}".format(config.BASE_DIR))
    port = config.get('url','port')
    # 绑定端口
    Logging().trylogger('绑定服务端口',app.listen(port))
    tornado.ioloop.IOLoop.instance().start()
    logger.info("服务启动完成")



logger = Logging().getlogger()
if __name__ == '__main__':
    service()

