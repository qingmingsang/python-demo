def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))  # 99

import math

a = float(input("请输入a:"))
b = float(input("请输入b:"))
c = float(input("请输入c:"))


def quadratic(a, b, c):
    if a == 0 or b ** 2 - 4 * a * c < 0:
        print("无解")
    else:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        print("方程式解为：x1=%.2f,x2=%.2f" % (x1, x2))


print("quadratic(2, 3, 1) =", quadratic(2, 3, 1))
print("quadratic(1, 3, -4) =", quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print("测试失败")
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print("测试失败")
else:
    print("测试成功")

