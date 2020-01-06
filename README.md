### 调试阶段
#### -w 是设置运行工作线程数
#### -b 设置监听IP和端口
gunicorn -w 4 -b 0.0.0.0:8888 test:app

### 生产环境设置配置文件
gunicorn -c config.py run:app

### 查看PID号
ps -ef | grep gunicorn