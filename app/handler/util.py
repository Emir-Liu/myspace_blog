import configparser
import logging
import os

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


# 文件管理相关
class Fileoperation():

    def __init__(self):
        # 对象变量
        self.path = self.pwd()

    # 将文件名转化为对应的文件绝对路径
    # 找到对应的文件夹，并和文件名进行拼接
    def transfile(self,file_name):
        config = ReadConfig()
        file_file = config.get('data','article')
        file_path = os.path.join(file_file,file_name)
        return file_path


    # 显示当前路径下包含哪些文件，返回文件列表
    def ls(self,current_path=None):
        if current_path == None:
            current_path = os.getcwd()
        file_list = os.listdir(current_path)
        return file_list

    # 显示当前的绝对路径
    def pwd(self):
        return os.getcwd()

    # 将当前路径和路径中包含的文件进行拼接,得到绝对路径文件列表
    def pathfile(self,path,file_list):
        return []

    # 进入下一级,返回当前绝对路径
    def cd(self,file=None):
        self.path = os.path.join(self.path,file)
        return

    # 判断是否为路径
    def ispath(self,path):
        if os.path.exists(path):
            if os.path.isfile(path):
                return 'file'
            elif os.path.isdir(path):
                return 'dir'
        return False


# markdown文本解析相关内容
# 读取一篇文档的内容
# 读取所有文档的内容
class Markdown():
    def __init__(self):
        pass

    # 开始解析文档内容
    def gethtml(self,path=None):
        # 读取 Markdown 文件内容
        with open(path, 'r',encoding='utf8') as f:
            md_text = f.read()
        # 解析 Markdown 文件
        html = markdown.markdown(md_text)
        # 输出 HTML 结果
        return html
