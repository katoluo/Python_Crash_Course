# 第9章	类



根据类来创建对象被称为**实例化** ,这让你能够使用类的实例。

**创建和使用类**



例子：

**创建Dog类**

根据 Dog 类创建的每个实例都将存储名字和年龄。我们赋予了每条小狗蹲下( sit() )和打滚( roll_over() )的能力:

```python
❶class Dog():
❷	""" 一次模拟小狗的简单尝试 """
    
❸	def __init__(self, name, age):
		""" 初始化属性 name 和 age"""
❹		self.name = name
		self.age = age
        
❺	def sit(self):
		""" 模拟小狗被命令时蹲下 """
		print(self.name.title() + " is now sitting.")
        
	def roll_over(self):
		""" 模拟小狗被命令时打滚 """
		print(self.name.title() + " rolled over!")
```

在❶处,我们定义了一个名为 Dog 的类。

在❷处,我们编写了一个文档字符串,对这个类的功能作了描述。

在❸处的方法 \_\_init\_\_() 是一个特殊的方法,每当你根据 Dog 类创建新实例时, Python 都会自动运行它。在这个方法的名称中,开头和末尾各有两个下划线,这是一种约定,旨在避免 Python 默认方法与普通方法发生名称冲突。

在这个方法的定义中,形参 self 必不可少,还必须位于其他形参的前面。为何必须在方法定义中包含形参 self 呢?因为 Python 调用这个方法来创建 Dog 实例时,将自动传入实参 self 。每个与类相关联的方法调用都自动传递实参 self ,它是一个指向实例本身的引用,让实例能够访问类中的属性和方法。每当我们根据 Dog 类创建实例时,都只需给最后两个形参( name 和 age )提供值。

在❹处定义的两个变量都有前缀 self 。以 self 为前缀的变量都可供类中的所有方法使用,我们还可以通过类的任何实例来访问这些变量。 self.name = name 获取存储在形参 name 中的值,并将其存储到变量 name 中,然后该变量被关联到当前创建的实例。 self.age = age 的作用与此类似。像这样可通过实例访问的变量称为**属性 **。

在❺处还定义了另外两个方法: sit() 和 roll_over()。由于这些方法不需要额外的信息,如名字或年龄,因此它们只有一个形参 self 。



**根据类创建示例**

例子：

**访问属性**

```python
❶ my_dog = Dog('willie', 6)

❷ print("My dog's name is " + my_dog.name.title() + ".")
❸ print("My dog is " + str(my_dog.age) + " years old.")
```

在❶处,Python 使用实参 'willie' 和 6 调用 Dog 类中的方法 \_\_init\_\_() ，创建一个表示特定小狗的示例,并使用我们提供的值来设置属性 name 和 age 。未显式地包含 return 语句,但 Python 自动返回一个表示这条小狗的实例。

在❷处,要访问实例的属性,可使用句点表示法。

在❸处,我们使用同样的方法来获取属性 age 的值。

输出：

```
My dog's name is Willie.
My dog is 6 years old.
```



**调用方法**

根据 Dog 类创建实例后,就可以使用句点表示法来调用 Dog 类中定义的任何方法。

例子：

```python
my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()
```

输出：

```
Willie is now sitting.
Willie rolled over!
```



***

**动手试一试**

**9-1 餐馆 :** 创建一个名为 Restaurant 的类,其方法 __init__() 设置两个属性: restaurant_name 和 cuisine_type 。创建一个名为 describe_restaurant() 的方法和一个名为 open_restaurant() 的方法,其中前者打印前述两项信息,而后者打印一条消息,指出餐馆正在营业。

根据这个类创建一个名为 restaurant 的实例,分别打印其两个属性,再调用前述两个方法。

​	[9-1.py]()

**9-2 三家餐馆 :** 根据你为完成练习 9-1 而编写的类创建三个实例,并对每个实例调用方法 describe_restaurant() 。

​	[9-2.py]()

**9-3 用户 :** 创建一个名为 User 的类,其中包含属性 first_name 和 last_name ,还有用户简介通常会存储的其他几个属性。在类 User 中定义一个名为 describe_user() 的方法,它打印用户信息摘要;再定义一个名为 greet_user() 的方法,它向用户发出个性化的问候。

创建多个表示不同用户的实例,并对每个实例都调用上述两个方法。

​	[9-3.py]()

**9-4 就餐人数 :** 在为完成练习 9-1 而编写的程序中,添加一个名为 number_served 的属性,并将其默认值设置为 0 。根据这个类创建一个名为 restaurant 的实例;打印有多少人在这家餐馆就餐过,然后修改这个值并再次打印它。

添加一个名为 set_number_served() 的方法,它让你能够设置就餐人数。调用这个方法并向它传递一个值,然后再次打印这个值。

添加一个名为 increment_number_served() 的方法,它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值:你认为这家餐馆每天可能接待的就餐人数。

​	[9-4.py]()

**9-5 尝试登录次数 :** 在为完成练习 9-3 而编写的 User 类中,添加一个名为 login_attempts 的属性。编写一个名为 increment_login_attempts() 的方法,它将属性 login_attempts 的值加 1 。再编写一个名为 reset_login_attempts() 的方法,它将属性 login_attempts 的值重置为 0 。

根据 User 类创建一个实例,再调用方法 increment_login_attempts() 多次。打印属性 login_attempts 的值,确认它被正确地递增;然后,调用方法 reset_login_attempts() ,并再次打印属性 login_attempts 的值,确认它被重置为 0 。

​	[9-5.py]()

***



**继承**

编写类时,并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本,可使用**继承** 。

一个类继承 另一个类时,它将自动获得另一个类的所有属性和方法;

原有的类称为父类 ,而新类称为子类 。子类继承了其父类的所有属性和方法,同时还可以定义自己的属性和方法。

例子：

下面来创建一个简单的 ElectricCar 类版本,它具备 Car 类的所有功能:

```python
❶ class Car():
	""" 一次模拟汽车的简单尝试 """
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
        
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
    
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
            
	def increment_odometer(self, miles):
		self.odometer_reading += miles
        
❷ class ElectricCar(Car):
	""" 电动汽车的独特之处 """
    
❸	def __init__(self, make, model, year):
	""" 初始化父类的属性 """
❹		super().__init__(make, model, year)
        
❺my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
```

❶: 创建子类时,父类必须包含在当前文件中,且位于子类前面。

❷: 定义了子类 ElectricCar 。定义子类时,必须在括号内指定父类的名称。

❸: 方法 \_\_init\_\_() 接受创建 Car 实例所需的信息。

❹: super() 是一个特殊函数,帮助 Python 将父类和子类关联起来。这行代码让 Python 调用 ElectricCar 的父类的方法 \_\_init\_\_() ,让 ElectricCar 实例包含父类的所有属性。父类也称为超类 ( superclass ),名称 super 因此而得名。

❺: 创建 ElectricCar 类的一个实例,并将其存储在变量 my_tesla 中。



**给子类定义属性和方法**

让一个类继承另一个类后,可添加区分子类和父类所需的新属性和方法。

例子：

```python
class Car():
	--snip--
    
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
	"""
	电动汽车的独特之处
	初始化父类的属性,再初始化电动汽车特有的属性
	"""
		super().__init__(make, model, year)
❶		self.battery_size = 70
        
❷	def describe_battery(self):
		""" 打印一条描述电瓶容量的消息 """
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

❶: 添加了新属性 self.battery_size ,并设置其初始值(如 70 )。根据 ElectricCar 类创建的所有实例都将包含这个属性,但所有 Car 实例都不包含它。

❷: 添加了一个名为 describe_battery() 的方法,它打印有关电瓶的信息。

输出：

```
2016 Tesla Model S
This car has a 70-kWh battery.
```



**重写父类的方法**

对于父类的方法,只要它不符合子类模拟的实物的行为,都可对其进行重写。为此,可在子类中定义一个这样的方法,即它与要重写的父类方法同名。这样, Python 将不会考虑这个父类方法,而只关注你在子类中定义的相应方法。

例子：

```python
class ElectricCar(Car):
	--snip--
    
	def fill_gas_tank():
		""" 电动汽车没有油箱 """
		print("This car doesn't need a gas tank!")
```

使用继承时,可让子类保留从父类那里继承而来的精华,并剔除不需要的糟粕。



**将实例用作属性**

使用代码模拟实物时,你可能会发现自己给类添加的细节越来越多:属性和方法清单以及文件都越来越长。在这种情况下,可能需要将类的一部分作为一个独立的类提取出来。

例如：不断给 ElectricCar 类添加细节时,我们可能会发现其中包含很多专门针对汽车电瓶的属性和方法。在这种情况下,我们可将这些属性和方法提取出来,放到另一个名为 Battery 的类中,并将一个 Battery 实例用作 ElectricCar 类的一个属性:

```python
class Car():
--snip--

❶ class Battery():
	""" 一次模拟电动汽车电瓶的简单尝试 """
    
❷	def __init__(self, battery_size=70):
		""" 初始化电瓶的属性 """
		self.battery_size = battery_size
        
❸	def describe_battery(self):
		""" 打印一条描述电瓶容量的消息 """
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
class ElectricCar(Car):
	""" 电动汽车的独特之处 """
    
	def __init__(self, make, model, year):
		"""
		初始化父类的属性,再初始化电动汽车特有的属性
		"""
		super().__init__(make, model, year)
❹		self.battery = Battery()
        
my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
```

❶: 定义了一个名为 Battery 的新类,它没有继承任何类。

❷: 方法 \_\_init\_\_() 除 self 外,还有另一个形参 battery_size (默认参数)。

❸: 法 describe_battery() 也移到了这个类中。

❹: 在 ElectricCar 类中,添加了一个名为 self.battery 的属性。这行代码让 Python 创建一个新的 Battery 实例(由于没有指定尺寸,因此为默认值 70 ),并将该实例存储在属性 self.battery 中。每个 ElectricCar 实例都包含一个自动创建的 Battery 实例。



***

**动手试一试**

**9-6 冰淇淋小店 :** 冰淇淋小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的类,让它继承你为完成练习 9-1 或练习 9-4 而编写的 Restaurant 类。这两个版本的 Restaurant 类都可以,挑选你更喜欢的那个即可。添加一个名为 flavors 的属性,用于存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个 IceCreamStand 实例,并调用这个方法。

​	[9-6.py]()

**9-7 管理员 :** 管理员是一种特殊的用户。编写一个名为 Admin 的类,让它继承你为完成练习 9-3 或练习 9-5 而编写的 User 类。添加一个名为 privileges 的属性,用于存储一个由字符串(如 "can add post" 、 "can delete post" 、 "can ban user" 等)组成的列表。编写一个名为 show_privileges() 的方法,它显示管理员的权限。创建一个 Admin 实例,并调用这个方法。

​	[9-7.py]()

**9-8 权限 :** 编写一个名为 Privileges 的类,它只有一个属性 —— privileges ,其中存储了练习 9-7 所说的字符串列表。将方法 show_privileges() 移到这个类中。在 Admin 类中,将一个 Privileges 实例用作其属性。创建一个 Admin 实例,并使用方法 show_privileges() 来显示其权限。

​	[9-8.py]()

**9-9 电瓶升级 :** 在本节最后一个 electric_car.py 版本中,给 Battery 类添加一个名为 upgrade_battery() 的方法。这个方法检查电瓶容量,如果它不是 85 ,就将它设置为 85 。创建一辆电瓶容量为默认值的电动汽车,调用方法 get_range() ,然后对电瓶进行升级,并再次调用 get_range() 。你会看到这辆汽车的续航里程增加了。

​	[9-9.py]()

***





**导入类**

随着你不断地给类添加功能,文件可能变得很长,即便你妥善地使用了继承亦如此。为遵循 Python 的总体理念,应让文件尽可能整洁。为在这方面提供帮助, Python 允许你将类存储在模块中,然后在主程序中导入所需的模块。



**导入单个类**

例子：

*car.py*

```python
❶ """ 一个可用于表示汽车的类 """

class Car():
	""" 一次模拟汽车的简单尝试 """
    
	def __init__(self, make, model, year):
		""" 初始化描述汽车的属性 """
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
        
	def get_descriptive_name(self):
		""" 返回整洁的描述性名称 """
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
    
	def read_odometer(self):
		""" 打印一条消息,指出汽车的里程 """
		print("This car has " + str(self.odometer_reading) + " miles on it.")
        
	def update_odometer(self, mileage):
		"""
		将里程表读数设置为指定的值
		拒绝将里程表往回拨
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
            
	def increment_odometer(self, miles):
		""" 将里程表读数增加指定的量 """
		self.odometer_reading += miles
```

❶: 包含了一个模块级文档字符串,对该模块的内容做了简要的描述。应为自己创建的每个模块都编写文档字符串。



下面来创建另一个文件 ——**my_car.py** ,在其中导入 Car 类并创建其实例:

*my_car.py*

```python
❶ from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

❶: import 语句让 Python 打开模块 car ,并导入其中的 Car 类。

输出：

```
2016 Audi A4
This car has 23 miles on it.
```





**一个模块中存储多个类**

虽然同一个模块中的类之间应存在某种相关性,但可根据需要在一个模块中存储任意数量的类。



类 Battery 和 ElectricCar 都可帮助模拟汽车,因此下面将它们都加入模块car.py 中:

*car.py*

```python
""" 一组用于表示燃油汽车和电动汽车的类 """
class Car():
	--snip--
    
class Battery():
	""" 一次模拟电动汽车电瓶的简单尝试 """
    
	def __init__(self, battery_size=60):
		""" 初始化电瓶的属性 """
		self.battery_size = battery_size
        
	def describe_battery(self):
		""" 打印一条描述电瓶容量的消息 """
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
	def get_range(self):
		""" 打印一条描述电瓶续航里程的消息 """
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
        
class ElectricCar(Car):
	""" 模拟电动汽车的独特之处 """
    
	def __init__(self, make, model, year):
		"""
		初始化父类的属性,再初始化电动汽车特有的属性
		"""
		super().__init__(make, model, year)
		self.battery = Battery()
```



现在,可以新建一个名为 my_electric_car.py 的文件,导入 ElectricCar 类,并创建一辆电动汽车了:

*my_electric_car.py*

```python
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

输出：

```
2016 Tesla Model S
This car has a 70-kWh battery.
This car can go approximately 240 miles on a full charge.
```





**从一个模块中导入多个类**

可根据需要在程序文件中导入任意数量的类。

如果我们要在同一个程序中创建普通汽车和电动汽车,就需要将 Car 和 ElectricCar 类都导入:

*my_cars.py*

```python
❶ from car import Car, ElectricCar

❷ my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

❸ my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
```

❶: 从一个模块中导入多个类时,用逗号分隔了各个类。

❷: 创建了一辆大众甲壳虫普通汽车

❸: 创建了一辆特斯拉 Roadster 电动汽车

输出：

```
2016 Volkswagen Beetle
2016 Tesla Roadster
```



**导入整个模块**

还可以导入整个模块,再使用句点表示法访问需要的类。这种导入方法很简单,代码也易于阅读。由于创建类实例的代码都包含模块名,因此不会与当前文件使用的任何名称发生冲突。

下面的代码导入整个 car 模块,并创建一辆普通汽车和一辆电动汽车:

*my_cars.py*

```python
❶ import car

❷ my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

❸ my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
```

❶: 导入了整个 car 模块

❷: 创建了一辆大众甲壳虫汽车

❸: 创建了一辆特斯拉 Roadster 汽车



**导入模块中所有的类**

要导入模块中的每个类,可使用下面的语法:

```python
from module_name import *
```

不推荐使用这种导入方式,其原因有二。首先,如果只要看一下文件开头的 import 语句,就能清楚地知道程序使用了哪些类,将大有裨益;但这种导入方式没有明确地指出你使用了模块中的哪些类。这种导入方式还可能引发名称方面的困惑。如果你不小心导入了一个与程序文件中其他东西同名的类,将引发难以诊断的错误。



**在一个模块中导入另一个模块**

有时候,需要将类分散到多个模块中,以免模块太大,或在同一个模块中存储不相关的类。将类存储在多个模块中时,你可能会发现一个模块中的类依赖于另一个模块中的类。在这种情况下,可在前一个模块中导入必要的类。

例如,下面将 Car 类存储在一个模块中,并将 ElectricCar 和 Battery 类存储在另一个模块中。我们将第二个模块命名为 electric_car.py,并将 Battery 和 ElectricCar 类复制到这个模块中:

*electric_car.py*

```python
""" 一组可用于表示电动汽车的类 """
❶ from car import Car

class Battery():
	--snip--
    
class ElectricCar(Car):
	--snip--
```

ElectricCar 类需要访问其父类 Car ,因此在❶处,我们直接将 Car 类导入该模块中。如果我们忘记了这行代码, Python 将在我们试图创建 ElectricCar 实例时引发错误。

我们还需要更新模块 car ,使其包含 Car 类:

*car.py*

```python
""" 一个可用于表示汽车的类 """

class Car():
	--snip--
```

现在可以分别从每个模块中导入类,以根据需要创建任何类型的汽车了:

*my_cars.py*

```python
❶ from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
```

在❶处,我们从模块 car 中导入了 Car 类,并从模块 electric_car 中导入 ElectricCar 类。接下来,我们创建了一辆普通汽车和一辆电动汽车。这两种汽车都得以正确地创建:

```
2016 Volkswagen Beetle
2016 Tesla Roadster
```



***

**动手试一试**

**9-13 使用 OrderedDict :** 在练习 6-4 中,你使用了一个标准字典来表示词汇表。请使用 OrderedDict 类来重写这个程序,并确认输出的顺序与你在字典中添加键— 值对的顺序一致。

​	[9-13.py](https://github.com/programming-book-practice/Python-Crash-Course-Homework/blob/master/chapter09/9-13.py)

**9-14 骰子 :** 模块 random 包含以各种方式生成随机数的函数,其中的 randint() 返回一个位于指定范围内的整数,例如,下面的代码返回一个 1~6 内的整数:

```python
from random import randint
x = randint(1, 6)
```

请创建一个 Die 类,它包含一个名为 sides 的属性,该属性的默认值为 6 。编写一个名为 roll_die() 的方法,它打印位于 1 和骰子面数之间的随机数。创建一个 6 面的骰子,再掷 10 次。 创建一个 10 面的骰子和一个 20 面的骰子,并将它们都掷 10 次。

​	[9-14.py](https://github.com/programming-book-practice/Python-Crash-Course-Homework/blob/master/chapter09/9-14.py)

**9-15 Python Module of the Week :** 要了解 Python 标准库,一个很不错的资源是网站 Python Module of the Week 。请访问 http://pymotw.com/ 并查看其中的目录,在其中找一个你感兴趣的模块进行探索,或阅读模块 collections 和 random 的文档。

