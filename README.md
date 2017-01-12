#**awesome-python3-webapp**
参考学习来源：[廖雪峰python3教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)<br>
测试平台：Windows10 + Python3.5.2
---
####Day 1 - 搭建开发环境
#####搭建开发环境
>首先，确认系统安装的Python版本是3.5.x：
```python
    E:\virtualenv> python3 --version
    Python 3.5.2
```
>然后，用virtualenv创建隔离的开发环境
```python
    E:\virtualenv> virtualenv awesome-python3-webapp --no-site-packages --python=D:\Python35\python.exe
    Running virtualenv with interpreter D:\Python35\python.exe
    Using base prefix 'D:\\Python35'
    New python executable in E:\virtualenv\awesome-python3-webapp\Scripts\python.exe
    Installing setuptools, pip, wheel...done.
```
>激活virtualenv：
```python
    E:\virtualenv> cd awesome-python3-webapp\Scripts
    E:\virtualenv\awesome-python3-webapp\Scripts> activate
    (awesome-python3-webapp) E:\virtualenv\awesome-python3-webapp\Scripts>
```
>接下来用pip安装开发Web APP需要的第三方库(以下安装都是使用豆瓣的源)：<br>
>异步框架aiohttp：
```python
    (awesome-python3-webapp) E:\virtualenv\awesome-python3-webapp\Scripts>pip3 install -i https://pypi.douban.com/simple aiohttp
```
>前段模板引擎jinja2
```python
    (awesome-python3-webapp) E:\virtualenv\awesome-python3-webapp\Scripts>pip3 install -i https://pypi.douban.com/simple jinja2
```
>MySQL的Python异步驱动程序aiomysql(前提：MySQL 5.x数据库已经安装)：
```python
    (awesome-python3-webapp) E:\virtualenv\awesome-python3-webapp\Scripts>pip3 install -i https://pypi.douban.com/simple aiomysql
```
#####项目结构
>选择一个工作目录，然后新建如下的目录结构：

    awesome-python3-webapp/     <--- 根目录
    |
    +—— backup/                 <---- 备份目录
    |
    +—— conf/                   <---- 配置文件
    |
    +—— dist/                   <---- 打包目录
    |
    +—— www/                    <---- Web目录，存放.py文件
    |   |
    |   +—— static/             <---- 存放静态文件
    |   |
    |   +—— templates/          <---- 存放模板文件
    |
    +—— ios/                    <---- 存放IOS APP工程
    |
    +—— LICENSE                 <---- 代码LICENSE

>创建好项目的目录结构后，建立git仓库awesome-python3-webapp并同步至[github](https://github.com)，保证代码修改的安全
#####开发工具
>[Sublime Text3](http://www.sublimetext.com/3) + [PyCharm](https://www.jetbrains.com/pycharm/)