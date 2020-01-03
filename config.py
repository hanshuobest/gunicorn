# config.py
import os
import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing

# 生产环境下不需配置，调试的时候开始，启动gunicorn时可以看到所有项的配置
debug = True
# 用于控制errorlog的信息级别，可以设置为debug,info,warning,error,critical
loglevel = 'debug'
bind = "10.1.25.84:8888"
pidfile = "log/gunicorn.pid"
# 访问日志
accesslog = "log/access.log"
errorlog = "log/debug.log"
# 开启后台运行，默认为False
daemon = True

# 启动的进程数
workers = multiprocessing.cpu_count()
# 指开启的每个工作进程的模式类型，默认为sync模式，野结衣使用gevent模式
worker_class = 'gevent'
x_forwarded_for_header = 'X-FORWARDED-FOR'