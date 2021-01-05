# 第5章	if 语句

编程时经常需要检查一系列条件,并据此决定采取什么措施。

本章主要是了解语法的使用，然后完成课后习题。

## 5.1 一个简单示例

下面是一个简短的示例,演示了如何使用 if 语句来正确地处理特殊情形。

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
```

这个示例中的循环首先检查当前的汽车名是否是 'bmw'。如果是,就以全大写的方式打印它;否则就以首字母大写的方式打印:

```bash
Audi
BMW
Subaru
Toyota
```



### 5.2.5 检查多个条件

**1. 使用 and 检查多个条件**

要检查是否两个条件都为 True ,可使用关键字 and 将两个条件测试合而为一;如果每个测试都通过了,整个表达式就为 True ;如果至少有一个测试没有通过,整个表达式就为 False 。

```python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 21
False
>>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
True
```

**2. 使用 or 检查多个条件**

关键字 or 也能够让你检查多个条件,但只要至少有一个条件满足,就能通过整个测试。

```python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21
True
>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False
```



### 5.2.6 检查特定值是否包含在列表中

要判断特定的值是否已包含在列表中,可使用关键字 in 。

```python
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepperoni' in requested_toppings
False
```

### 5.2.7 检查特定值是否不包含在列表中

有些时候,确定特定的值未包含在列表中很重要;在这种情况下,可使用关键字 not in 。

```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
```



***

**5-1 条件测试：** 编写一系列条件测试;将每个测试以及你对其结果的预测和实际结果都打印出来。你编写的代码应类似于下面这样:

```python
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
```

- 详细研究实际结果,直到你明白了它为何为 True 或 False 。
- 创建至少 10 个测试,且其中结果分别为 True 和 False 的测试都至少有 5 个。

​	[5-1.py]()

**5-2 更多的条件测试 :** 你并非只能创建 10 个测试。如果你想尝试做更多的比较,可再编写一些测试,并将它们加入到 conditional_tests.py 中。对于下面列出的各种测试,至少编写一个结果为 True 和 False 的测试。

- 检查两个字符串相等和不等。

- 使用函数 lower() 的测试。

- 检查两个数字相等、不等、大于、小于、大于等于和小于等于。

- 使用关键字 and 和 or 的测试。

- 测试特定的值是否包含在列表中。

- 测试特定的值是否未包含在列表中。

  [5-2.py]()



## 5.3 if 语句



### 5.3.1 简单的 if 语句

```python
if conditional_test:
	do something
```



### 5.3.2 if-else 语句

下面的代码在一个人够投票的年龄时显示与前面相同的消息,同时在这个人不够投票的年龄时也显示一条消息:

```python
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")
```



### 5.3.3 if-elif-else 结构

```python
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")
print("Your admission cost is $" + str(price) + ".")
```



### 5.3.4 使用多个 elif 代码块

```python
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5
    
print("Your admission cost is $" + str(price) + ".")
```



***

**5-3 外星人颜色 #1 :** 假设在游戏中刚射杀了一个外星人,请创建一个名为 alien_color 的变量,并将其设置为 'green' 、 'yellow' 或 'red' 。

- 编写一条 if 语句,检查外星人是否是绿色的;如果是,就打印一条消息,指出玩家获得了 5 个点。

- 编写这个程序的两个版本,在一个版本中上述测试通过了,而在另一个版本中未通过(未通过测试时没有输出)。

  [5-3.py]()

**5-4 外星人颜色 #2 :** 像练习 5-3 那样设置外星人的颜色,并编写一个 if-else 结构。

- 如果外星人是绿色的,就打印一条消息,指出玩家因射杀该外星人获得了 5 个点。

- 如果外星人不是绿色的,就打印一条消息,指出玩家获得了 10 个点。

- 编写这个程序的两个版本,在一个版本中执行 if 代码块,而在另一个版本中执行 else 代码块。

  [5-4.py]()

**5-5 外星人颜色 #3 :** 将练习 5-4 中的 if-else 结构改为 if-elif-else 结构。

- 如果外星人是绿色的,就打印一条消息,指出玩家获得了 5 个点。

- 如果外星人是黄色的,就打印一条消息,指出玩家获得了 10 个点。

- 如果外星人是红色的,就打印一条消息,指出玩家获得了 15 个点。

- 编写这个程序的三个版本,它们分别在外星人为绿色、黄色和红色时打印一条消息。

  [5-5.py]()

**5-6 人生的不同阶段 :** 设置变量 age 的值,再编写一个 if-elif-else 结构,根据 age 的值判断处于人生的哪个阶段。

- 如果一个人的年龄小于 2 岁,就打印一条消息,指出他是婴儿。

- 如果一个人的年龄为 2 (含)~ 4 岁,就打印一条消息,指出他正蹒跚学步。

- 如果一个人的年龄为 4 (含)~ 13 岁,就打印一条消息,指出他是儿童。

- 如果一个人的年龄为 13 (含)~ 20 岁,就打印一条消息,指出他是青少年。

- 如果一个人的年龄为 20 (含)~ 65 岁,就打印一条消息,指出他是成年人。

- 如果一个人的年龄超过 65 (含)岁,就打印一条消息,指出他是老年人。

  [5-6.py]()

**5-7 喜欢的水果 :** 创建一个列表,其中包含你喜欢的水果,再编写一系列独立的 if 语句,检查列表中是否包含特定的水果。

- 将该列表命名为 favorite_fruits ,并在其中包含三种水果。

- 编写 5 条 if 语句,每条都检查某种水果是否包含在列表中,如果包含在列表中,就打印一条消息,如 “You really like bananas!” 。

  [5-7.py]()

**5-8 以特殊方式跟管理员打招呼 :** 创建一个至少包含 5 个用户名的列表,且其中一个用户名为 'admin' 。想象你要编写代码,在每位用户登录网站后都打印一条问候消息。遍历用户名列表,并向每位用户打印一条问候消息。

- 如果用户名为 'admin' ,就打印一条特殊的问候消息,如 “Hello admin, would you like to see a status report?” 。

- 否则,打印一条普通的问候消息,如 “Hello Eric, thank you for logging in again” 。

  [5-8.py]()

**5-9 处理没有用户的情形 :** 在为完成练习 5-8 编写的程序中,添加一条 if 语句,检查用户名列表是否为空。

- 如果为空,就打印消息 “We need to find some users!” 。

- 删除列表中的所有用户名,确定将打印正确的消息。

  [5-9.py]()

**5-10 检查用户名 :** 按下面的说明编写一个程序,模拟网站确保每位用户的用户名都独一无二的方式。

- 创建一个至少包含 5 个用户名的列表,并将其命名为 current_users 。

- 再创建一个包含 5 个用户名的列表,将其命名为 new_users ,并确保其中有一两个用户名也包含在列表 current_users 中。

- 遍历列表 new_users ,对于其中的每个用户名,都检查它是否已被使用。如果是这样,就打印一条消息,指出需要输入别的用户名;否则,打印一条消息,指出这个用户名未被使用。

- 确保比较时不区分大消息;换句话说,如果用户名 'John' 已被使用,应拒绝用户名 'JOHN' 。

  [5-10.py]()

**5-11 序数 :** 序数表示位置,如 1st 和 2nd 。大多数序数都以 th 结尾,只有 1 、 2 和 3 例外。

- 在一个列表中存储数字 1~9 。

- 遍历这个列表。

- 在循环中使用一个 if-elif-else 结构,以打印每个数字对应的序数。输出内容应为 1st 、 2nd 、 3rd 、 4th 、 5th 、 6th 、 7th 、 8th 和 9th ,但每个序数都独占一行。

  [5-11.py]()