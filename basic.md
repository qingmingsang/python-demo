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

## 字符编码
因为计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。最早的计算机在设计时采用8个比特（bit）作为一个字节（byte），所以，一个字节能表示的最大的整数就是255（二进制11111111=十进制255），如果要表示更大的整数，就必须用更多的字节。比如两个字节可以表示的最大整数是65535，4个字节可以表示的最大整数是4294967295。
由于计算机是美国人发明的，因此，最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为`ASCII`编码，比如大写字母A的编码是65，小写字母z的编码是122。
但是要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以，中国制定了`GB2312`编码，用来把中文编进去。
可以想得到的是，全世界有上百种语言，日本把日文编到Shift_JIS里，韩国把韩文编到Euc-kr里，各国有各国的标准，就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示出来会有乱码。

因此，`Unicode`应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。
Unicode标准也在不断发展，但最常用的是用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）。现代操作系统和大多数编程语言都直接支持Unicode。

现在，捋一捋ASCII编码和Unicode编码的区别：
ASCII编码是1个字节，而Unicode编码通常是2个字节。


字母A用ASCII编码是十进制的65，二进制的01000001；
字符0用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；
汉字中已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的01001110 00101101。

如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 01000001。

新的问题又出现了：如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。

本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间：

字符 |	ASCII |	Unicode	 | UTF-8
-|-|-|-
A	 |	01000001 |		00000000 01000001 |		01000001
中 |		x |		01001110 00101101	 |	11100100 10111000 10101101

在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：
@0

浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：
@1


## Python的字符串
在Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言.

Python提供了`ord()`函数获取字符的整数表示，`chr()`函数把编码转换为对应的字符
```
print(ord("A"))
# 65
print(ord("中"))
# 20013
print(chr(66))
# 'B'
print(chr(25991))
# '文'
print("\u4e2d\u6587")
# 中文
```

由于Python的字符串类型是`str`，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把`str`变为以字节为单位的`bytes`。

Python对`bytes`类型的数据用带`b`前缀的单引号或双引号表示
```
x = b'ABC'
```
要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

以Unicode表示的str通过`encode()`方法可以编码为指定的bytes

纯英文的str可以用ASCII编码为bytes，内容是一样的，
含有中文的str可以用UTF-8编码为bytes。
含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
```
print('ABC'.encode('ascii'))
# b'ABC'

print('中文'.encode('utf-8'))
# b'\xe4\xb8\xad\xe6\x96\x87'

print('中文'.encode('ascii'))
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
```

在bytes中，无法显示为ASCII字符的字节，用`\x##`显示。
反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用`decode()`方法
如果bytes中包含无法解码的字节，`decode()`方法会报错
```
print(b"ABC".decode("ascii"))
# 'ABC'
print(b"\xe4\xb8\xad\xe6\x96\x87".decode("utf-8"))
# '中文'
print(b"\xe4\xb8\xad\xff".decode("utf-8"))
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte
```

如果bytes中只有一小部分无效的字节，可以传入`errors='ignore'`忽略错误的字节
```
print(b"\xe4\xb8\xad\xff".decode("utf-8", errors="ignore"))
# '中'
```

要计算str包含多少个字符，可以用`len()`函数.
`len()`函数计算的是str的字符数，如果换成bytes，`len()`函数就计算字节数.
```
print(len("ABC"))
# 3
print(len("中文"))
# 2

print(len(b"ABC"))
# 3
print(len(b"\xe4\xb8\xad\xe6\x96\x87"))
# 6
print(len("中文".encode("utf-8")))
# 6
```
可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。

在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```
第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码

如果.py文件本身使用UTF-8编码，并且也申明了`# -*- coding: utf-8 -*-`，打开命令提示符测试就可以正常显示中文.

## 格式化
在Python中，采用的格式化方式和C语言是一致的，用`%`实现

有几个`%`占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个`%`，括号可以省略。

占位符  | 	替换内容
- | -
`%d`	| 整数
`%f`	| 浮点数
`%s`	| 字符串
`%x`	| 十六进制整数
`%.nf`   | 保留n位小数
`%2d`   | ?
`%02d`   | ?

```
print("Hello, %s" % "world")
# 'Hello, world'
print("Hi, %s, you have $%d." % ("Michael", 1000000))
# 'Hi, Michael, you have $1000000.'
```

格式化整数和浮点数还可以指定是否补0和整数与小数的位数
```
print("%2d-%02d" % (3, 1))
#  3-01
print("%.2f" % 3.1415926)
# 3.14
```

如果不太确定应该用什么，`%s`永远起作用，它会把任何数据类型转换为字符串：
```
print("Age: %s. Gender: %s" % (25, True))
# 'Age: 25. Gender: True'

print("growth rate: %d %%" % 7)
# 'growth rate: 7 %'
```

`%%`来表示一个`%`
```
s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print("%s的成绩今年提升了%.2f%%。" % ("小明", r))
# 小明的成绩今年提升了18.06%。
```

`format()`
另一种格式化字符串的方法是使用字符串的`format()`方法，它会用传入的参数依次替换字符串内的占位符`{0}、{1}……`
```
print("Hello, {0}, 成绩提升了 {1:.1f}%".format("小明", 17.125))
# Hello, 小明, 成绩提升了 17.1%
```

## 使用list和tuple

### list
Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

比如，列出班里所有同学的名字，就可以用一个list表示.
变量classmates就是一个list。用len()函数可以获得list元素的个数
用索引来访问list中每一个位置的元素，记得索引是从0开始的
```
>>> classmates = ['Michael', 'Bob', 'Tracy']
>>> classmates
['Michael', 'Bob', 'Tracy']

>>> len(classmates)
3

>>> classmates[0]
'Michael'
>>> classmates[1]
'Bob'
>>> classmates[2]
'Tracy'
>>> classmates[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。
如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
```
>>> classmates[-1]
'Tracy'
```

以此类推，可以获取倒数第2个、倒数第3个：
```
>>> classmates[-2]
'Bob'
>>> classmates[-3]
'Michael'
>>> classmates[-4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```
当然，倒数第4个就越界了。


list是一个可变的有序表，所以，可以往list中追加`append()`元素到末尾：
```
>>> classmates.append('Adam')
>>> classmates
['Michael', 'Bob', 'Tracy', 'Adam']
```

也可以把元素`insert()`插入到指定的位置，比如索引号为1的位置：
```
>>> classmates.insert(1, 'Jack')
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
```

要删除list末尾的元素，用`pop()`方法：
```
>>> classmates.pop()
'Adam'
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy']
```

要删除指定位置的元素，用`pop(i)`方法，其中i是索引位置：
```
>>> classmates.pop(1)
'Jack'
>>> classmates
['Michael', 'Bob', 'Tracy']
```

要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
```
>>> classmates[1] = 'Sarah'
>>> classmates
['Michael', 'Sarah', 'Tracy']
```

list里面的元素的数据类型也可以不同，比如：
```
>>> L = ['Apple', 123, True]
```

list元素也可以是另一个list，比如：
```
>>> s = ['python', 'java', ['asp', 'php'], 'scheme']
>>> len(s)
4
```

要注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了：
```
>>> p = ['asp', 'php']
>>> s = ['python', 'java', p, 'scheme']
```
要拿到'php'可以写`p[1]`或者`s[2][1]`，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。

如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
```
>>> L = []
>>> len(L)
0
```

### tuple
另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
```
>>> classmates = ('Michael', 'Bob', 'Tracy')
```
现在，classmates这个tuple不能变了，它也没有`append()`，`insert()`这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用`classmates[0]，classmates[-1]`，但不能赋值成另外的元素。

不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
```
>>> t = (1, 2)
>>> t
(1, 2)
```

如果要定义一个空的tuple，可以写成()：
```
>>> t = ()
>>> t
()
```

但是，要定义一个只有1个元素的tuple，如果你这么定义：
```
>>> t = (1)
>>> t
1
```

定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。

所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
```
>>> t = (1,)
>>> t
(1,)
```

Python在显示只有1个元素的tuple时，也会加一个逗号`,`，以免你误解成数学计算意义上的括号。

最后来看一个“可变的”tuple：
```
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
```
这个tuple定义的时候有3个元素，分别是'a'，'b'和一个list。

表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。


## 条件判断
计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。

比如，输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现：
```
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
```
根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。

也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了：
```
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
```
注意不要少写了冒号`:`。

当然上面的判断是很粗略的，完全可以用elif做更细致的判断：
```
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
```

elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是：
```
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
```

if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else，所以，请测试并解释为什么下面的程序打印的是teenager：
```
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
```

if判断条件还可以简写，比如写：
```
if x:
    print('True')
```
只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。

### 再议 input
最后看一个有问题的条件判断。很多同学会用`input()`读取用户的输入，这样可以自己输入，程序运行得更有意思：
```
birth = input('birth: ')
if birth < 2000:
    print('00前')
else:
    print('00后')
```
输入1982，结果报错：
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: str() > int()
```
这是因为`input()`返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了`int()`函数来完成这件事情：
```
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
```
再次运行，就可以得到正确地结果。但是，如果输入abc呢？又会得到一个错误信息：
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'abc'
```
`int()`函数发现一个字符串并不是合法的数字时就会报错，程序就退出了。


## 循环
要计算1+2+3，我们可以直接写表达式：
```
>>> 1 + 2 + 3
6
```
要计算1+2+3+...+10，勉强也能写出来。
但是，要计算1+2+3+...+10000，直接写表达式就不可能了。
为了让计算机能计算成千上万次的重复运算，我们就需要循环语句。

Python的循环有两种，一种是`for...in`循环，依次把list或tuple中的每个元素迭代出来，看例子：
```
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 执行这段代码，会依次打印names的每一个元素：
# 
# Michael
# Bob
# Tracy
```

所以`for x in ...`循环就是把每个元素代入变量x，然后执行缩进块的语句。

再比如我们想计算1-10的整数之和，可以用一个sum变量做累加：
```
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

L = ["Bart", "Lisa", "Adam"]
for x in L:
    print(x)
```

如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个`range()`函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
```
>>> list(range(5))
[0, 1, 2, 3, 4]
```

第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
```
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
```
在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出。

### break
在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：
```
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')
```
上面的代码可以打印出1~100。

如果要提前结束循环，可以用break语句：
```
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
```
执行上面的代码可以看到，打印出1~10后，紧接着打印END，程序结束。
可见break的作用是提前结束循环。


### continue
在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
```
n = 0
while n < 10:
    n = n + 1
    print(n)
```

上面的程序可以打印出1～10。但是，如果我们想只打印奇数，可以用continue语句跳过某些循环：
```
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
```
执行上面的代码可以看到，打印的不再是1～10，而是1，3，5，7，9。
可见continue的作用是提前结束本轮循环，并直接开始下一轮循环。

## dict
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
```
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
```

给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。

如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下：
```
>>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['Michael']
95
```
为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。

第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。

dict就是第二种实现方式，给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。

这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value。
把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
```
>>> d['Adam'] = 67
>>> d['Adam']
67
```

由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
```
>>> d['Jack'] = 90
>>> d['Jack']
90
>>> d['Jack'] = 88
>>> d['Jack']
88
```

如果key不存在，dict就会报错：
```
>>> d['Thomas']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Thomas'
```

要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
```
>>> 'Thomas' in d
False
```

二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
```
>>> d.get('Thomas')
# 返回None的时候Python的交互环境不显示结果。
>>> d.get('Thomas', -1)
-1
```

要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
```
>>> d.pop('Bob')
75
>>> d
{'Michael': 95, 'Tracy': 85}
```
请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：
- 查找和插入的速度极快，不会随着key的增加而变慢；
- 需要占用大量的内存，内存浪费多。

而list相反：
- 查找和插入的时间随着元素的增加而增加；
- 占用空间小，浪费内存很少。

所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
```
>>> key = [1, 2, 3]
>>> d[key] = 'a list'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

### set
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

要创建一个set，需要提供一个list作为输入集合：
```
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}
```

注意，传入的参数`[1, 2, 3]`是一个list，而显示的`{1, 2, 3}`只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。

重复元素在set中自动被过滤：
```
>>> s = set([1, 1, 2, 2, 3, 3])
>>> s
{1, 2, 3}
```

通过`add(key)`方法可以添加元素到set中，可以重复添加，但不会有效果：
```
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
```

通过`remove(key)`方法可以删除元素：
```
>>> s.remove(4)
>>> s
{1, 2, 3}
```

set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
```
>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2
{2, 3}
>>> s1 | s2
{1, 2, 3, 4}
```
set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。

### 再议不可变对象
上面我们讲了，str是不变对象，而list是可变对象。

对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
```
>>> a = ['c', 'b', 'a']
>>> a.sort()
>>> a
['a', 'b', 'c']
```

而对于不可变对象，比如str，对str进行操作呢：
```
>>> a = 'abc'
>>> a.replace('a', 'A')
'Abc'
>>> a
'abc'
```

虽然字符串有个`replace()`方法，也确实变出了'Abc'，但变量a最后仍是'abc'，应该怎么理解呢？
```
>>> a = 'abc'
>>> b = a.replace('a', 'A')
>>> b
'Abc'
>>> a
'abc'
```
a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'：
当我们调用`a.replace('a', 'A')`时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：
所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。





























































