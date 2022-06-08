# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2022/6/7 下午 4:50 
import time
from proj.main import app

@app.task
def add(x, y):
    time.sleep(1)
    return x + y