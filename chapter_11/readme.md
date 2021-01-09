# 第11章	测试代码



使用 Python 模块 unittest 中的工具来测试代码。



#### 测试函数

Python 标准库中的模块 unittest 提供了代码测试工具。**单元测试** 用于核实函数的某个方面没有问题;**测试用例** 是一组单元测试,这些单元测试一起核实函数在各种情形下的行为都符合要求。良好的测试用例考虑到了函数可能收到的各种输入,包含针对所有这些情形的测试。**全覆盖式测试** 用例包含一整套单元测试,涵盖了各种可能的函数使用方式。



**可通过的测试**

例子：

*name_function.py*

```python
def get_formatted_name(first, last):
	"""Generate a neatly formatted full name."""
	full_name = first + ' ' + last
	return full_name.title()
```

要为函数编写测试用例,可先导入模块 unittest 以及要测试的函数,再创建一个继承 unittest.TestCase 的类。

下面是一个只包含一个方法的测试用例,它检查函数 get_formatted_name() 在给定名和姓时能否正确地工作:

*test_name_function.py*

```python
import unittest
from name_function import get_formatted_name

❶ class NamesTestCase(unittest.TestCase):
	""" 测试 name_function.py"""
    
	def test_first_last_name(self):
		""" 能够正确地处理像 Janis Joplin 这样的姓名吗? """
❷		formatted_name = get_formatted_name('janis', 'joplin')
❸		self.assertEqual(formatted_name, 'Janis Joplin')
        
unittest.main()
```

导入了模块 unittest 和要测试的函数 get_formatted_name() 。

❶: 创建了一个名为 NamesTestCase 的类,用于包含一系列针对 get_formatted_name() 的单元测试。这个类必须继承 unittest.TestCase 类,这样 Python 才知道如何运行你编写的测试。

NamesTestCase 只包含一个方法,用于测试 get_formatted_name() 的一个方面。我们将这个方法命名为 test_first_last_name() ,因为我们要核实的是只有名和姓的姓名能否被正确地格式化。我们运行 testname_function.py 时,所有以 test 打头的方法都将自动运行。在这个方法中,我们调用了要测试的函数,并存储了要测试的返回值。

❷: 使用实参 'janis' 和 'joplin' 调用 get_formatted_name() ,并将结果存储到变量 formatted_name 中

❸: 使用了 unittest 类最有用的功能之一:一个断言 方法。断言方法用来核实得到的结果是否与期望的结果一致。

为检查是否确实如此,我们调用 的方法 assertEqual() ,并向它传递 formatted_name 和 'Janis Joplin' 。

“ 将 formatted_name 的值同字符串 'Janis Joplin' 进行比较,如果它们相等,就万事大吉,如果它们不相等,跟我说一声! ”

代码行 unittest.main() 让 Python 运行这个文件中的测试。运行 test_name_function.py 时,得到的输出如下:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
OK
```

第 1 行的句点表明有一个测试通过了。接下来的一行指出 Python 运行了一个测试,消耗的时间不到 0.001 秒。最后的 OK 表明该测试用例中的所有单元测试都通过了。



**不能通过的测试**

测试未通过时结果是什么样的呢?我们来修改 get_formatted_name() ,使其能够处理中间名。

*name_function.py*

```python
def get_formatted_name(first, middle, last):
	""" 生成整洁的姓名 """
	full_name = first + ' ' + middle + ' ' + last
	return full_name.title()
```

这个版本应该能够正确地处理包含中间名的姓名,但对其进行测试时,我们发现它再也不能正确地处理只有名和姓的姓名。这次运行程序 test_name_function.py 时,输出如下:

```
❶  E
======================================================================
❷ ERROR: test_first_last_name (__main__.NamesTestCase)
----------------------------------------------------------------------
❸ Traceback (most recent call last):
	File "test_name_function.py", line 8, in test_first_last_name
		formatted_name = get_formatted_name('janis', 'joplin')
  TypeError: get_formatted_name() missing 1 required positional argument: 'last'
----------------------------------------------------------------------
❹ Ran 1 test in 0.000s
❺ FAILED (errors=1)
```

❶: 第 1 行输出只有一个字母 E),它指出测试用例中有一个单元测试导致了错误。

❷: 看到 NamesTestCase 中的 test_first_last_name() 导致了错误。测试用例包含众多单元测试时,知道哪个测试未通过至关重要。

❸: 看到了一个标准的 traceback ,它指出函数调用 get_formatted_name('janis', 'joplin') 有问题,因为它缺少一个必不可少的位置实参。

❹: 看到运行了一个单元测试

❺: 指出整个测试用例都未通过,因为运行该测试用例时发生了一个错误。这条消息位于输出末尾,一眼就能看到。



**测试未通过时怎么办**

测试未通过时怎么办呢?如果你检查的条件没错,测试通过了意味着函数的行为是对的,而测试未通过意味着你编写的新代码有错。因此,测试未通过时,不要修改测试,而应修复导致测试不能通过的代码:检查刚对函数所做的修改,找出导致函数行为不符合预期的修改。



***

**动手试一试**

**11-1 城市和国家 :** 编写一个函数,它接受两个形参:一个城市名和一个国家名。这个函数返回一个格式为 City, Country 的字符串,如 Santiago, Chile 。将这个函数存储在一个名为 city_functions.py 的模块中。

创建一个名为 test_cities.py 的程序,对刚编写的函数进行测试(别忘了,你需要导入模块 unittest 以及要测试的函数)。编写一个名为 test_city_country() 的方法,核实使用类似于 'santiago' 和 'chile' 这样的值来调用前述函数时,得到的字符串是正确的。运行 test_cities.py ,确认测试 test_city_country() 通过了。

​	[11-1.py]()

**11-2 人口数量 :** 修改前面的函数,使其包含第三个必不可少的形参 population ,并返回一个格式为 City, Country - population xxx 的字符串,如 Santiago, Chile - population 5000000 。运行 test_cities.py ,确认测试 test_city_country() 未通过。

修改上述函数,将形参 population 设置为可选的。再次运行 test_cities.py ,确认测试 test_city_country() 又通过了。

再编写一个名为 test_city_country_population() 的测试,核实可以使用类似于 'santiago' 、 'chile' 和 'population=5000000' 这样的值来调用这个函数。再次运行 test_cities.py ,确认测试 test_city_country_population() 通过了。

​	[11-2.py]()

***



#### 测试类



**各种断言方法**

Python 在 unittest.TestCase 类中提供了很多断言方法。

6 个常用的断言方法。

|           方法            |          用途          |
| :-----------------------: | :--------------------: |
|     assertEqual(a, b)     |       核实a == b       |
|   assertNotEqual(a, b)    |       核实a != b       |
|       assertTrue(x)       |      核实x 为True      |
|      assertFalse(x)       |     核实x 为False      |
|  assertIn(item , list )   |  核实 item 在 list 中  |
| assertNotIn(item , list ) | 核实 item 不在 list 中 |



**一个要测试的类**

下面来编写一个类进行测试。

*survey.py*

```python
class AnonymousSurvey():
    """收集匿名调查问卷的答案"""

    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查卷"""
        self.responses.append(new_response)

    def show_result(self):
        """显示收集到的所有答卷"""
        print("Survey result: ")
        for response in self.responses:
            print('- ' + response)
```

为证明 AnonymousSurvey 类能够正确地工作,我们来编写一个使用它的程序:

*language_survey.py*

```python
from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果
print("\nThank you to every who participated in the survey!")
my_survey.show_result()
```

输出：

```
What language did you first learn to speak?
Enter 'q' at any time to quit.

Language: English
Language: Spanish
Language: Mandarin
Language: q

Thank you to every who participated in the survey!
Survey result: 
- English
- Spanish
- Mandarin
```



**测试AnonymousSurvey 类**

下面来编写一个测试,对 AnonymousSurvey 类的行为的一个方面进行验证:如果用户面对调查问题时只提供了一个答案,这个答案也能被妥善地存储。为此,我们将在这个答案被存储后,使用方法 assertIn() 来核实它包含在答案列表中:

*test_survey.py*

```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

unittest.main()
```

我们首先导入了模块 unittest 以及要测试的类 AnonymousSurvey 。我们将测试用例命名为 TestAnonymousSurvey ,它也继承了 unittest.TestCase。第一个测试方法验证调查问题的单个答案被存储后,会包含在调查结果列表中。对于这个方法,一个不错的描述性名称是 test_store_single_response()。如果这个测试未通过,我们就能通过输出中的方法名得知,在存储单个调查答案方面存在问题。

要测试类的行为,需要创建其实例。使用方法 store_response() 存储了单个答案 English 。接下来,我们检查 English 是否包含在列表 my_survey.responses 中,以核实这个答案是否被妥善地存储了。

运行 test_survey.py 时,测试通过了:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.001s
OK
```



下面来核实用户提供三个答案时,它们也将被妥善地存储。为此,我们在 TestAnonymousSurvey 中再添加一个方法:

```python
def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)
```

再次运行 test_survey.py 时,两个测试(针对单个答案的测试和针对三个答案的测试)都通过了:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s
OK
```



**方法setUp()**

在前面的 test_survey.py 中,我们在每个测试方法中都创建了一个 AnonymousSurvey 实例,并在每个方法中都创建了答案。 unittest.TestCase 类包含方法 setUp() ,让我们只需创建这些对象一次,并在每个测试方法中使用它们。如果你在 TestCase 类中包含了方法 setUp() , Python 将先运行它,再运行各个以 test_ 打头的方法。这样,在你编写的每个测试方法中都可使用在方法 setUp() 中创建的对象了。

```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnoymousSurvey类的测试"""

    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_responses(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
```

方法 setUp() 做了两件事情:创建一个调查对象;创建一个答案列表。存储这两样东西的变量名包含前缀 self (即存储在属性中),因此可在这个类的任何地方使用。这让两个测试方法都更简单,因为它们都不用创建调查对象和答案。





***

**动手试一试**

**11-3 雇员 :** 编写一个名为 Employee 的类,其方法 __init__() 接受名、姓和年薪,并将它们都存储在属性中。编写一个名为 give_raise() 的方法,它默认将年薪增加 5000 美元,但也能够接受其他的年薪增加量。

为 Employee 编写一个测试用例,其中包含两个测试方法: test_give_default_raise() 和 test_give_custom_raise() 。使用方法 setUp() ,以免在每个测试方法中都创建新的雇员实例。运行这个测试用例,确认两个测试都通过了。

​	[employee.py]()

​	[test_employee.py]()

***



