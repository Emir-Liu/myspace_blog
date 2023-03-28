# 0.概述
该项目主要构建基于python的个人博客。
这个项目主要包含下面的几个功能:
1.markdown解析
2.页面设置
2.1.主页面
2.1.1.文章时间，标签，部分显示
3.标签分类
4.搜索

# 1.部分功能实现
## 1.1 tornado显示主要页面

## 1.2 markdown文章解析

# 2.项目管理
## 2.1 git

## 2.2 github的project

# 3.tips
获取项目中的环境要求:

## 发现网站中如果有部分的内容再不同的网页中会重复出现，可以使用下面的方法来避免重复写代码
在Tornado中实现类似顶部导航栏的功能，可以通过以下步骤来避免直接复制代码：

1.使用Tornado的模板引擎来渲染HTML页面，而不是直接在HTML页面中嵌入静态的HTML代码。
2.在Tornado的模板引擎中定义一个包含顶部导航栏的模板块（template block），比如说命名为“navbar”。
3.在每个需要包含顶部导航栏的HTML页面中，通过模板继承（template inheritance）的方式引用该模板块。具体来说，可以在HTML页面的<head>标签中使用{% extends "base.html" %}语句，其中“base.html”是包含顶部导航栏的模板文件名。然后在HTML页面中定义{% block navbar %}{% end %}语句，以覆盖掉模板文件中的该模板块。
4.在包含顶部导航栏的模板文件中，可以使用Tornado的模板继承语法{% include "navbar.html" %}来引入一个单独的HTML文件作为导航栏。
通过使用Tornado的模板引擎和模板继承功能，可以将重复的HTML代码抽象成一个模板块，从而避免直接复制代码。

其中方法3的具体实现方法为:
在Tornado中，可以使用模板继承来实现代码复用和分离。模板继承允许您定义一个基础模板，并在子模板中使用{% extends %}指令扩展它。
使用{% include %}指令可以将一个单独的HTML文件引入到模板中。

假设我们有一个名为navbar.html的导航栏模板，我们想要在多个页面中使用它。
首先，在基础模板（例如base.html）中，我们使用{% block %}指令定义一个名为navbar的块：

```bash
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Default Title{% endblock %}</title>
    {% block css %}{% endblock %}
</head>
<body>
    {% include "navbar.html" %}
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    {% block js %}{% endblock %}
</body>
</html>
```
在上面的代码中，我们使用{% include "navbar.html" %}指令来引入navbar.html文件，其中的内容会插入到navbar块中。

接下来，我们在子模板中使用{% extends %}指令扩展基础模板，并在子模板中重写navbar块以定义自己的导航栏：

```bash
{% extends "base.html" %}

{% block navbar %}
    <nav>
        <!-- 自定义导航栏代码 -->
    </nav>
{% endblock %}

{% block content %}
    <!-- 子模板内容 -->
{% endblock %}
```
在上面的代码中，我们重写了navbar块以定义自己的导航栏。在子模板中，我们可以使用{% block %}指令重写任意数量的块，以便覆盖基础模板中定义的任何部分。

这样，在Tornado中使用模板继承语法{% include "navbar.html" %}来引入一个单独的HTML文件作为导航栏就可以实现了。
注意上面的东西endblock是django里面的,tornado里面是end

# 4.对象管理

## 4.1.网页
主页面内容：

上导航栏：
标签：点击标签会有标签列表，碰到标签列表下拉显示所有的标签，有最大值限制。点击标签会显示所有的标签。
折叠：点击则将上导航栏缩小
设置：设置主页面的文档列表显示的相关内容，
每页显示的个数，
是否显示简介还是只有名称，
排序方式选择，
标签选择

## 4.2文档结构
文档的建立时间
文档名称
文档标签
文档内容
文档的最后编辑时间

## 4.3前端整理

### 4.3.1文章页面
#### 4.3.1.1顶部导航栏：
格式：
fix 相对窗口固定
内容：
1.左侧导航栏 折叠/展开按钮
控制左侧导航栏折叠展开
2.返回主页 index
3.返回blog页面 blog
4.文章标题

#### 4.3.1.2左侧导航栏
格式:
fix 相对窗口固定
上下scroll 左右hidden
内容:
1.文章目录
根据 文章的内容生成
2.点击文章目录可以跳转
3.包含多级标题显示

### 4.3.2主页面
显示最新的内容


#### 4.3.2.1顶端导航栏
home
blog
about

#### 4.3.2.2左侧边栏
显示标签云
显式栏目的引导
还有统计信息，更新频率相关内容


### 4.3.3博客页面
进行所有博客的搜索，过滤和显示

#### 4.3.3.1左侧导航栏
搜索：

搜索的依据：
标签
栏目
内容关键词

排序的依据：
建立时间
最新更新时间

