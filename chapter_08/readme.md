# 第8章	函数



**定义函数**

例子：

```python
❶ def greet_user():
❷ 	""" 显示简单的问候语 """
❸ 	print("Hello!")

❹ greet_user()
```

❶处的代码行使用关键字 **def** 来告诉 Python 你要定义一个函数。

❷处的文本是被称为**文档字符串** ( docstring )的注释,描述了函数是做什么的。

❸是函数体内的唯一一行代码

❹函数调用 让 Python 执行函数的代码。



**想函数传递信息**

例子：

```python
def greet_user(username): # username是一个形参
	""" 显示简单的问候语 """
	print("Hello, " + username.title() + "!")
    
greet_user('jesse') # 'jesse'是一个实参
```

输出：

```
Hello, Jesse!
```



***

**动手试一试**

**8-1 消息 :** 编写一个名为 display_message() 的函数,它打印一个句子,指出你在本章学的是什么。调用这个函数,确认显示的消息正确无误。

​	[8-1.py]()

**8-2 喜欢的图书 :** 编写一个名为 favorite_book() 的函数,其中包含一个名为 title 的形参。这个函数打印一条消息,如 One of my favorite books is Alice in Wonderland 。调用这个函数,并将一本图书的名称作为实参传递给它。

​	[8-2.py]()

***





**传递实参：** 



**位置实参**

最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参 。

例子：

```python
def describe_pet(animal_type, pet_name):
	""" 显示宠物的信息 """
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
 
describe_pet('hamster', 'harry')
```

输出：

```bash
I have a hamster.
My hamster's name is Harry.
```



**关键字实参**

关键字实参 是传递给函数的名称 — 值对。

例子：

```python
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
```

两个函数调用是等效的。



**默认值**

编写函数时,可给每个形参指定默认值 。

在调用函数中给形参提供了实参时, Python 将使用指定的实参值;否则,将使用形参的默认值。

例子：

```python
def describe_pet(pet_name, animal_type='dog'):
	""" 显示宠物的信息 """
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(pet_name='willie')
```

输出：

```bash
I have a dog.
My dog's name is Willie.
```

**注意**	使用默认值时,在形参列表中必须先列出没有默认值的形参,再列出有默认值的实参。这让 Python 依然能够正确地解读位置实参。



***

**动手试一试**

**8-3 T 恤 :** 编写一个名为 make_shirt() 的函数,它接受一个尺码以及要印到 T 恤上的字样。这个函数应打印一个句子,概要地说明 T 恤的尺码和字样。使用位置实参调用这个函数来制作一件 T 恤;再使用关键字实参来调用这个函数。

​	[8-3.py]()

**8-4 大号 T 恤 :** 修改函数 make_shirt() ,使其在默认情况下制作一件印有字样 “I love Python” 的大号 T 恤。调用这个函数来制作如下 T 恤:一件印有默认字样的大号 T恤、一件印有默认字样的中号 T 恤和一件印有其他字样的 T 恤(尺码无关紧要)。

​	[8-4.py]()

**8-5 城市 :** 编写一个名为 describe_city() 的函数,它接受一座城市的名字以及该城市所属的国家。这个函数应打印一个简单的句子,如 Reykjavik is in Iceland 。给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数,且其中至少有一座城市不属于默认国家。

​	[8-5.py]()

***





**返回值**

函数并非总是直接显示输出,相反,它可以处理一些数据,并返回一个或一组值。

在函数中,可使用 return 语句将值返回到调用函数的代码行。

例子：

```python
def get_formatted_name(first_name, last_name):
	""" 返回整洁的姓名 """
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```



**返回字典**

函数可返回任何类型的值,包括列表和字典等较复杂的数据结构。

```python
def build_person(first_name, last_name):
	""" 返回一个字典,其中包含有关一个人的信息 """
	person = {'first': first_name, 'last': last_name}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)
```

输出：

```bash
{'first': 'jimi', 'last': 'hendrix'}
```



***

**动手试一试**

**8-6 城市名 :** 编写一个名为 city_country() 的函数,它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面这样的字符串:

```
"Santiago, Chile"
```

至少使用三个城市 - 国家对调用这个函数,并打印它返回的值。

​	[8-6.py]()

**8-7 专辑 :** 编写一个名为 make_album() 的函数,它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名,并返回一个包含这两项信息的字典。使用这个函数创建三个表示不同专辑的字典,并打印每个返回的值,以核实字典正确地存储了专辑的信息。

给函数 make_album() 添加一个可选形参,以便能够存储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数,就将这个值添加到表示专辑的字典中。调用这个函数,并至少在一次调用中指定专辑包含的歌曲数。

​	[8-7.py]()

**8-8 用户的专辑 :** 在为完成练习 8-7 编写的程序中,编写一个 while 循环,让用户输入一个专辑的歌手和名称。获取这些信息后,使用它们来调用函数 make_album() ,并将创建的字典打印出来。在这个 while 循环中,务必要提供退出途径。

​	[8-8.py]()

***



**传递列表**

例子：

```python
def greet_users(names):
	""" 向列表中的每位用户都发出简单的问候 """
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
        
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

输出：

```bash
Hello, Hannah!
Hello, Ty!
Hello, Margot!
```



**在函数中修改列表**

将列表传递给函数后,函数就可对其进行修改。

例子：

```python
def print_models(unprinted_designs, completed_models):
	"""
	模拟打印每个设计,直到没有未打印的设计为止
	打印每个设计后,都将其移到列表 completed_models 中
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
        
		# 模拟根据设计制作 3D 打印模型的过程
		print("Printing model: " + current_design)
		completed_models.append(current_design)
        
def show_completed_models(completed_models):
	""" 显示打印好的所有模型 """
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)
        
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```



**禁止函数修改列表**

有时候,需要禁止函数修改列表。

为解决这个问题,可向函数传递列表的副本而不是原件;这样函数所做的任何修改都只影响副本,而丝毫不影响原件。

例子：

```python
# function_name(list_name[:])
print_models(unprinted_designs[:], completed_models)
```

切片表示法 [:] 创建列表的副本。



***

**动手试一试**

**8-9 魔术师 :** 创建一个包含魔术师名字的列表,并将其传递给一个名为 show_magicians() 的函数,这个函数打印列表中每个魔术师的名字。

​	[8-9.py]()

**8-10 了不起的魔术师 :** 在你为完成练习 8-9 而编写的程序中,编写一个名为 make_great() 的函数,对魔术师列表进行修改,在每个魔术师的名字中都加入字样 “the Great” 。调用函数 show_magicians() ,确认魔术师列表确实变了。

​	[8-10.py]()

**8-11 不变的魔术师 :** 修改你为完成练习 8-10 而编写的程序,在调用函数 make_great() 时,向它传递魔术师列表的副本。由于不想修改原始列表,请返回修改后的列表,并将其存储到另一个列表中。分别使用这两个列表来调用 show_magicians() ,确认一个列表包含的是原来的魔术师名字,而另一个列表包含的是添加了字样 “the Great” 的魔术师名字。

​	[8-11.py]()

***





**传递任意数量的实参**

有时候,你预先不知道函数需要接受多少个实参,好在 Python 允许函数从调用语句中收集任意数量的实参。

例子：

```python
def make_pizza(*toppings):
	""" 打印顾客点的所有配料 """
	print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

形参名 *toppings 中的星号让 Python 创建一个名为 toppings 的空元组,并将收到的所有值都封装到这个元组中。

输出：

```
('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')
```



**结合使用位置实参和任意数量实参**

如果要让函数接受不同类型的实参,必须在函数定义中将接纳任意数量实参的形参放在最后。 Python 先匹配位置实参和关键字实参,再将余下的实参都收集到最后一个形参中。

例子：

```python
def make_pizza(size, *toppings):
	""" 概述要制作的比萨 """
	print("\nMaking a " + str(size) +
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
        
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

输出：

```
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```



**使用任意数量的关键字实参**

有时候,需要接受任意数量的实参,但预先不知道传递给函数的会是什么样的信息。在这种情况下,可将函数编写成能够接受任意数量的键 — 值对。

例子：

```python
def build_profile(first, last, **user_info):
	""" 创建一个字典,其中包含我们知道的有关用户的一切 """
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein',
								location='princeton',
								field='physics')
print(user_profile)
```

形参 **user_info 中的两个星号让 Python 创建一个名为 user_info 的空字典,并将收到的所有名称 — 值对都封装到这个字典中。

输出：

```
{'first_name': 'albert', 'last_name': 'einstein',
'location': 'princeton', 'field': 'physics'}
```



***

**动手试一试**

**8-12 三明治 :** 编写一个函数,它接受顾客要在三明治中添加的一系列食材。这个函数只有一个形参(它收集函数调用中提供的所有食材),并打印一条消息,对顾客点的三明治进行概述。调用这个函数三次,每次都提供不同数量的实参。

​	[8-12.py]()

**8-13 用户简介 :** 复制前面的程序 user_profile.py ,在其中调用 build_profile() 来创建有关你的简介;调用这个函数时,指定你的名和姓,以及三个描述你的键 - 值对。

​	[8-13.py]()

**8-14 汽车 :** 编写一个函数,将一辆汽车的信息存储在一个字典中。这个函数总是接受制造商和型号,还接受任意数量的关键字实参。这样调用这个函数:提供必不可少的信息,以及两个名称 — 值对,如颜色和选装配件。这个函数必须能够像下面这样进行调用:

```python
car = make_car('subaru', 'outback', color='blue', tow_package=True)
```

​	[8-14.py]()

***



**将函数存储在模块中**

函数的优点之一是,使用它们可将代码块与主程序分离。通过给函数指定描述性名称,可让主程序容易理解得多。还可以更进一步,将函数存储在被称为模块 的独立文件中,再将模块导入 到主程序中。 import 语句允许在当前运行的程序文件中使用模块中的代码。



**导入整个模块**

要让函数是可导入的,得先创建模块。模块 是扩展名为 .py 的文件,包含要导入到程序中的代码。

例子：

下面来创建一个包含函数 make_pizza() 的模块。

*pizza.py*

```python
def make_pizza(size, *toppings):
	""" 概述要制作的比萨 """
	print("\nMaking a " + str(size) +
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
```

接下来,我们在 pizza.py 所在的目录中创建另一个名为 making_pizzas.py 的文件,这个文件导入刚创建的模块,再调用 make_pizza() 两次:

*makeing_pizzas.py*

```python
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

Python 读取这个文件时,代码行 import pizza 让 Python 打开文件 pizza.py ,并将其中的所有函数都复制到这个程序中。

要调用被导入的模块中的函数,可指定导入的模块的名称 pizza 和函数名 make_pizza() ,并用句点分隔它们

输出：

```
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```



**导入特定的函数**

还可以导入模块中的特定函数,这种导入方法的语法如下:

```python
from module_name import function_name
```

通过用逗号分隔函数名,可根据需要从模块中导入任意数量的函数:

```python
from module_name import function_0, function_1, function_2
```

例子：

```python
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

若使用这种语法,调用函数时就无需使用句点。由于我们在 import 语句中显式地导入了函数 make_pizza() ,因此调用它时只需指定其名称。



**使用 as 给函数指定别名**

如果要导入的函数的名称可能与程序中现有的名称冲突,或者函数的名称太长,可指定简短而独一无二的别名 —— 函数的另一个名称,类似于外号。

例子：

```python
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```

上面的 import 语句将函数 make_pizza() 重命名为 mp() ;在这个程序中,每当需要调用 make_pizza() 时,都可简写成 mp() ,而 Python 将运行 make_pizza() 中的代码,这可避免与这个程序可能包含的函数 make_pizza() 混淆。

指定别名的通用语法如下:

```python
from module_name import function_name as fn
```



**使用 as 给模块指定别名**

还可以给模块指定别名。

例子：

```python
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

给模块指定别名的通用语法如下:

```python
import module_name as mn
```



**导入模块中的所有函数**

使用星号( * )运算符可让 Python 导入模块中的所有函数:

例子：

```python
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

import 语句中的星号让 Python 将模块 pizza 中的每个函数都复制到这个程序文件中。由于导入了每个函数,可通过名称来调用每个函数,而无需使用句点表示法。然而,使用并非自己编写的大型模块时,最好不要采用这种导入方法:如果模块中有函数的名称与你的项目中使用的名称相同,可能导致意想不到的结果: Python 可能遇到多个名称相同的函数或变量,进而覆盖函数,而不是分别导入所有的函数。