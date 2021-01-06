# 第六章 字典



记录一些需要着重记录的。



在 Python 中，**字典** 是一系列**键 — 值**对 。每个**键** 都与一个值相关联,你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何 Python 对象用作字典中的值。

例子：

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
```

输出：

```bash
green
5
```



字典是一种动态结构,可随时在其中**添加键 — 值对**。要添加键 — 值对,可依次指定字典名、用方括号括起的键和相关联的值。

例子：

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```

输出：

```bash
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}
```



**可先使用一对空的花括号定义一个字典,再分行添加各个键 — 值对。**

例子：

```python
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
```

输出：

```bash
{'color': 'green', 'points': 5}
```



**修改字典中的值**

要修改字典中的值,可依次指定字典名、用方括号括起的键以及与该键相关联的新值。

例子：

```python
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
```

输出：

```bash
The alien is green.
The alien is now yellow.
```





**删除键——值对**

可使用 del 语句将相应的键 — 值对彻底删除。

例子：

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
```

输出：

```bash
{'color': 'green', 'points': 5}
{'color': 'green'}
```



**由类似对象组成的字典**

例子：

```python
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

print("Sarah's favorite language is " +
	favorite_languages['sarah'].title() +
	".")
```



***

**动手试一试**

**6-1 人：** 使用一个字典来存储一个熟人的信息,包括名、姓、年龄和居住的城市。该字典应包含键 first_name 、 last_name 、 age 和 city 。将存储在该字典中的每项信息都打印出来。

​	[6-1.py]()

**6-2 喜欢的数字：** 使用一个字典来存储一些人喜欢的数字。请想出 5 个人的名字,并将这些名字用作字典中的键;想出每个人喜欢的一个数字,并将这些数字作为值存储在字典中。打印每个人的名字和喜欢的数字。为让这个程序更有趣,通过询问朋友确保数据是真实的。

​	[6-2.py]()

**6-3 词汇表 :** Python 字典可用于模拟现实生活中的字典,但为避免混淆,我们将后者称为词汇表。

- 想出你在前面学过的 5 个编程词汇,将它们用作词汇表中的键,并将它们的含义作为值存储在词汇表中。

- 以整洁的方式打印每个词汇及其含义。为此,你可以先打印词汇,在它后面加上一个冒号,再打印词汇的含义;也可在一行打印词汇,再使用换行符( \n )插入一个空行,然后在下一行以缩进的方式打印词汇的含义。

  [6-3.py]()

***





**遍历字典的所有键值对**

声明两个变量,用于存储键 — 值对中的键和值。字典名和方法 items()，它返回一个键 — 值对列表。

例子：

```python
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
	print("Value: " + value)
```

输出：

```bash
Key: last
Value: fermi

Key: first
Value: enrico

Key: username
Value: efermi
```

注意,即便遍历字典时,键 — 值对的返回顺序也与存储顺序不同。 Python 不关心键 — 值对的存储顺序,而只跟踪键和值之间的关联关系。



**遍历字典中的所有键**

在不需要使用字典中的值时,方法 keys() 很有用。

例子：

```python
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

for name in favorite_languages.keys():
	print(name.title())
```

输出：

```bash
Jen
Sarah
Phil
Edward
```

遍历字典时,会默认遍历所有的键,因此,如果将上述代码中的 `for name in favorite_languages.keys():` 替换为 `for name in favorite_languages: `,输出
将不变。



**遍历字典中的所有值**

可使用方法 values() ,它返回一个值列表,而不包含任何键。

例子：

```python
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
```

输出：

```bash
The following languages have been mentioned:
Python
C
Python
Ruby
```



**集合**

为剔除重复项,可使用集合( set )。集合 类似于列表,但每个元素都必须是独一无二的:

例子：

```python
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
```

通过对包含重复元素的列表调用 set() ,可让 Python 找出列表中独一无二的元素,并使用这些元素来创建一个集合。我们使用了 set() 来提取 favorite_languages.values() 中不同的语言。

```bash
The following languages have been mentioned:
Python
C
Ruby
```



***

**动手试一试**

**6-4 词汇表 2 :** 既然你知道了如何遍历字典,现在请整理你为完成练习 6-3 而编写的代码,将其中的一系列 print 语句替换为一个遍历字典中的键和值的循环。确定该循环正确无误后,再在词汇表中添加 5 个 Python 术语。当你再次运行这个程序时,这些新术语及其含义将自动包含在输出中。

​	[6-4.py]()

**6-5 河流 :** 创建一个字典,在其中存储三条大河流及其流经的国家。其中一个键 — 值对可能是 'nile': 'egypt' 。

- 使用循环为每条河流打印一条消息,如 “The Nile runs through Egypt.” 。

- 使用循环将该字典中每条河流的名字都打印出来。

- 使用循环将该字典包含的每个国家的名字都打印出来。

  [6-5.py]()

**6-6 调查：** 在 6.3.1 节编写的程序 favorite_languages.py 中执行以下操作。

- 创建一个应该会接受调查的人员名单,其中有些人已包含在字典中,而其他人未包含在字典中。

- 遍历这个人员名单,对于已参与调查的人,打印一条消息表示感谢。对于还未参与调查的人,打印一条消息邀请他参与调查。

  [6-6.py]()

***





**嵌套**

有时候,需要将一系列字典存储在列表中,或将列表作为值存储在字典中,这称为嵌套 。

嵌套是一项强大的功能。



**字典列表：**

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)
```

输出：

```bash
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
```





**在字典中存储列表**

例子：

```python
# 存储所点比萨的信息
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}

# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
```

输出：

```bash
You ordered a thick-crust pizza with the following toppings:
	mushrooms
	extra cheese
```

每当需要在字典中将一个键关联到多个值时,都可以在字典中嵌套一个列表。

例子：

```python
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())
```

输出：

```bash
Jen's favorite languages are:
	Python
	Ruby
Sarah's favorite languages are:
	C
Phil's favorite languages are:
	Python
	Haskell
Edward's favorite languages are:
	Ruby
	Go
```





**在字典中存储字典**

可在字典中嵌套字典,但这样做时,代码可能很快复杂起来。

例子：

```python
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
	},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
	},
}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
```

输出：

```bash
Username: aeinstein
	Full name: Albert Einstein
	Location: Princeton

Username: mcurie
	Full name: Marie Curie
	Location: Paris
```





***

**动手试一试**

**6-7 人 :** 在为完成练习 6-1 而编写的程序中,再创建两个表示人的字典,然后将这三个字典都存储在一个名为 people 的列表中。遍历这个列表,将其中每个人的所有信息都打印出来。

​	[6-7.py]()

**6-8 宠物 :** 创建多个字典,对于每个字典,都使用一个宠物的名称来给它命名;在每个字典中,包含宠物的类型及其主人的名字。将这些字典存储在一个名为 pets的列表中,再遍历该列表,并将宠物的所有信息都打印出来。

​	[6-8.py]()

**6-9 喜欢的地方 :** 创建一个名为 favorite_places 的字典。在这个字典中,将三个人的名字用作键;对于其中的每个人,都存储他喜欢的 1~3 个地方。为让这个练习更有趣些,可让一些朋友指出他们喜欢的几个地方。遍历这个字典,并将其中每个人的名字及其喜欢的地方打印出来。

​	[6-9.py]()

**6-10 喜欢的数字 :** 修改为完成练习 6-2 而编写的程序,让每个人都可以有多个喜欢的数字,然后将每个人的名字及其喜欢的数字打印出来。

​	[6-10.py]()

**6-11 城市 :** 创建一个名为 cities 的字典,其中将三个城市名用作键;对于每座城市,都创建一个字典,并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。在表示每座城市的字典中,应包含 country 、 population 和 fact 等键。将每座城市的名字以及有关它们的信息都打印出来。

​	[6-11.py]()

**6-12 扩展 :** 本章的示例足够复杂,可以以很多方式进行扩展了。请对本章的一个示例进行扩展:添加键和值、调整程序要解决的问题或改进输出的格式。

​	[6-12.py]()