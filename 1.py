# _*_ coding:utf-8 _*_

#老鼠吃大米，一天吃总量的一半多一个，正好第i天吃完
#i = input("请输入天数")
n = 0
def dg(i):
    global n
    if i >= 1:
        n = (dg(i-1) + 1) * 2
    return n
print(dg(6))

#1+2+3+4+5+。。。
def bg(i):
    n = 0
    if i >= 1:
        n = bg(i-1) + i
    return n


print(bg(2))

# 阶乘
def qg(i):
    m = 1
    if i > 1:
        m = qg(i-1) * i
    return m 

print(qg(4))
