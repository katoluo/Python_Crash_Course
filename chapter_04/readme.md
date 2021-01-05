# 第 4 章	操作列表



## 4.1 遍历整个列表

使用 for 循环来打印魔术师名单中的所有名字:

```python
magicians = ['alice', 'david', 'carolina']
	for magician in magicians:
		print(magician)
```

输出很简单,就是列表中所有的姓名:

```bash
alice
david
carolina
```

### 4.1.1 深入地研究循环

对每个在列表中的元素都执行一次循环体中的代码，直到列表中的最后一个元素执行完毕之后，循环结束，执行下一行代码。缩进表示着属于循环体内的。



### 4.1.2 在 for 循环中执行更多的操作

在 for 循环中,想包含多少行代码都可以。每个缩进的代码行都是循环的一部分,且将针对列表中的每个值都执行一次。

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
```

```bash
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
```



### 4.1.3 在 for 循环结束后执行一些操作

在 for 循环后面,没有缩进的代码都只执行一次,而不会重复执行。



## 4.2 避免缩进错误

下面来看一些较为常见的缩进错误。



### 4.2.1 忘记缩进

对于位于 for 语句后面且属于循环组成部分的代码行,一定要缩进。如果你忘记缩进, Python 会提醒你:

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)
```

Python 没有找到期望缩进的代码块时,会让你知道哪行代码有问题。

```bash
File "magicians.py", line 3
	print(magician)
	^
IndentationError: expected an indented block
```



### 4.2.2 忘记缩进额外的代码行

例如,如果忘记缩进循环中的第 2 行代码(它告诉每位魔术师,我们期待他的下一次表演),就会出现这种情况:

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")
```

这是一个逻辑错误 。从语法上看,这些 Python 代码是合法的,但由于存在逻辑错误,结果并不符合预期。



### 4.2.3 不必要的缩进

不小心缩进了无需缩进的代码行, Python 将指出这一点:

```python
# hello_world.py
message = "Hello Python world!"
	print(message)
```

print 语句无需缩进,因为它并不属于前一行代码,因此 Python 将指出这种错误:

```bash
 File "hello_world.py", line 2
	print(message)
	^
IndentationError: unexpected indent
```



### 4.2.4 循环后不必要的缩进

例如,如果不小心缩进了感谢全体魔术师精彩表演的代码行,结果将如何呢?

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
	
    print("Thank you everyone, that was a great magic show!")
```

这也是一个逻辑错误,与 4.2.2 节的错误类似。 Python 不知道你的本意,只要代码符合语法,它就会运行。如果原本只应执行一次的操作执行了多次,请确定你是否不应该缩进执行该操作的代码。



### 4.2.5 遗漏了冒号

for 语句末尾的冒号告诉 Python ,下一行是循环的第一行。

如果你不小心遗漏了冒号，将导致语法错误,因为 Python 不知道你意欲何为。



***

**动手试一试**

**4-1 比萨：** 想出至少三种你喜欢的比萨,将其名称存储在一个列表中,再使用 for 循环将每种比萨的名称都打印出来。

- 修改这个 for 循环,使其打印包含比萨名称的句子,而不仅仅是比萨的名称。对于每种比萨,都显示一行输出,如 “I like pepperoni pizza” 。

- 在程序末尾添加一行代码,它不在 for 循环中,指出你有多喜欢比萨。输出应包含针对每种比萨的消息,还有一个总结性句子,如 “I really love pizza!” 。

  [pizza.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_04/pizza.py)

**4-2 动物：** 想出至少三种有共同特征的动物,将这些动物的名称存储在一个列表中,再使用 for 循环将每种动物的名称都打印出来。

- 修改这个程序,使其针对每种动物都打印一个句子,如 “A dog would make a great pet” 。

- 在程序末尾添加一行代码,指出这些动物的共同之处,如打印诸如 “Any of these animals would make a great pet!” 这样的句子。

  [animal.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_04/animal.py)



## 4.3 创建数值列表

列表非常适合用于存储数字集合,而 Python 提供了很多工具,可帮助你高效地处理数字列表。

### 4.3.1 使用函数 range()

```python
# numbers.py
for value in range(1,5):
	print(value)
```

上述代码好像应该打印数字 1~5 ,但实际上它不会打印数字 5 :

```bash
1
2
3
4
```

在这个示例中, range() 只是打印数字 1~4 ,这是你在编程语言中经常看到的差一行为的结果。函数 range() 让 Python 从你指定的第一个值开始数,并在到达你指定的第二个值后停止,因此输出不包含第二个值(这里为 5 )。



### 4.3.2 使用 range() 创建数字列表

要创建数字列表,可使用函数 list() 将 range() 的结果直接转换为列表。

```python
numbers = list(range(1,6))
print(numbers)
```

结果如下:

```bash
[1, 2, 3, 4, 5]
```

使用函数 range() 时,还可指定步长。例如,下面的代码打印 1~10 内的偶数:

```python
# even_numbers.py
even_numbers = list(range(2,11,2))
print(even_numbers)
```

在这个示例中,函数 range() 从 2 开始数,然后不断地加 2 ,直到达到或超过终值( 11 ),因此输出如下:

```bash
[2, 4, 6, 8, 10]
```

使用函数 range() 几乎能够创建任何需要的数字集,例如,如何创建一个列表,其中包含前 10 个整数(即 1~10 )的平方呢?在 Python 中,两个星号( ** )表示乘方运算。下面的代码演示了如何将前 10 个整数的平方加入到一个列表中:

```python
# squares.py
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)
```

打印列表 squares：

```bash
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```



### 4.3.3 对数字列表执行简单的统计计算

有几个专门用于处理数字列表的 Python 函数。例如,你可以轻松地找出数字列表的最大值、最小值和总和:

```bash
>>> digits = [1, 2, 3, 4, 5]
>>> min(digits)
1
>>> max(digits)
5
>>> sum(digits)
15
>>>
```



### 4.3.4 列表解析

前面介绍的生成列表 squares 的方式包含三四行代码,而列表解析让你只需编写一行代码就能生成这样的列表。**列表解析** 将 for 循环和创建新元素的代码合并成一行,并自动附加新元素。

下面的示例使用列表解析创建你在前面看到的平方数列表:

```python
# squares.py
squares = [value**2 for value in range(1,11)]
print(squares)
```

要使用这种语法,首先指定一个描述性的列表名,如 squares ;然后,指定一个左方括号,并定义一个表达式,用于生成你要存储到列表中的值。接下来,编写一个 for 循环,用于给表达式提供值,再加上右方括号。

结果与你在前面看到的平方数列表相同:

```bash
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```



***

**动手试一试**

**4-3 数到20：** 使用一个 for 循环打印数字 1~20 (含)。

​	[4-3.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_04/4-3.py)

**4-4 一百万：** 创建一个列表,其中包含数字 1~1 000 000 ,再使用一个 for 循环将这些数字打印出来(如果输出的时间太长,按 Ctrl + C 停止输出,或关闭输出窗口)。

​	[4-4.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_04/4-4.py)

**4-5 计算1～1000000的总和：** 创建一个列表,其中包含数字 1~1 000 000 ,再使用 min() 和 max() 核实该列表确实是从 1 开始,到 1 000 000 结束的。另外,对这个列表调用函数 sum() ,看看 Python 将一百万个数字相加需要多长时间。

​	[4-5.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_04/4-5.py)

**4-6 奇数：** 通过给函数 range() 指定第三个参数来创建一个列表,其中包含 1~20 的奇数;再使用一个 for 循环将这些数字都打印出来。

​	[4-6.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_04/4-6.py)

**4-7 3的倍数：** 创建一个列表,其中包含 3~30 内能被 3 整除的数字;再使用一个 for 循环将这个列表中的数字都打印出来。

​	[4-7.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_04/4-7.py)

**4-8 立方：** 将同一个数字乘三次称为立方。例如,在 Python 中, 2 的立方用 2**3 表示。请创建一个列表,其中包含前 10 个整数(即 1~10 )的立方,再使用一个 for 循环将这些立方数都打印出来。

​	[4-8.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_04/4-8.py)

**4-9 立方解析：** 使用列表解析生成一个列表,其中包含前 10 个整数的立方。

​	[4-8.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_04/4-8.py)



## 4.4 使用列表的一部分

在第 3 章中,学习了如何访问单个列表元素。在本章中,一直在学习如何处理列表的所有元素。还可以处理列表的部分元素 ——Python 称之为**切片** 。



#### 4.4.1 切片

要创建切片,可指定要使用的第一个元素和最后一个元素的**索引**。与函数 range() 一样, Python 在到达你指定的第二个索引前面的元素后停止。要输出列表中的前三个元素,需要指定索引 0~3 ,这将输出分别为 0 、 1 和 2 的元素。

下面的示例处理的是一个运动队成员列表:

```python
# players.py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
```

打印该列表的一个切片,其中只包含三名队员。输出也是一个列表,其中包含前三名队员:

```bash
['charles', 'martina', 'michael']
```

可以生成列表的任何子集,例如,如果你要提取列表的第 2~4 个元素,可将起始索引指定为 1 ,并将终止索引指定为 4 :

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
```

切片始于 'marita' ,终于 'florence' :

```bash
['martina', 'michael', 'florence']
```

如果你没有指定第一个索引, Python 将自动从列表开头开始:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
```

要让切片终止于列表末尾,也可使用类似的语法。例如,如果要提取从第 3 个元素到列表末尾的所有元素,可将起始索引指定为 2 ,并省略终止索引:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
```

本书前面说过,负数索引返回离列表末尾相应距离的元素,因此你可以输出列表末尾的任何切片。

例如,如果你要输出名单上的最后三名队员,可使用切片 players[-3:] :

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
```



### 4.4.2 遍历切片

如果要遍历列表的部分元素,可在 for 循环中使用切片。在下面的示例中,我们遍历前三名队员,并打印他们的名字:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
```

代码没有遍历整个队员列表,而只遍历前三名队员:

```bash
Here are the first three players on my team:
Charles
Martina
Michael
```



### 4.4.3 复制列表

这节讲的创建一个切片，从而创建了该列表的副本，然后在存储到别的变量，从而达成复制列表。有些疑惑是为何不直接将此列表直接赋值给别的变量。之后我取实验一下，得到结果是，这样的直接使用等号进行的赋值有点像C/C++那边的别名，把变量名绑定在存储内存上了。创建切片的话，应该是开辟一块内存来存储切片内容，然后使用等号赋值，这样就是两个不同的内存了。

要复制列表,可创建一个包含整个列表的切片,方法是同时省略起始索引和终止索引( [:] )。

```python
# foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
```

在不指定任何索引的情况下从列表 my_foods 中提取一个切片,从而创建了这个列表的副本,再将该副本存储到变量 friend_foods 中。



***

**4-10 切片：** 选择你在本章编写的一个程序,在末尾添加几行代码,以完成如下任务。

- 打印消息 “The first three items in the list are:” ,再使用切片来打印列表的前三个元素。

- 打印消息 “Three items from the middle of the list are:” ,再使用切片来打印列表中间的三个元素。

- 打印消息 “The last three items in the list are:” ,再使用切片来打印列表末尾的三个元素。

  [4-10.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_04/4-10.py)

**4-11 你的比萨和我的比萨：** 在你为完成练习 4-1 而编写的程序中,创建比萨列表的副本,并将其存储到变量 friend_pizzas 中,再完成如下任务。

- 在原来的比萨列表中添加一种比萨。

- 在列表 friend_pizzas 中添加另一种比萨。

- 核实你有两个不同的列表。为此,打印消息 “My favorite pizzas are:” ,再使用一个 for 循环来打印第一个列表;打印消息 “My friend's favorite pizzas are:” ,再使用一个 for 循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。

  [4-11.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_04/4-11.py)

**4-12 使用多个循环 :** 在本节中,为节省篇幅,程序 foods.py 的每个版本都没有使用 for 循环来打印列表。请选择一个版本的 foods.py ,在其中编写两个 for 循环,将各个食品列表都打印出来。

​	拒绝。



## 4.5 元组

有时候你需要创建一系列不可修改的元素,元组可以满足这种需求。 Python 将不能修改的值称为不可变的 ,而不可变的列表被称为**元组 **。

### 4.5.1 定义元组

元组看起来犹如列表,但使用圆括号而不是方括号来标识。

```python
# dimensions.py
dimensions = (200, 50)
print(dimensions[0]) # 200
print(dimensions[1]) # 50
```



### 4.5.2 遍历元组中的所有值

像列表一样,也可以使用 for 循环来遍历元组中的所有值:

```python
dimensions = (200, 50)
for dimension in dimensions:
print(dimension)
```



### 4.5.3 修改元组变量

虽然不能修改元组的元素,但可以给存储元组的变量赋值。

```python
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
```

给元组变量赋值是合法的。

相比于列表,元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都不变,可使用元组。

***

**动手试一试**

**4-13 自助餐 :** 有一家自助式餐馆,只提供五种简单的食品。请想出五种简单的食品,并将其存储在一个元组中。

- 用一个 for 循环将该餐馆提供的五种食品都打印出来。

- 尝试修改其中的一个元素,核实 Python 确实会拒绝你这样做。

- 餐馆调整了菜单,替换了它提供的其中两种食品。请编写一个这样的代码块:给元组变量赋值,并使用一个 for 循环将新元组的每个元素都打印出来。

  [4-13.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_04/4-13.py)