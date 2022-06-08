# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2022/6/7 下午 6:12 

import subprocess

# celery -A proj.main  flower --address=127.0.0.1 --port=5555
cmd = [
    r'C:\Users\WT\celery_lean\Scripts\python.exe',
    '-m',
    'celery',
    '-A',
    'proj.main',
    'flower',
    '--address=127.0.0.1',  # flower需要的address
    '--port=5555',  # flower需要的端口号
]
if __name__ == '__main__':
    subprocess.run(cmd)
