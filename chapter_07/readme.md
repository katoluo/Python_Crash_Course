# 第7章	用户输入和while循环



**函数input()的工作原理**

函数 input() 让程序暂停运行,等待用户输入一些文本。

例子：

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

函数 input() 接受一个参数:即要向用户显示的提示 或说明,让用户知道该如何做。程序等待用户输入,并在用户按回车键后继续运行。输入存储在变量 message 中,接下来的 print(message) 将输入呈现给用户:

```bash
Tell me something, and I will repeat it back to you: Hello everyone!
Hello everyone!
```



**使用 int() 来获取数值输入**

使用函数 input() 时, Python 将用户输入解读为字符串。

```bash
>>> age = input("How old are you? ")
How old are you? 21
>>> age
'21'
```

如果我们只想打印输入,这一点问题都没有;但如果试图将输入作为数字使用,就会引发错误:

```bash
>>> age >= 18
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
TypeError: unorderable types: str() >= int()
```

**函数 int()** 将数字的字符串表示转换为数值表示,如下所示:

```bash
>>> age = input("How old are you? ")
How old are you? 21
>>> age = int(age)
>>> age >= 18
True
```



***

**动手试一试**

**7-1 汽车租赁 :** 编写一个程序,询问用户要租赁什么样的汽车,并打印一条消息,如 “Let me see if I can find you a Subaru” 。

​	[7-1.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_07/7-1.py)

**7-2 餐馆订位 :** 编写一个程序,询问用户有多少人用餐。如果超过 8 人,就打印一条消息,指出没有空桌;否则指出有空桌。

​	[7-2.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_07/7-2.py)

**7-3 10 的整数倍 :** 让用户输入一个数字,并指出这个数字是否是 10 的整数倍。

​	[7-3.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_07/7-3.py)

***





**while循环**

例子：

```python
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1
```



**让用户选择何时退出**

例子：

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)
    
	if message != 'quit':
		print(message)
```



**使用标志**

例子：

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	message = input(prompt)
    
	if message == 'quit':
		active = False
	else:
		print(message)
```



**使用break退出循环**

例子：

```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")
```



**在循环中使用continue**

例子：

```python
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
        
	print(current_number)
```



***

**动手试一试**

**7-4 比萨配料 :** 编写一个循环,提示用户输入一系列的比萨配料,并在用户输入 'quit' 时结束循环。每当用户输入一种配料后,都打印一条消息,说我们会在比萨中添加这种配料。

​		[7-4.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_07/7-4.py)

**7-5 电影票 :** 有家电影院根据观众的年龄收取不同的票价:不到 3 岁的观众免费; 3~12 岁的观众为 10 美元;超过 12 岁的观众为 15 美元。请编写一个循环,在其中询问用户的年龄,并指出其票价。

​		[7-5.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_07/7-5.py)

**7-6 三个出口 :** 以另一种方式完成练习 7-4 或练习 7-5 ,在程序中采取如下所有做法。

- 在 while 循环中使用条件测试来结束循环。

- 使用变量 active 来控制循环结束的时机。

- 使用 break 语句在用户输入 'quit' 时退出循环。

  [7-6.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_07/7-6.py)

**7-7 无限循环 : ** 编写一个没完没了的循环,并运行它(要结束该循环,可按 Ctrl +C ,也可关闭显示输出的窗口)。

​	[7-7.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_07/7-7.py)

***





**使用while循环来处理列表和字典**

for 循环是一种遍历列表的有效方式,但在 for 循环中不应修改列表,否则将导致 Python 难以跟踪其中的元素。

要在遍历列表的同时对其进行修改,可使用 while 循环。

例子：

```python
# 首先,创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户,直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
    
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)
    
# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
```

输出：

```bash
Verifying user: Candace
Verifying user: Brian
Verifying user: Alice

The following users have been confirmed:
Candace
Brian
Alice
```



**删除包含特定值的所有列表元素**

例子：

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
    
print(pets)
```

输出：

```bash
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']
```



**使用用户输入填充字典**

例子：

```python
responses = {}

# 设置一个标志,指出调查是否继续
polling_active = True

while polling_active:
	# 提示输入被调查者的名字和回答
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")
    
	# 将答卷存储在字典中
	responses[name] = response
    
	# 看看是否还有人要参与调查
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False
        
# 调查结束,显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
print(name + " would like to climb " + response + ".")
```

输出：

```bash
What is your name? Eric
Which mountain would you like to climb someday? Denali
Would you like to let another person respond? (yes/ no) yes

What is your name? Lynn
Which mountain would you like to climb someday? Devil's Thumb
Would you like to let another person respond? (yes/ no) no

--- Poll Results ---
Lynn would like to climb Devil's Thumb.
Eric would like to climb Denali.
```



***

**动手试一试**

**7-8 熟食店 :** 创建一个名为 sandwich_orders 的列表,在其中包含各种三明治的名字;再创建一个名为 finished_sandwiches 的空列表。遍历列表 sandwich_orders ,对于其中的每种三明治,都打印一条消息,如 I made your tuna sandwich ,并将其移到列表 finished_sandwiches 。所有三明治都制作好后,打印一条消息,将这些三明治列出来。

​	[7-8.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_07/7-8.py)

**7-9 五香烟熏牛肉( pastrami )卖完了 :** 使用为完成练习 7-8 而创建的列表 sandwich_orders ,并确保 'pastrami' 在其中至少出现了三次。在程序开头附近添加这样的代码:打印一条消息,指出熟食店的五香烟熏牛肉卖完了;再使用一个 while 循环将列表 sandwich_orders 中的 'pastrami' 都删除。确认最终的列表 finished_sandwiches 中不包含 'pastrami' 。

​	[7-9.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_07/7-9.py)

**7-10 梦想的度假胜地 :** 编写一个程序,调查用户梦想的度假胜地。使用类似于 “If you could visit one place in the world, where would you go?” 的提示,并编写一个打印调查结果的代码块。

​	[7-10.py](https://github.com/katoluo/Python_Crash_Course/blob/master/chapter_07/7-10.py)



