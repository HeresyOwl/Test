#測試NumPy ********************************************************************
import numpy as np
a = np.arange(24).reshape(2, 3, 4)     #新建一個從0~24的2X3X4的矩陣
print('a = ' + str(a))
b = a[1][1][1]
print('b = ' + str(b))
c = a[:, 2, :]
print('c = ' + str(c))
d = a[:, :, 1]
print('d = ' + str(d))
e = a[..., 1]
print('e = ' + str(e))
f = a[:, 1:, 1:-1]
print('f = ' + str(f))
g = np.split(np.arange(9), 3)      #拆成3等分的矩陣
print('g = ' + str(g))
h = np.split(np.arange(9), [2, -3])        #拆成3個1X2,1X4,1X3的矩陣
print('h = ' + str(h))
hh = np.arange(6).reshape((2, 3))        #新增1個從0~6的2X3維矩陣
hhh = np.arange(6, 12).reshape(2, 3)        #新增1個從6~12的2X3維矩陣
print('hh = ' + str(hh))
print('hhh = ' + str(hhh))
m = np.vstack((hh, hhh))      #垂直拼接
p = np.hstack((hh ,hhh))      #水平拼接
print('m = ' + str(m))
print('p = ' + str(p))
q = np.concatenate((hh, hhh))      #垂直拼接
r = np.concatenate((hh, hhh), axis=-1)      #水平拼接
print('q = ' + str(q))
print('r = ' + str(r))
s = np.stack((hh, hhh))    #新增維度，從2維變成3維
print('s = ' + str(s))
t = s.transpose((2, 0, 1))     #轉置矩陣
print('t = ' + str(t))
u = a[0].transpose()     #指定維度轉置
print('u = ' + str(u))
v = np.rot90(u, 3)     #逆時針旋轉3次
print('v = ' + str(v))
w = np.fliplr(u)       #左右翻轉
print('w = ' + str(w))
x = np.flipud(u)       #上下翻轉
print('x = ' + str(x))
y = np.roll(u, 1)      #所有維度按順序滾動位移1位
print('y = ' + str(y))
z = np.roll(u, 1, axis=1)      #第2維度按順序滾動位移1位
print('z = ' + str(z))

#線性代數
aa = np.array([3, 4])
xx = np.linalg.norm(aa)
print('xx = ' + str(xx))
bb = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
cc = np.array([1, 0, 1])
yy = np.dot(cc, b.T)
print('yy = ' + str(yy))