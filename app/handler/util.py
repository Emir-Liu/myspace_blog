import configparser
import logging
import os
import time

# 第三方库
import markdown


# 配置文件相关内容
class ReadConfig():
    # 读取配置文件
    def __init__(self,config_path=None):
        self.BASE_DIRS = os.path.dirname(__file__)
        if config_path == None:
            config_path = 'config.ini'
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    # 获取配置内容
    def get(self,section,key):
        return self.config.get(section,key)


# 日志文件相关内容
class Logging():
    # 类变量
    __instance = None
    logger = None

    def __init__(self):
        # 实例变量
        self.logger = Logging.logger

    # 创建Logging类
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.logger = cls.__instance.createlogger()
        return cls.__instance

    # 未实装
    def __call__(self, *args, **kwargs):
        return Logging.logger

    # 测试日志输出
    def test(self):
        # 记录日志
        self.logger.debug('debug message')
        self.logger.info('info message')
        self.logger.warning('warning message')
        self.logger.error('error message')
        self.logger.critical('critical message')

    # 创建并配置日志
    def createlogger(self):
        stream, stream_level, file, file_level, file_path = self.readloggingconfig()

        # 创建一个名为 example 的 logger
        logger = logging.getLogger('example')
        logger.setLevel(logging.DEBUG)

        if stream == 'True':
            # 创建一个控制台处理器并设置日志级别
            console_handler = logging.StreamHandler()
            console_handler.setLevel(self.translogginglevel(stream_level))

        if file == 'True':
            # 创建一个文件处理器并设置日志级别，将日志写入文件中
            file_handler = logging.FileHandler(file_path)
            file_handler.setLevel(self.translogginglevel(file_level))

        # 设置日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # 添加处理器到 logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        return logger

    # 获取日志对象
    def getlogger(self):
        return self.logger

    # 读取日志相关配置
    def readloggingconfig(self):
        config = ReadConfig()
        stream = config.get('logging','stream')
        stream_level = config.get('logging', 'stream_level')
        file = config.get('logging', 'file')
        file_level = config.get('logging', 'file_level')
        file_path = config.get('logging','file_path')
        return stream,stream_level,file,file_level,file_path

    # 对级别进行转化
    def translogginglevel(self,stringlevel):
        if stringlevel == 'debug':
            return logging.DEBUG
        elif stringlevel == 'info':
            return logging.INFO
        elif stringlevel == 'warning':
            return logging.WARNING
        elif stringlevel == 'error':
            return logging.ERROR
        elif stringlevel == 'critical':
            return logging.CRITICAL
        else:
            return logging.INFO

    # 异常捕获标准化输出
    # 未实装
    def trylogger(self,stringtask,cmd):
        try:
            cmd
            self.logger.info(stringtask+'成功')
        except Exception as e:
            self.logger.warning(stringtask+'失败：'+e)

    # 状态标准化输出
    # 未实装
    def startlogger(self,string):
        pass


# 提供向上的文本信息接口
class Article():
    config = ReadConfig()
    article_file = config.get('data', 'article')
    logger = Logging().getlogger()

    # 判断是否为路径
    def ispath(self,path):
        if os.path.exists(path):
            if os.path.isfile(path):
                return 'file'
            elif os.path.isdir(path):
                return 'dir'
        return False

    # 将文档相对路径，输入标题
    def title2path(self,article_title):
        article_path = os.path.join(Article().article_file,article_title+'.md')
        return article_path

    # 将文档相对路径，输入标题
    def file2path(self,file):
        article_path = os.path.join(Article().article_file,file)
        return article_path

    # 获取文件的时间
    def path2time(self,path):
        # 读取系统数据，获取时间
        create_time = os.path.getctime(path)
        edit_time = os.path.getmtime(path)
        # 将时间进行转换
        create_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(create_time))
        edit_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(edit_time))
        return create_time,edit_time,create_time_str,edit_time_str

    # 将文件转换为meta和html
    def path2html(self,path):
        # 使用markdown解析，获取元数据，文档内容
        # 读取 Markdown 文件内容
        with open(path, 'r',encoding='utf8') as f:
            article_f = f.read()
        # 解析 Markdown 文件
        md = markdown.Markdown(extensions=['meta'])
        html = md.convert(article_f)
        meta = md.Meta
        return meta,html

    # 获取文档的信息
    def getonearticle(self,article_title=None,article_path=None):
        article_info = {
            'title':'',
            'create_time':'',
            'edit_time':'',
            'meta':{
            },
            'content':'',
        }
        if article_path == None:
            # 如果没有路径，将title解析为文件的相对位置
            article_path = self.title2path(article_title)
        # 需要增加path检测，待定
        if self.ispath(article_path) != 'file':
            Article().logger.warning('没有找到对应的文件:{}'.format(article_path))
            return article_info
        if article_title == None:
            # 如果没有标题，通过路径解析标题
            article_title = os.path.basename(article_path)[0:-3]
        # 获取文件信息中的标题
        article_info['title'] = article_title
        # 对文件进行解析
        # 获取时间
        create_time,edit_time,create_time_str,edit_time_str = self.path2time(article_path)
        article_info['create_time'] = create_time_str
        article_info['edit_time'] = edit_time_str
        # 使用markdown解析，获取元数据，文档内容
        # 读取 Markdown 文件内容
        article_meta,article_html = self.path2html(article_path)
        article_info['content'] = article_html
        article_info['meta'] = article_meta
        return article_info

    # 显示所有文档列表
    def getpathlist(self):
        file_list = os.listdir(Article().article_file)
        return file_list

    # 获取所有文档信息
    def getallarticle(self):
        article_list = []
        # 遍历所有的文件
        pathlist = self.getpathlist()
        Article().logger.debug('pathlist:{}'.format(pathlist))
        for path in pathlist:
            article_list.append(self.getonearticle(article_path=self.file2path(path)))
        return article_list

    # 获取所有的tags和category
    def getalltags(self,articlelist=None):
        if articlelist == None:
            articlelist = self.getallarticle()
        tag_set = set()
        for article in articlelist:
            if 'tags' in article['meta']:
                if article['meta']['tags'] != None and article['meta']['tags'] != '':
                    # for tag in article['meta']['tags']:
                    #     tag_set.add(tag)
                    tag_set.update(article['meta']['tags'])
        return tag_set

    def getallcategory(self,articlelist=None):
        if articlelist == None:
            articlelist = self.getallarticle()
        category_set = set()
        for article in articlelist:
            if 'category' in article['meta']:
                if article['meta']['category'] != None and article['meta']['category'] != '':
                    # for cat in article['meta']['category']:
                    #     category_set.add(cat)
                    category_set.update(article['meta']['category'])
        return category_set

    # 过滤文件
    def articlefilter(self,articlelist=None,):
        pass