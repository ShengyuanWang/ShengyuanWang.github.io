---
layout: post
title: "Django Note"
date: 2023-01-13
author: "SWang"
header-img: "img/bg-material.jpg"
tags: [Django]
---

# Env Setup

### Step 1

```bash
# 使用系统自带的venv创建
python3 -m venv 虚拟环境名称

# 在虚拟环境下安装django
pip install django==2.1.2

#在项目目录下使用
django-admin startproject `应用名
#进入项目目录之后使用
python manage.py startapp 应用名

****
```

### Step2 - django 项目目录

```bash
应用文件夹：
	admin.py 配置后台管理系统的配置文件
	app.py 注册子应用的文件
	models.py 数据模型 与数据库交互的文件
	views.py 网站的交互文件，网站中的跳转 登陆 支付功能都在该文件中出现

项目文件夹：
	settings.py django网站的配置文件
	urls.py 网站的入口配置文件
	wsgi.py 网站服务器部署文件
```

### Step3 - 如何启动

```bash
python manage.py runserver 0.0.0.0:8000
```

![django run pic](/img/in_post/2023-01-03-django-note/success_django_run.png)

### Step4 - 简单的路由设置

`./app/views.py`

```bash
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#视图函数
def index(request):
	return HttpResponse('hello django')
```

**设置子路由**

`./app/urls.py`

```bash
from django.urls import path
from .views import index
urlpatterns = [
    path('', index),
]
```

**更新根路由**

`./one/urls.py`

```bash
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
```

# About URL

**url 中的参数设置**

```bash
1.在url后面用?开始，键值等于号链接，中间用&分开，比如http://127.0.0.1:8000/app?name=dewei&age=30
2.在陆游的参数重用分隔号分开比如http://127.0.0.1:8000/app/dewei/30
```

**django2.x 的 url 变量类型**

```bash
字符串类型，匹配任何非空字符串，但不包括斜杠，在不指定类型的前提下，默认字符串类型 <str:name>
整型，匹配0和正整数 <int:age>
slug: 可理解为注释后缀或附属型概念 <slug:day>
uuid: 匹配一个uuid格式的对象 <uuid:uid> 类似xxx-xx-xx
```

**支持 url 类型的方法**

```bash
2.0以后的新方法
from django.urls import path
补充：在django之后，可以映入repath模块来支持正则表达式

2.0以前的方法不支持参数重的类型，只能通过正则表达式的方式进行基本的pipei
from django.conf.urls import url
```

**Django2.0 以前 url 参数匹配简介**

```bash
url(r'^add/(?P<name>\w+)/(?P<name>\d+)$')

r 非转义原始字符串
w+ 匹配一个或者多个包括下划线在哪的任何字符串
d+ 匹配一个或者多个数字
```

**为 url 设置别名**

```bash
path('add', view_function, name='add')
```

**视图读取参数**

```bash
?形式的参数：
	request.GET.get(参数名)
url路由设置为：
	path('add', add)
以分隔符形式的参数：
	def index(request, name1, name2):
		print(name1)
url设置为：
	path('<str:name>/<int:age>', add)
```

# Views

**视图的详细讲解**

```bash
我们可以讲views的工作流程分为三个部分：
	1. 用户使用浏览器向网站发送请求 request
	2. 对用户的请求作出相应的处理 handler
	3. 将处理后的数据返回给浏览器 response
```

**用户的请求对象 request**

```bash
浏览器向服务器发送的请求对象，包含用户信息，请求内容和请求方法
我们可以用dir(request)去看request对象中的所有方法
```

**常用的 request 对象方法**

```bash
1. request.GET 获取url以？形式的参数
2. request.POST 获取post提交的数据
3. request.path 请求的路径，比如127.0.0.1/test/1 那么这个值就会是/test/1
4. request.mathod 请求的方法 比如：get post
5. request.COOKIES 请求过来的cookies
6. request.user 请求的用户对象，可以通过它判断用户是否登陆，并获取用户信息
7. request.session 一个既可读又可以写的类似与字典的对象，表示当前会话
8. request.META 一个标准的python库， 包含所有的HTTP收不，具体的头部信息取决于客户端和服务器
```

**常用的返回对象**

```bash
HttpResponse可以直接喊回一些字符串内容
render 将数据在模版中渲染并显示
JasonResponse 返回一个json类型， 通常与前端进行ajax交互

from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
```

视图面向对象的写法

```bash
from django.views.generic import View

class Test(View):
		def get(self, request):
			pass
		def get(self, request):
			pass
```

# restful 规范&http 协议

**Restful**

```bash
url定位资源，简单来说，通过一个url地址可以让我们知道这个地址所要提供的功能是什么
比如说：127.0.0.1/add/user 可以看出我们这个url所要做的事情就是添加一个yonghu
再比如说：127.0.0.1/get/user/1 就可以很轻松的读出来是获取一个用户并且这个用户id是1
```

**restful 常用方法**

```bash
Get 获取资源时使用 比如我们查看一个网页
Post 提交资源时使用 比如我们注册一个用户的时候
Put 修改资源的时候 比如我们修改自己的用户信息的时候
Delete 删除资源时使用 比如我们注销我们账号的时候
```

**Http 协议**

```bash
网上应用最为广泛的一种网络协议，所有www文件都必须遵守这个标准
```

**Http 的无状态性**

```bash
无状态是指，当浏览器发送请求给服务器的时候，服务器响应客户端的请求，但是当用一个浏览器再次给你服务器发送请求的时候，服务器并不知道它就是刚才的那个浏览器
简单的说，服务器不会记得你，所以就是无状态协议
```

**Http 常用状态码**

```
200 成功
400 请求错误，一般是参数格式有问题的时候出现
402 禁止访问
404 没有获取到url地址
405 方法仅用，比如这个地址指定用get方法，但你用了post，就会有这个提示
500 服务器异常
```

# 模版 Template 介绍，配置，以及 View 绑定

**template 模版**

```bash
模版可以动态生成Html网页，它包括部分Html代码和一些特殊的语法
```

**template 配置方法**

```bash
一半template模版存放在“template”目录中
通过在项目settings的templates的DIRS列表中添加对应的路径即可 比如
	os.path.join(BASE_DIR, 'templates')
```

**Template 与视图的绑定**

```bash
通过 from django.shortcuts import render 模块
return render(request, template_path, {k:v})
字典中的key和value就是要向前端渲染出的数据
```

**Template 展示渲染的数据**

```
在html中以{.{.}.}为标示，在双打括号中传入视图中传入的数据
```

**视图中的基本写法**

```bash
from django.shortcuts import render
from django.views import View

class Index(View):
	def get(self, request):
		return render(request, 'index.html', {key: value})
```

# Template 内置标签与静态文件配置

**变量与标签**

```bash
什么是变量？
	变量用{.{.}.}双打括号包裹，比如我们后端渲染过来的数据，用双大括号来包裹，例如{{name}}
内置标签
内置标签类型，用{.% %.}大括号， 左右各一个百分号包裹
```

**内置标签**

![form-example](/img/in_post/2023-01-03-django-note/form-example.png)

**for 标签模版**

```bash
forloop.counter 从1开始计算获取当前索引
forloop.counter0 从0开始计算获取当前索引
forloop.recounter 索引从最大数递减到1
forloop.recounter0 索引从最大数递减到0
forloop.first 当前元素是否是第一个
forloop.last 当前元素是否为最后一个
empty 为空的情况
```

**静态文件配置**

```bash
项目根目录‘static’与‘templates’文件夹同级
在settings文件中配置static文件夹
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static')))
```

**什么是静态文件？**

```bash
CSS 样式文件
JS 文件
IMG 图片等文件
```
