# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2022/6/7 下午 4:52 
from proj.tasks import add
import time

t1 = time.time()

# r1 = add.delay(1, 2)
# r2 = add.delay(2, 4)
# r3 = add.delay(3, 6)
# r4 = add.delay(4, 8)
# r5 = add.delay(5, 10)
# r6 = add.apply_async((2, 2), queue='lopri', countdown=2)

r_list = [
    *[add.delay(i, 2 * i) for i in range(1, 6)],
    add.apply_async((99, 99), countdown=2)
]
for r in r_list:
    while not r.ready():
        time.sleep(0.1)
    print(r.result)
    print(r.status)

t2 = time.time()

print('共耗时：%s' % str(t2 - t1))
