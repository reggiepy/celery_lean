# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2022/6/7 下午 4:50 
broker_url = 'redis://localhost:6379/4' # 使用Redis作为消息代理
# BROKER_URL = 'amqp://admin:wangtong123.@172.18.50.56//' # 使用rabbitmq作为消息代理

RESULT_BACKEND = 'redis://localhost:6379/4' # 把任务结果存在了Redis

TASK_SERIALIZER = 'msgpack' # 任务序列化和反序列化使用msgpack方案
TASK_SERIALIZER = 'json' # 任务序列化和反序列化使用msgpack方案

RESULT_SERIALIZER = 'json' # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON

TASK_RESULT_EXPIRES = 60 * 60 * 24 # 任务过期时间

ACCEPT_CONTENT = ['json', 'msgpack'] # 指定接受的内容类型
ACCEPT_CONTENT = ['json'] # 指定接受的内容类型