# 第10章	文件和异常



#### 从文件中读取数据



**读取整个文件**

例子：

*pi_digits.txt*

包含精确到小数点后 30 位的圆周率值,且在小数点后每 10 位处都换行:

```
3.1415926535
8979323846
2643383279
```

下面的程序打开并读取这个文件,再将其内容显示到屏幕上:

*file_reader.py*

```python
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)
```

函数 *open()* 接受一个参数:要打开的文件的名称，返回一个表示文件的对象。在这里, open('pi_digits.txt') 返回一个表示文件 pi_digits.txt 的对象; Python 将这个对象存储在我们将在后面使用的变量中。

关键字 with 在不再需要访问文件后将其关闭。在这个程序中,注意到我们调用了 open() ,但没有调用 close() ;你也可以调用 open() 和 close() 来打开和关闭文件,但这样做时,如果程序存在 bug ,导致 close() 语句未执行,文件将不会关闭。

有了表示 pi_digits.txt 的文件对象后,我们使用方法 read() (前述程序的第 2 行)读取这个文件的全部内容,并将其作为一个长长的字符串存储在变量 contents 中。这样,通过打印 contents 的值,就可将这个文本文件的全部内容显示出来:

```
3.1415926535
8979323846
2643383279

```

相比于原始文件,该输出唯一不同的地方是末尾多了一个空行。为何会多出这个空行呢?因为 read() 到达文件末尾时返回一个空字符串,而将这个空字符串显示出来时就是一个空行。要删除多出来的空行,可在 print 语句中使用 rstrip() :

```python
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())
```



**文件路径**

要让 Python 打开不与程序文件位于同一个目录中的文件,需要提供文件路径 ,它让 Python 到系统的特定位置去查找。

在 Linux 和 OS X 中：

```python
# 相对路径 目标文件存放在与程序文件同一个目录下的text_files目录下
with open('text_files/filename.txt') as file_object:
```

在 Windows 系统中:

```python
with open('text_files\filename.txt') as file_object:
```



还可以将文件在计算机中的准确位置告诉 Python ,这样就不用关心当前运行的程序存储在什么地方了。这称为*绝对文件路径* 。

在 Linux 和 OS X 中:

```python
file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
with open(file_path) as file_object:
```

在 Windows 系统中:

```python
file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
with open(file_path) as file_object:
```



**逐行读取**

例子：

```python
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line)
```

发现空白行更多了:

```
3.1415926535

  8979323846
  
  2643383279
  
```



**创建一个包含文件各行内容的列表**

使用关键字 with 时, open() 返回的文件对象只在 with 代码块内可用。

例子：

```python
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
    
for line in lines:
	print(line.rstrip())
```

方法 readlines() 从文件中读取每一行,并将其存储在一个列表中;接下来,该列表被存储到变量 lines 中;在 with 代码块外,我们依然可以使用这个变量。



**使用文件的内容**

将文件读取到内存中后,就可以以任何方式使用这些数据了。

例子：

```python
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    
print(pi_string)
print(len(pi_string))
```

输出：

```
3.1415926535 8979323846 2643383279
36
```

**注意**	读取文本文件时, Python 将其中的所有文本都解读为字符串。如果你读取的是数字,并要将其作为数值使用,就必须使用函数 int() 将其转换为整数,或使用函数 float() 将其转换为浮点数。



***

**动手试一试**

**10-1 Python 学习笔记 :** 

​	[10-1.py]()

**10-2 C 语言学习笔记 :** 可使用方法 replace() 将字符串中的特定单词都替换为另一个单词。下面是一个简单的示例,演示了如何将句子中的 'dog' 替换为 'cat'

```
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
```

读取你刚创建的文件 learning_python.txt 中的每一行,将其中的 Python 都替换为另一门语言的名称,如 C 。将修改后的各行都打印到屏幕上。

​	[10-2.py]()

***





#### 写入文件

保存数据的最简单的方式之一是将其写入到文件中。



**写入空文件**

例子：

```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.")
```

在这个示例中,调用 open() 时提供了两个实参。第一个实参也是要打开的文件的名称;第二个实参( 'w' )告诉 Python ,我们要以写入模式 打开这个文件。打开文件时,可指定读取模式 ( 'r' )、写入模式 ( 'w' )、附加模式 ( 'a' )或让你能够读取和写入文件的模式( 'r+' )。如果你省略了模式实参, Python 将以默认的只读模式打开文件。

如果你要写入的文件不存在,函数 open() 将自动创建它。然而,以写入( 'w' )模式打开文件时千万要小心,因为如果指定的文件已经存在, Python 将在返回文件对象前清空该文件。

我们使用文件对象的方法 write() 将一个字符串写入文件。这个程序没有终端输出,但如果你打开文件 programming.txt ,将看到其中包含如下一行内容:

```
I love programming.
```



**写入多行**

函数 write() 不会在你写入的文本末尾添加换行符,因此如果你写入多行时没有指定换行符,文件看起来可能不是你希望的那样，要让每个字符串都单独占一行,需要在 write() 语句中包含换行符。



***

**动手试一试**

**10-3 访客 :** 编写一个程序,提示用户输入其名字;用户作出响应后,将其名字写入到文件 guest.txt 中。

​	[10-3.py]()

**10-4 访客名单 :** 编写一个 while 循环,提示用户输入其名字。用户输入其名字后,在屏幕上打印一句问候语,并将一条访问记录添加到文件 guest_book.txt 中。确保这个文件中的每条记录都独占一行。

​	[10-4.py]()

**10-5 关于编程的调查 :** 编写一个 while 循环,询问用户为何喜欢编程。每当用户输入一个原因后,都将其添加到一个存储所有原因的文件中。

​	[10-5.py]()

***



#### 异常

每当发生让 Python 不知所措的错误时,它都会创建一个异常对象。如果你编写了处理该异常的代码,程序将继续运行;如果你未对异常进行处理,程序将停止,并显示一个 traceback ,其中包含有关异常的报告。

异常是使用 try-except 代码块处理的。



**处理 ZeroDivisionError 异常**

例子：

```python
print(5/0)
```

输出：

```
Traceback (most recent call last):
	File "division.py", line 1, in <module>
		print(5/0)
ZeroDivisionError: division by zero
```

指出的错误 ZeroDivisionError 是一个异常对象。Python 无法按你的要求做时,就会创建这种对象。



**使用try-except代码块**

处理 ZeroDivisionError 异常的 try-except 代码块类似于下面这样:

```python
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")
```

如果 try 代码块中的代码运行起来没有问题, Python 将跳过 except 代码块;如果 try 代码块中的代码导致了错误, Python 将查找这样的 except 代码块,并运行其中的代码,即其中指定的错误与引发的错误相同。

输出：

```
You can't divide by zero!
```

如果 try-except 代码块后面还有其他代码,程序将接着运行,因为已经告诉了 Python 如何处理这种错误。



**使用异常避免崩溃**

发生错误时,如果程序还有工作没有完成,妥善地处理错误就尤其重要。这种情况经常会出现在要求用户提供输入的程序中;如果程序能够妥善地处理无效输入,就能再提示用户提供有效输入,而不至于崩溃。

例子：

```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	answer = int(first_number) / int(second_number)
	print(answer)
```

这个程序提示用户输入一个数字,并将其存储到变量 first_number 中;如果用户输入的不是表示退出的 q ,就再提示用户输入一个数字,并将其存储到变量 second_number 中。接下来,我们计算这两个数字的商。这个程序没有采取任何处理错误的措施,因此让它执行除数为 0 的除法运算时,它将崩溃。

修改：

```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)
```



**处理FileNotFoundError异常**

使用文件时,一种常见的问题是找不到文件:你要查找的文件可能在其他地方、文件名可能不正确或者这个文件根本就不存在。对于所有这些情形,都可使用 try-except 代码块以直观的方式进行处理。

例子：

```python
filename = 'alice.txt'

with open(filename) as f_obj:
	contents = f_obj.read()
```

Python 无法读取不存在的文件,因此它引发一个异常:

```
Traceback (most recent call last):
	File "alice.py", line 3, in <module>
		with open(filename) as f_obj:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
```

报告了 FileNotFoundError 异常,这是 Python 找不到要打开的文件时创建的异常。在这个示例中,这个错误是函数 open() 导致的,因此要处理这个错误,必须将 try 语句放在包含 open() 的代码行之前:

```python
filename = 'alice.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)
```

输出：

```
Sorry, the file alice.txt does not exist.
```



**分析文本**

例子：

```bash
>>> title = "Alice in Wonderland"
>>> title.split()
['Alice', 'in', 'Wonderland']
```

方法 split() 以空格为分隔符将字符串分拆成多个部分,并将这些部分都存储到一个列表中。

```python
filename = 'alice.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)
else:
	# 计算文件大致包含多少个单词
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words.")
```

输出：

```
The file alice.txt has about 29461 words.
```



**失败时一声不吭**

有时候你希望程序在发生异常时一声不吭,就像什么都没有发生一样继续运行。

例子：

```python
def count_words(filename):
	""" 计算一个文件大致包含多少个单词 """
	try:
		--snip--
	except FileNotFoundError:
		pass
	else:
		--snip--
        
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)
```



***

**动手试一试**

**10-6 加法运算 :** 提示用户提供数值输入时,常出现的一个问题是,用户提供的是文本而不是数字。在这种情况下,当你尝试将输入转换为整数时,将引发 TypeError 异常。编写一个程序,提示用户输入两个数字,再将它们相加并打印结果。在用户输入的任何一个值不是数字时都捕获 TypeError 异常,并打印一条友好的错误消息。对你编写的程序进行测试:先输入两个数字,再输入一些文本而不是数字。

​	[10-6.py]()

**10-7 加法计算器 :** 将你为完成练习 10-6 而编写的代码放在一个 while 循环中,让用户犯错(输入的是文本而不是数字)后能够继续输入数字。

​	[10-7.py]()

**10-8 猫和狗 :** 创建两个文件 cats.txt 和 dogs.txt ,在第一个文件中至少存储三只猫的名字,在第二个文件中至少存储三条狗的名字。编写一个程序,尝试读取这些文件,并将其内容打印到屏幕上。将这些代码放在一个 try-except 代码块中,以便在文件不存在时捕获 FileNotFound 错误,并打印一条友好的消息。将其中一个文件移到另一个地方,并确认 except 代码块中的代码将正确地执行。

​	[10-8.py]()

**10-9 沉默的猫和狗 :** 修改你在练习 10-8 中编写的 except 代码块,让程序在文件不存在时一言不发。

​	[10-9.py]()

***



#### 存储数据

使用模块 json 来存储数据。



**使用 json.dump() 和 json.load()**

编写一个存储一组数字的简短程序,再编写一个将这些数字读取到内存中的程序。第一个程序将使用 json.dump() 来存储这组数字,而第二个程序将使用 json.load() 。



函数 json.dump() 接受两个实参:要存储的数据以及可用于存储数据的文件对象。下面演示了如何使用 json.dump() 来存储数字列表:

```python
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)
```

打开文件 numbers.json，数据的存储格式与 Python 中一样:

```
[2, 3, 5, 7, 11, 13]
```



使用 json.load() 将这个列表读取到内存中:

```python
import json

filename = 'numbers.json'
with open(filename) as f_obj:
	numbers = json.load(f_obj)

print(numbers)
```

输出：

```
[2, 3, 5, 7, 11, 13]
```



**重构**

代码能够正确地运行,但可做进一步的改进 —— 将代码划分为一系列完成具体工作的函数。这样的过程被称为重构 。重构让代码更清晰、更易于理解、更容易扩展。



例子：

```python
import json

def get_stored_username():
	""" 如果存储了用户名,就获取它 """
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
    	return None
	else:
		return username
    
def get_new_username():
	""" 提示用户输入用户名 """
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	""" 问候用户,并指出其名字 """
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")
        
greet_user()
```

每个函数都执行单一而清晰的任务。



***

**动手试一试**

**10-11 喜欢的数字 :** 编写一个程序,提示用户输入他喜欢的数字,并使用 json.dump() 将这个数字存储到文件中。再编写一个程序,从文件中读取这个值,并打印消息 “I know your favorite number! It's _____.” 。

​	[10-11.py]()

**10-12 记住喜欢的数字 :** 将练习 10-11 中的两个程序合而为一。如果存储了用户喜欢的数字,就向用户显示它,否则提示用户输入他喜欢的数字并将其存储到文件中。运行这个程序两次,看看它是否像预期的那样工作。

​	[10-12.py]()

**10-13 验证用户 :** 最后一个 remember_me.py 版本假设用户要么已输入其用户名,要么是首次运行该程序。我们应修改这个程序,以应对这样的情形:当前和最后一次运行该程序的用户并非同一个人。

为此,在 greet_user() 中打印欢迎用户回来的消息前,先询问他用户名是否是对的。如果不对,就调用 get_new_username() 让用户输入正确的用户名。

​	[10-13.py]()

***



