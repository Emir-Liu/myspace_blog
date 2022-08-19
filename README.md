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
pip install xxx -i https://pypi.tuna.tsinghua.edu.cn/simple
# 下载模块慢就使用镜像源
```

## 1.2 git管理

```
git ini #创建了.git文件
git status #查看当前项目的文件状态
git add --all # 对所有文件放入暂存区域
git commit -m "xxx" #将暂存区的内容推送到仓库中

git remote add origin https://github.com/Emir-Liu/myspace_blog.git
git branch -M main
git push -u origin main
```

Git生成密钥后将密钥配置到Github上，但是每次提交代码的时候还是要输入用户名和密码。操作步骤很是麻烦。

问题引入：
因为用的是https而不是ssh，更新origin为ssh格式即可。
https的格式为：https://github.com/用户名/仓库名.git
ssh的格式为：git@github.com:用户名/仓库名.git
解决方法：
git remote remove origin
git remote add origin git@github.com:用户名/仓库名.git


由于密码认证被取消了需要通过ssh连接获取密钥进行长久的认证
```
ssh-keygen -t rsa -C "xemailx"
ssh -T git@github.com
```
对代码打标签
```
git tag -a 0.0.0.1 -m "项目格式测试"
git push origin mastar
git push origin --tags
# 将标签提交到远程服务器

git status
# 显示文件状态
git los
# 显示commit记录
```

### 1.2.1 取消对一些文件的跟踪
.gitignore
```
/env/
```

### 1.2.2 tag与branch区别
tag:当发布一个稳定的版本，需要记录的时候使用tag
tag指向的是一次commit的id

branch:是一个分支
多人开发，完成后merge到master


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

## 1.4 makefile管理工程

