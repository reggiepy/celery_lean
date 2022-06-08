# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2022/6/7 下午 6:12 

import subprocess

# celery -A proj.main worker --loglevel=INFO  -P eventlet
cmd = [
    r'C:\Users\WT\celery_lean\Scripts\python.exe',
    '-m',
    'celery',
    '-A',
    'proj.main',
    'worker',
    '--loglevel=INFO',  # flower需要的address
    '-P',  # -P
    'eventlet',  # eventlet
    '-n',
    'worker1@%h',
]
if __name__ == '__main__':
    subprocess.run(cmd)
