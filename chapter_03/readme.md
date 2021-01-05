# 第3章	列表简介



## 3.1 列表是什么

**列表** 由一系列按特定顺序排列的元素组成。

在 Python 中,用方括号( [] )来表示列表,并用逗号来分隔其中的元素。

```python
# bicycles.py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```

运行，Python 将打印列表的内部表示，包括方括号：

```bash
['trek', 'cannondale', 'redline', 'specialized']
```



### 3.1.1 访问列表元素

列表是有序集合,因此要访问列表的任何元素,只需将该元素的位置或索引告诉 Python 即可。

例如,下面的代码从列表 bicycles 中提取第一款自行车：

```python
# Python只返回该元素,而不包括方括号和引号；
# 将打印trek
print(bicycles[0])
```

还可以对任何列表元素调用第 2 章介绍的字符串方法。

```python
print(bicycles[0].title())
```



### 3.1.2 索引从0而不是1开始

在 Python 中,第一个列表元素的索引为 0 ,而不是 1 。

访问索引 1 和 3 处的自行车:

```python
print(bicycles[1]) # 输出cannondale
print(bicycles[3]) # 输出specialized
```

Python 为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为 -1 ,可让 Python 返回最后一个列表元素:

```python
print(bicycles[-1])
```

这种约定也适用于其他负数索引,例如,索引 -2 返回倒数第二个列表元素,索引 -3 返回倒数第三个列表元素,以此类推。



### 3.1.3 使用列表中的各个值

可像使用其他变量一样使用列表中的各个值。

尝试从列表中提取第一款自行车,并使用这个值来创建一条消息:

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
# 输出： My first bicycle was a Trek.
```

***

**动手试一试**

请尝试编写一些简短的程序来完成下面的练习,以获得一些使用 Python 列表的第一手经验。你可能需要为每章的练习创建一个文件夹,以整洁有序的方式存储为完成各章的练习而编写的程序。

**3-1 姓名：** 将一些朋友的姓名存储在一个列表中,并将其命名为 names 。依次访问该列表中的每个元素,从而将每个朋友的姓名都打印出来。

​	[names.py]()

**3-2 问候语：** 继续使用练习 3-1 中的列表,但不打印每个朋友的姓名,而为每人打印一条消息。每条消息都包含相同的问候语,但开头为相应朋友的姓名。

​	[greetings.py]()

**3-3 自己的列表：** 想想你喜欢的通勤方式,如骑摩托车或开汽车,并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言,如 “I would like to own a Honda motorcycle” 。

​	[own_list.py]()



## 3.2 修改、添加和删除元素

创建的大多数列表都将是动态的,这意味着列表创建后,将随着程序的运行增删元素。

### 3.2.1 修改列表元素

motorcycles.py：

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
```

运行输出：

```bash
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']
```

可以修改任何列表元素的值,而不仅仅是第一个元素的值。



### 3.2.2 在列表中添加元素

可能出于众多原因要在列表中添加新元素。

#### 1. 在列表末尾添加元素

在列表中添加新元素时,最简单的方式是将元素附加到列表末尾：

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
```

方法 append() 将元素 'ducati' 添加到了列表末尾：

```bash
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']
```

方法 append() 让动态地创建列表：

```python
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
```

最终的列表与前述示例中的列表完全相同：

```bash
['honda', 'yamaha', 'suzuki']
```



#### 2. 在列表中插入元素

使用方法 insert() 可在列表的任何位置添加新元素：

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') # 指定新元素的索引和值。
print(motorcycles)
```

方法 insert() 在索引 0 处添加空间,并将值 'ducati' 存储到这个地方。这种操作将列表中既有的每个元素都右移一个位置：

```bash
['ducati', 'honda', 'yamaha', 'suzuki']
```



### 3.2.3 从列表中删除元素

从列表中删除一个或多个元素。

#### 1. 使用del语句删除元素

如果知道要删除的元素在列表中的位置,可使用 del 语句。

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
```

使用 del 删除了列表 motorcycles 中的第一个元素 —— 'honda' ：

```python
['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']
```

如何删除前述列表中的第二个元素 —— 'yamaha' ：

```python
del motorcycles[1]
print(motorcycles)
```



#### 2. 使用方法 pop() 删除元素

有时候,你要将元素从列表中删除,并接着使用它的值。

方法 pop() 可删除列表末尾的元素,并让你能够接着使用它：

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
```

输出表明,列表末尾的值 'suzuki' 已删除,它现在存储在变量 popped_motorcycle 中:

```bash
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki
```



#### 3. 弹出列表中任何位置处的元素

可以使用 pop() 来删除列表中任何位置的元素,只需在括号中指定要删除的元素的索引即可。

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
```

输出是一个简单的句子,描述了我购买的第一辆摩托车:

```bash
The first motorcycle I owned was a Honda.
```

如果你要从列表中删除一个元素,且不再以任何方式使用它,就使用 del 语句;如果你要在删除元素后还能继续使用它,就使用方法 pop() 。



#### 4. 根据值删除元素

有时候,你不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值,可使用方法 remove() 。

从列表 motorcycles 中删除值 'ducati' 。

```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
```

确定 'ducati' 出现在列表的什么地方,并将该元素删除：

```bash
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']
```

**注意：** 方法 remove() 只删除第一个指定的值。如果要删除的值可能在列表中出现多次,就需要使用循环来判断是否删除了所有这样的值。



***

**动手试一试**

下面的练习比第 2 章的练习要复杂些,但让你有机会以前面介绍过的各种方式使用列表。

**3-4 嘉宾名单：** 

​	[guest_list.py]()

**3-5 修改嘉宾名单：** 

​	[change_list.py]()

**3-6 添加嘉宾：**

​	[add_guest.py]()

**3-7 缩减名单：** 

​	[del_list.py]()



## 3.3 组织列表

Python 提供了很多组织列表的方式,可根据具体情况选用。

### 3.3.1 使用方法 sort() 对列表进行永久性排序

Python 方法 sort() 让你能够较为轻松地对列表进行排序。

```python
# cars.py
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
```

现在,汽车是按字母顺序排列的,再也无法恢复到原来的排列顺序:

```bash
['audi', 'bmw', 'subaru', 'toyota']
```

还可以按与字母顺序相反的顺序排列列表元素,为此,只需向 sort() 方法传递参数 reverse=True 。

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
```

同样,对列表元素排列顺序的修改是永久性的:

```bash
['toyota', 'subaru', 'bmw', 'audi']
```



### 3.3.2 使用函数 sorted() 对列表进行临时排序

要保留列表元素原来的排列顺序,同时以特定的顺序呈现它们,可使用函数 sorted() 。

尝试对汽车列表调用这个函数。

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
```

```bash
Here is the original list:
['bmw', 'audi', 'toyota', 'subaru']

Here is the sorted list:
['audi', 'bmw', 'subaru', 'toyota']

Here is the original list again:
['bmw', 'audi', 'toyota', 'subaru']
```

注意,调用函数 sorted() 后,列表元素的排列顺序并没有变。如果你要按与字母顺序相反的顺序显示列表,也可向函数 sorted() 传递参数 reverse=True 。

在并非所有的值都是小写时,按字母顺序排列列表要复杂些。决定排列顺序时,有多种解读大写字母的方式,要指定准确的排列顺序,可能比我们这里所做的要复杂。



### 3.3.3 倒着打印列表

要反转列表元素的排列顺序,可使用方法 reverse() 。

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
```

注意, reverse() 不是指按与字母顺序相反的顺序排列列表元素,而只是反转列表元素的排列顺序:

```bash
['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']
```

方法 reverse() 永久性地修改列表元素的排列顺序,但可随时恢复到原来的排列顺序,为此只需对列表再次调用 reverse() 即可。



### 3.3.4 确定列表的长度

函数 len() 可快速获悉列表的长度。

```bash
>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> len(cars)
4
```



***

**动手试一试**

**3-8 放眼世界：** 

​	[3-8.py]()

**3-9 晚餐嘉宾：**

​	[3-9.py]()

**3-10 尝试使用各个函数：** 

​	[3-10.py]()



## 3.4 使用列表时避免索引错误

刚开始使用列表时,经常会遇到一种错误。

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])
```

这将导致**索引错误 :**

```bash
Traceback (most recent call last):
	File "motorcycles.py", line 3, in <module>
		print(motorcycles[3])
IndexError: list index out of range
```



