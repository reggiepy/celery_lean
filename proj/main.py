# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2022/6/7 下午 4:41
# import os
# os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
from celery import Celery

app = Celery(
    'tasks',
    broker=r'pyamqp://guest:guest@172.18.50.56//test2',
    backend="redis://127.0.0.1:6379/5",
    include=['proj.tasks']
)
# app = Celery(
#     'tasks',
#     broker='redis://127.0.0.1:6379/4',
#     backend="redis://127.0.0.1:6379/5",
#     include=['proj.tasks']
# )

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start(
        [
            "worker",
            '--loglevel=INFO',
            '-P',
            'eventlet',
            '-n',
            'main@%h',
        ]
    )
