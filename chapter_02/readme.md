# 第2章 变量和简单数据类型



## 2.2 变量

尝试在*hello_world.py*使用一个**变量**：

```python
message = "Hello Python world!"
print(message)
```

运行：

```bash
$python3 hello_world.py
Hello Python world!
```

每个变量都存储了一个值 —— 与变量相关联的信息。

扩展：修改*hello_world.py*

```python
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)
```

运行：

```bash
$python3 hello_world.py
Hello Python world!
Hello Python Crash Course world!
```

在程序中可随时修改变量的值,而 Python 将始终记录变量的最新值。

### 2.2.1 变量的命名和使用

在 Python 中使用变量时,需要遵守一些规则和指南。违反这些规则将引发错误,而指南旨在让你编写的代码更容易阅读和理解。请务必牢记下述有关变量的规则。

- 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头,但不能以数字打头,例如,可将变量命名为 message_1 ,但不能将其命名为 1_message 。
- 变量名不能包含空格,但可使用下划线来分隔其中的单词。例如,变量名 greeting_message 可行,但变量名 greeting message 会引发错误。
- 不要将 Python 关键字和函数名用作变量名,即不要使用 Python 保留用于特殊用途的单词,如 print
- 变量名应既简短又具有描述性。例如, name 比 n 好, student_name 比 s_n 好, name_length 比 length_of_persons_name 好。
- 慎用小写字母 l 和大写字母 O ,因为它们可能被人错看成数字 1 和 0 。

### 2.2.2 使用变量时避免命令错误

```bash
>>> message = "Hello Python Crash Course reader!"
>>> print(mesage)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mesage' is not defined
>>>
```



**动手试一试：**

请完成下面的练习,在做每个练习时,都编写一个独立的程序。保存每个程序时,使用符合标准 Python 约定的文件名:使用小写字母和下划线,如 simple_message.py 和
simple_messages.py 。

**2-1 简单消息：** 将一条消息存储到变量中,再将其打印出来。

​	[simple_message.py]()

**2-2 多条简单消息：** 将一条消息存储到变量中,将其打印出来;再将变量的值修改为一条新消息,并将其打印出来。

​	[multiple_message.py]()



## 2.3 字符串

**字符串**就是一系列字符。在Python中，用单引号或者双引号括起的都是字符串。

```python
"This is a string."
'This is also a string.'
```

这种灵活性让你能够在字符串中包含引号和撇号:

```python
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
```

### 2.3.1 使用方法修改字符串的大小写

请看下面的代码,并尝试判断其作用:

```python
# name.py
name = "ada lovelace"
print(name.title())
```

没有在终端运行之前：单看*.title()*的话，我以为是简单的照本输出。

运行输出：

```bash
$python3 name.py
Ada Lovelace
```

title() 以首字母大写的方式显示每个单词,即将每个单词的首字母都改为大写。这很有用,因为你经常需要将名字视为信息。例如,你可能希望程序将值 Ada 、 ADA 和 ada视为同一个名字,并将它们都显示为 Ada 。

还有其他几个很有用的大小写处理方法。例如,要将字符串改为全部大写或全部小写,可以像下面这样做：

```python
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
```

这些代码的输出如下:

```bash
ADA LOVELACE
ada lovelace
```

### 2.3.2 合并（拼接）字符串

在很多情况下,都需要合并字符串。

```python
first_name = "ada"
last_name = "lovelace"
# 使用（+）来合并
full_name = first_name + " " + last_name
# 整条消息都存储在一个变量
message = "Hello, " + full_name.title() + "!"
print(full_name)
print("Hello, " + full_name.title() + "!")
print(message)
```

Python 使用加号( + )来合并字符串。结果如下：

```bash
ada lovelace
Hello, Ada Lovelace!
Hello, Ada Lovelace!
```

### 2.3.3 使用制表符或换行符来添加空白

在编程中,**空白**泛指任何非打印字符,如空格、制表符和换行符。

要在字符串中添加制表符,可使用字符组合 \t：

```bash
>>> print("Python")
Python
>>> print("\tPython")
	Python
>>>
```

要在字符串中添加换行符,可使用字符组合 \n :

```bash
>>> print("Languages:\nPython\nC\nJavaScript")
Languages:
Python
C
JavaScript
>>>
```

还可在同一个字符串中同时包含制表符和换行符。

```bash
>>> print("Languages:\n\tPython\n\tC\n\tJavaScript")
Languages:
	Python
	C
	JavaScript
>>>
```

### 2.3.4 删除空白

Python 能够找出字符串开头和末尾多余的空白。要确保字符串**末尾**没有空白,可使用方法 rstrip() 。

```bash
>>> favourite_language = 'python '
>>> favourite_language
'python '
>>> favourite_language.rstrip()
'python'
>>> favourite_language
'python '
>>>
>>> favourite_language = 'p ython'
>>> favourite_language
'p ython'
>>> favourite_language.rstrip()
'p ython'
```

变量 favorite_language 调用方法 rstrip() 后，空格被暂时的删除了，下次再询问该变量时还是带空格。

要永久删除这个字符串中的空白,必须将删除操作的结果存回到变量中:

```bash
>>> favorite_language = 'python '
>>> favorite_language = favorite_language.rstrip()
>>> favorite_language
'python'
```

还可以剔除字符串开头的空白,或同时剔除字符串两端的空白。为此,可分别使用方法 lstrip() 和 strip() :

```bash
>>> favorite_language = ' python '
>>> favorite_language.rstrip()
' python'
>>> favorite_language.lstrip()
'python '
>>> favorite_language.strip()
'python'
```

### 2.3.5 使用字符串时避免语法错误

**语法错误** 是一种时不时会遇到的错误。程序中包含非法的 Python 代码时,就会导致语法错误。例如,在用单引号括起的字符串中,如果包含撇号,就将导致错误。这是因为这会导致 Python 将第一个单引号和撇号之间的内容视为一个字符串,进而将余下的文本视为 Python 代码,从而引发错误。

### 2.3.6 Python2中的print语句

在 Python 2 中, print 语句的语法稍有不同:

```bash
>>> python2.7
>>> print "Hello Python 2.7 world!"
Hello Python 2.7 world!
```

在 Python 2 中,无需将要打印的内容放在括号内。从技术上说, Python 3 中的 print 是一个函数,因此括号必不可少。有些 Python 2 print 语句也包含括号,但其行为与 Python 3 中
稍有不同。简单地说,在 Python 2 代码中,有些 print 语句包含括号,有些不包含。

***

**动手试一试**

**2-3 个性化消息：** 将用户的姓名存到一个变量中,并向该用户显示一条消息。显示的消息应非常简单,如 “Hello Eric, would you like to learn some Python today?” 。

​	[personalized_message.py]()

**2-4 调整名字的大小写：** 将一个人名存储到一个变量中,再以小写、大写和首字母大写的方式显示这个人名。

​	[2-4.py]()

**2-5 名言：** 找一句你钦佩的名人说的名言,将这个名人的姓名和他的名言打印出来。输出应类似于下面这样(包括引号):Albert Einstein once said, “A person who never made a mistake never tried anything new.”

​	[saying.py]()

**2-6 名言2：** 重复练习 2-5 ,但将名人的姓名存储在变量 famous_person 中,再创建要显示的消息,并将其存储在变量 message 中,然后打印这条消息。

​	[saying2.py]()

**2-7 剔除人名中的空白：** 存储一个人名,并在其开头和末尾都包含一些空白字符。务必至少使用字符组合 "\t" 和 "\n" 各一次。打印这个人名,以显示其开头和末尾的空白。然后,分别使用剔除函数 lstrip() 、 rstrip() 和 strip() 对人名进行处理,并将结果打印出来。



## 2.4 数字

在编程中,经常使用数字来记录游戏得分、表示可视化数据、存储 Web 应用信息等。 Python 根据数字的用法以不同的方式处理它们。

### 2.4.1 整数

在 Python 中,可对整数执行加( + )减( - )乘( * )除( / )运算。

```bash
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 2 / 3
0.6666666666666666
>>> 3 / 2
1.5
>>>
```

在终端会话中, Python 直接返回运算结果。 Python 使用两个乘号表示乘方运算:

```bash
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000
>>>
```

Python 还支持运算次序,因此你可在同一个表达式中使用多种运算。

```bash
>>> 2 + 3 * 4
14
>>> (2 + 3) * 4
20
>>>
```

### 2.4.2 浮点数

Python 将带小数点的数字都称为**浮点数** 。

```bash
>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>>
```

需要注意的是,结果包含的小数位数可能是不确定的:

```bash
>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
>>>
```

所有语言都存在这种问题,没有什么可担心的。 Python 会尽力找到一种方式,以尽可能精确地表示结果,但鉴于计算机内部表示数字的方式,这在有些情况下很难。就现在而言,暂时忽略多余的小数位数即可;在第二部分的项目中,你将学习在需要时处理多余小数位的方式。

### 2.4.3 使用函数str()避免类型错误

**birthday.py**

```python
age = 23
message = "Happy " + age + "rd Birthday!"

print(message)
```

程序的目的为了打印：Happy 23rd birthday!。但是编译器会报错。

这是一个**类型错误**，Python无法识别使用的信息。在这个示例中, Python 发现你使用了一个值为整数( int )的变量,但它不知道该如何解读这个值。 Python 知道,这个变量表示的可能是数值 23 ,也可能是字符 2 和 3 。像上面这样在字符串中使用整数时,需要显式地指出你希望 Python 将这个整数用作字符串。

为此,可调用函数 str() ,它让 Python 将非字符串值表示为字符串：

```python
age = 23
message = "Happy " + str(age) + "rd Birthday!"

print(message)
```

### 2.4.4 Python 2中的整数

在 Python 2 中,将两个整数相除得到的结果稍有不同：

```bash
>>> python2.7
>>> 3 / 2
1
```

在 Python 2 中,若要避免这种情况,务必确保至少有一个操作数为浮点数,这样结果也将为浮点数:

```bash
>>> 3 / 2
1
>>> 3.0 / 2
1.5
>>> 3 / 2.0
1.5
>>> 3.0 / 2.0
1.5
```



***

**动手试一试**

**2-8 数字8：** 编写 4 个表达式,它们分别使用加法、减法、乘法和除法运算,但结果都是数字 8 。为使用 print 语句来显示结果,务必将这些表达式用括号括起来,也就是说,你应该编写 4 行类似于下面的代码:

```python
print(5 + 3)
```

​	[number8.py]()

**2-9 最喜欢的数字：** 将你最喜欢的数字存储在一个变量中,再使用这个变量创建一条消息,指出你最喜欢的数字,然后将这条消息打印出来。

​	[favourite_number.py]()



## 2.5 注释

在 Python 中,注释用井号( # )标识。井号后面的内容都会被 Python 解释器忽略。



## 2.6 Python 之禅

```bash
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>>
```



## 2.7 小结

如何使用变量；

字符串是什么,以及如何使用小写、大写和首字母大写方式显示字符串;

如何使用整数和浮点数;