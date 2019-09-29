# python 基础

`python` 进入环境
`exit()` 退出
`input()` 接受输入,返回的数据类型是str.
`print()` 打印

在命令行模式下，可以执行`python`进入Python交互式环境，也可以执行`python hello.py`运行一个.py文件。

Python用缩进来组织代码块,按照约定俗成的管理，应该始终坚持使用`4个空格`的缩进。
以`#`开头的语句是注释.
每一行都是一个语句，当语句以冒号`:`结尾时，缩进的语句视为代码块。
大小写敏感.

## 输入输出
`print()`函数也可以接受多个字符串，用逗号“,”隔开.
每遇到逗号“,”会输出一个空格.
Python提供了一个`input()`，可以让用户输入字符串，并存放到一个变量里。

## 整数与浮点数
Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在`-2147483648-2147483647`。

Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。

十六进制用`0x`前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2，等等。

整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法也是精确的），而浮点数运算则可能会有四舍五入的误差。

`/`除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
还有一种除法是`//`，称为地板除，两个整数的除法仍然是整数
整数的地板除//永远是整数，即使除不尽
Python还提供一个余数运算`%`，可以得到两个整数相除的余数
```
print(10 / 3)
# 3.3333333333333335
print(9 / 3)
# 3.0
print(10 // 3)
# 3
print(10 % 3)
# 1
print(10 // 3.1)
# 3.0
```

## 字符串
转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
```
print('I\'m \"OK\"!')  
I'm "OK"!

print('I\'m learning\nPython.')
I'm learning
Python.

print('\\\n\\')
\
\
```

如果只是为了显示`''` `""`
```
print("Hello, 'Adam'")
Hello, 'Adam'
print('Hello, "Bart"')
Hello, "Bart"
```

如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，
Python还允许用`r''`表示''内部的字符串默认不转义：
```
>>> print('\\\t\\')
\       \
>>> print(r'\\\t\\')
\\\t\\
```

如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，
Python允许用`'''...'''`的格式表示多行内容：
```
print('''line1
line2
line3''')
line1
line2
line3

print(
    r"""hello,\n
world"""
)
hello,\n
world
```

## 布尔值
and运算是与运算，只有所有都为True，and运算结果才是True
or运算是或运算，只要其中有一个为True，or运算结果就是True
not运算是非运算，它是一个单目运算符，把True变成False，False变成True

## 空值
`None`是一个特殊的空值

## 变量
变量名必须是大小写英文、数字和_的组合，且不能用数字开头

在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量

这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。

`a = 'ABC'`时，Python解释器干了两件事情：
1. 在内存中创建了一个'ABC'的字符串；
2. 在内存中创建了一个名为a的变量，并把它指向'ABC'。

```
a = "ABC"
b = a
a = "XYZ"
print(b)
ABC
```


## 常量
在Python中，通常用全部大写的变量名表示常量
Python根本没有任何机制保证全部大写的变量不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法

