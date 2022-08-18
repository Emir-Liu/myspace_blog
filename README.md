# 0.概述
通过python的tornado模块构造一个博客

# 1.步骤

## 1.1 环境
```
conda create --prefix=/filespace/env 
#通过conda指定特定位置作为环境
conda env list # 显示环境列表
conda activate /filespace/env 
#激活特定的环境
```

## 1.2 git管理

```
git ini #创建了.git文件
git status #查看当前项目的文件状态
git add --all # 对所有文件放入暂存区域
git commit -m "xxx" #将暂存区的内容推送到仓库中
```
由于密码认证被取消了需要通过ssh连接获取密钥进行长久的认证
```
ssh-keygen -t rsa -C "xemailx"
ssh -T git@github.com
```

### 1.3 取消对一些文件的跟踪
.gitignore
```
/env/
```


## 1.3 项目框架
```
tornado-boilerplate/
    handlers/   # 逻辑,控制器
    env/        # python环境
    config/     # 配置文件
    log/        # 日志文件
    templates/  # 模板文件
    views/      # 视图文件
    static/     # 静态文件
        css/
        images/
    requirements.txt  # 环境依赖
    server.py  # 启动文件
```
