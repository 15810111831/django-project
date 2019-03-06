### 安装python 和 pip 
1. [安装教程](https://blog.csdn.net/lijunweiyhn/article/details/79037445)
2. 安装完毕后执行 `pip install -r requirements.txt`

### 安装Git
1. [Git安装教程](https://www.cnblogs.com/wj-1314/p/7993819.html)
2. 创建个项目文件夹, 进入文件夹之后执行 `git clone https://github.com/15810111831/django-project.git`

### 安装mysql数据库,并配置环境变量
1. [mysql 安装教程](https://blog.csdn.net/kan2016/article/details/80876722)

### 进入mysql 
1. `mysql -uroot -p`
2. `create database fruit charset=utf8mb4;` 创建数据库表

### 退出mysql, 进入项目目录, 同级文件有manage.py
3. 退出mysql,执行 `python manage.py migrate` 同步数据库
4. 执行 `python manage.py createsuperuser` 创建超级管理员
5. 执行 `python manage.py runserver 0.0.0.0:8000` 启动服务