print("Hello, %s" % "world")
# 'Hello, world'
print("Hi, %s, you have $%d." % ("Michael", 1000000))
# 'Hi, Michael, you have $1000000.'

print("%2d-%02d" % (3, 1))
#  3-01
print("%.2f" % 3.1415926)
# 3.14

print("Age: %s. Gender: %s" % (25, True))
# 'Age: 25. Gender: True'

print("growth rate: %d %%" % 7)
# 'growth rate: 7 %'

print("Hello, {0}, 成绩提升了 {1:.1f}%".format("小明", 17.125))
# Hello, 小明, 成绩提升了 17.1%


s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print("%s的成绩今年提升了%.2f%%。" % ("小明", r))
# 小明的成绩今年提升了18.06%。

