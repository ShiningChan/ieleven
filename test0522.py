print('stay foolish, stay hungry!')

###################### 第3章习题 ######################

##1
print('\n第一题')
years_list = [1991, 1992, 1993, 1994, 1995, 1996]
print(years_list)



##2
print('\n第二题')
print(years_list[3])


##3
print('\n第三题')
print(years_list[-1])


##4
print('\n第四题')
things = ['mozzarella', 'cinderella', 'salmonella']
print(things)

##5
print('\n第五题')
things[1] = things[1].capitalize()
print(things)

##6
print('\n第六题')
things[0] = things[0].upper()
print(things)

##7
print('\n第七题')
del things[2]
print(things)

##8
print('\n第八题')
surprise = ['Groucho', 'Chico', 'Harpo']
print(surprise)

##9
print('\n第九题')
surprise[-1] = ((surprise[-1].lower())[::-1]).capitalize()
print(surprise)

##10
print('\n第十题')
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'}
print(e2f)



##11
print('\n第十一题')
print(e2f['walrus'])

##12
print('\n第十二题')
f2e = {}
for key, value in e2f.items():
    f2e[value] = key
print(f2e)


##13
print('\n第十三题')
print(f2e['chien'])

##14
print('\n第十四题')
e2f_key = set(e2f.keys())
print(e2f_key)


##15
print('\n第十五题')
cats = ['Henri', 'Grumpy', 'Lucy']
animals = {'cats': cats, 'octopi': {} , 'emus': {}}
life = {'animals': animals ,'plants': {} ,'others': {}}
print(life)

##16
print('\n第十六题')
print(life.keys())

##17
print('\n第十七题')
print(life['animals'].keys())
print(animals.keys())

##18
print('\n第十八题')
print(life['animals']['cats'])
print(cats)




###################### 第4章习题 ######################

##1
print('\n第一题')
guess_me = 7

if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')
    
    
##2
print('\n第二题')
guess_me = 7
start = 1

while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    start += 1

##3
print('\n第三题')
test_list = [3, 2, 1, 0]
for i in test_list:
    print(i)

    
##4
print('\n第四题')
print([x for x in range(10) if x % 2 == 0])


##5
print('\n第五题')
print({key: key * key for key in range(10)})

##6
print('\n第六题')
print({x for x in range(10) if x % 2 == 1})

##7
print('\n第七题')
find_int = (i for i in 'GOT' if isinstance(i,int))
for i in find_int:
    print(i)
find_int2 = (i for i in range(10) if isinstance(i,int))
for i in find_int2:
    print(i)
print(find_int2)
    
##8
print('\n第八题')
def good():
    return ['Harry', 'Ron', 'Hermione']
    
test_list = good()
print(test_list)
    
##9
print('\n第九题')
def get_odds():
    for i in range(10):
        if i % 2 == 1:
            yield i
        
get_odds = get_odds()
m = 1

for i in get_odds:
    if m == 3:
        print(i)
        break
    else:
        m += 1

##10
print('\n第十题')
def test(func):
    def new_functions(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
        return True
    return new_functions
    
@test
def good():
    print('good!')

good()

##11
print('\n第十一题')
print(test_list)
try:
    print(test_list[3])
except IndexError as OopsException:
    print('Caught an oops')
    
    
##12
print('\n第十二题')
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movies)
movies_list = list(zip(titles, plots))
print(movies_list)

###################### 第5章课程 ######################

#setdefault()类似get()
#当键不存在时，往字典中添加一项
#当键存在时，不改变

print('\n')

dicttable = {'cz': 175, 'wq': 158}
print(dicttable)
print('\n')

dicttable.setdefault('dy', 159)
print(dicttable)
print('\n')

dicttable.setdefault('dy', 160)
print(dicttable)
print('\n')


#defaultdict()的参数是一个函数，返回赋值给缺失键的值

from collections import defaultdict

def no_idea():
	return 'Huh?'
	

maindict = defaultdict(no_idea)

maindict['A'] = 'an apple'
maindict['B'] = 'a bell'

print(maindict['C'])

for d in maindict.items():
    print(d)
	
print('/n')


#使用lamda函数
seconddict = defaultdict(lambda: 'Huh?')
print(seconddict['h'])
print(seconddict)



from collections import defaultdict

breakfast_food = ['spam', 'spam', 'eggs', 'spam']
lunch_food = ['eggs', 'eggs', 'bacon']

#计数器
counter_bre = defaultdict(int)   #int()初始化为0
for food in breakfast_food:
    counter_bre[food] += 1

for food, count in counter_bre.items():
    print(food, count)
print('\n')

#原始计数
counter_bre2 = {}
for food in breakfast_food:
    if not food in counter_bre2:
        counter_bre2[food] = 0      #需要手动初始化
    counter_bre2[food] += 1

    
for food, count in counter_bre2.items():
    print(food, count)
print('\n')
    

#自带计数器Counter()
from collections import Counter
counter_bre3 = Counter(breakfast_food)
counter_lunch = Counter(lunch_food)
print('早餐清单如下：')
print(counter_bre3)
print(counter_bre3.most_common())       #降序排列
print('\n')
print('午餐清单如下：')
print(counter_lunch)
print(counter_lunch.most_common(1))      #1之前的数字降序排列
print('\n')

#+- &|
plus_counter = counter_bre3 + counter_lunch
minus_counter = counter_bre3 - counter_lunch
and_counter = counter_bre3 & counter_lunch
or_counter = counter_bre3 | counter_lunch

print('plus_counter:')
print(plus_counter)
print('\n')

print('minus_counter')
print(minus_counter)
print('\n')

print('and_counter')
print(and_counter)
print('\n')

print('or_counter')
print(or_counter)
print('\n')





#有序字典生成

from collections import OrderedDict
quotes = OrderedDict([
	('Moe', 'A wise guy, huh?'),
	('Larry', 'Ow!'),
	('Curly', 'Nyuk nyuk!')
	])
	
quotes2 = dict([
    ('Moe', 'A wise guy, huh?'),
	('Larry', 'Ow!'),
	('Curly', 'Nyuk nyuk!')
	])
	

	
for stooge in quotes:    #打印key
    print(stooge)
print('\n')
	
for stooge in quotes2:    #打印key
    print(stooge)
print('\n')



#deque回文判断

def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.pop() != dq.popleft():
            return False
    return True 
    
    
#反向切片实现回文判断
def palindrome2(word):
    return word == word[::-1]
    

testword = ['a', 'hello', 'qwertyuiuytrewq', '123ertre321', '1234']

for w in testword:
    print(palindrome(w))
    print(palindrome2(w))
    if palindrome2(w) != palindrome(w):
        print('difference\n')
    else:
        print('same\n')

        
        
        
##itertools迭代代码结构


##chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
import itertools
m = itertools.chain([1, 2], ['a', 'b'])

for i in m:
    print(i)
print('\n')


##accumulate()计算累积的值，默认为加法函数
import itertools
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)
print('\n')


##定义乘法函数，修改accumulate参数
import itertools
def multiply(a, b):
    return a * b
    
for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)
print('\n')

##count计数器
import itertools
for item in itertools.count(1):
    print(item)
    if item > 10:
        break
print('\n')
        
##repeat将一个元素无限循环，也可增加次数参数
import itertools
for item in itertools.repeat('A', 4):
    print(item)

    
##pprint()友好输出：排列输出元素增加可读性
from pprint import pprint
from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'A wise guy'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!')
    ])

print(quotes)
pprint(quotes)


###################### 第5章习题 ######################

##1导入模块
print('\n第一题')
import zoo
zoo.hours()


##2导入模块并重命名
print('\n第二题')
import zoo as menagerie
menagerie.hours()


##3导入模块中函数
print('\n第三题')
from zoo import hours
hours()



##4导入模块中函数并重命名
print('\n第四题')
from zoo import hours as info
info()



##5
print('\n第五题')
plain = {
    'a': 1,
    'b': 2,
    'c': 3
    }
    
print(plain)


##6
print('\n第六题')
from collections import OrderedDict
fancy = OrderedDict([
    ('a', 1),
    ('b', 2),
    ('c', 3)
    ])
    
print(fancy)
for k, v in fancy.items():
    print(k, v)
    

##7
print('\n第七题')
dict_of_lists = {}
dict_of_lists['a'] = 'something for a'
print(dict_of_lists['a'])

###################### 第6章课程 ######################

##1.创建类
class Person():    #一般首字母大写
    def __init__(self, name):    #初始化方法,前后分别两个下划线
        self.name = name
        
##创建实例
hunter = Person('Elmer Fudd')

print('The mighty hunber: ', hunter.name)

print('\n')

##2.创建类继承类
class Car():
    def exclaim(self):
        print("I'm a car!")
        
class Yugo(Car):  #继承类
    pass

#创建实例
give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

print('\n')

##3.创建类继承类覆盖父类
#可以覆盖所有类，包括init
#也可以新增父类中没有的方法
class Car():
    def exclaim(self):
        print("I'm a car!")
        
class Yugo(Car):    #继承类，并修改
    def exclaim(self):
        print("I'm a Yugo!")
        

#创建实例
give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

print('\n')


##4.使用super()显示调用父类的方法，否则会被覆盖
class Person():
    def __init__(self, name):
        self.name = name

        
class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)  #显示调用
        self.email = email
        
        
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)

print('\n')

##5.使用属性对特性进行访问和设置
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)
    

#新建实例
fowl = Duck('Howard')
fowl.name
print(fowl.get_name())
print('\n')

fowl.name = 'Daffy'
print(fowl.name)
print('\n')

fowl.set_name('Daffy')
print(fowl.name)
print('\n')
        
        
##5.使用修饰符对特性进行访问和设置
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    

#新建实例
fowl = Duck('Howard')
fowl.name
print(fowl.name)
print('\n')

fowl.name = 'Daffy'
print(fowl.name)
print('\n')


##6.使用名称保护私有特性
class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name
    

#新建实例
fowl = Duck('Howard')
fowl.name
print(fowl.name)
print('\n')

fowl.name = 'Daffy'
#print(fowl.__name)
#print(fowl._Duck__name)
print('\n')


##7.类的方法和实例的方法
class A():
    count = 0
    def __init__(self):
        A.count += 1    #类特性
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):    #cls同A
        print("A has ", cls.count, "little objects.")
        
easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()
print('\n')

##8.静态方法
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')
        

CoyoteWeapon.commercial()
print('\n')

##9.组合
class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', bill.description, 
        'bill and a', tail.length, 'tail')
        
tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()
print('\n')

##10.命名元组
from collections  import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)
print('\n')

##用字典构造命名元组
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)   # **kw
print(duck2)
duck3 = duck2._replace(tail = 'magnificent', bill = 'crushing')
print(duck3)
print('\n')




###################### 第6章习题 ######################

##新建类和对象
print('\n第一题')
class Thing():
    pass

print(Thing())

example = Thing()
print(example)


##创建类，赋值类特性
print('\n第二题')
class Things():
    def __init__(self, letters):
        Things.letters = letters
        
Things('abc')
print(Things.letters)


##创建类，赋值实例特性
print('\n第三题')
class Things3():
    def __init__(self, letters):
        self.letters = letters

things = Things3('xyz')
print(things.letters)


##创建类，新建实例特性，并实例化对象
print('\n第四题')
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
        
ele = Element('Hydrogen', 'H', 1)
print(ele.name, ele.symbol, ele.number)


##用字典实例化对象
print('\n第五题')
dict_ele = {
    'name': 'Hydrogen',
    'symbol': 'H',
    'number': 1}
    
hydrogen = Element(**dict_ele)
print(hydrogen.name, hydrogen.symbol, hydrogen.number)

##类中定义方法，打印对象特性
print('\n第六题')
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print(self.name, self.symbol, self.number)
        
hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.dump()


##修改Element方法为私有
print('\n第七题')
print(hydrogen)
print('\n')

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        print(self.name, self.symbol, self.number)
        
hydrogen = Element('Hydrogen', 'H', 1)
#print(hydrogen)


##修改Element所有特性为私有
print('\n第八题')
class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    def __str__(self):
        print(self.name, self.symbol, self.number)
    @property
    def name(self):
        print('inside getter_name')
        return self.__name
    @property
    def symbol(self):
        print('inside the getter_symbol')
        return self.__symbol
    @property    #每个特性前都需标注
    def number(self):
        print('inside the getter_number')
        return self.__number

hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.name)    #访问的是特性，不是方法，不需要()
print('\n')
print(hydrogen.symbol)
print('\n')
print(hydrogen.number)
print('\n')        


##定义3个类，返回eat方法
print('\n第九题')
class Bear():
    def eats(self):
        return 'berries'

class Rabbit():
    def eats(self):
        return 'clover'        

class Octothorpe():
    def eats(self):
        return 'campers'
        
bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()

print('bear eats ' + bear.eats())
print('rabbit eats ' + rabbit.eats())
print('octothorpe eats ' + octothorpe.eats())


##定义3个类，返回does方法
print('\n第十题')
class Laser():
    def does(self):
        return 'disintegrate'

class Claw():
    def does(self):
        return 'crush'        

class SmartPhone():
    def does(self):
        return 'ring'

class Robot():
    def __init__(self, Laser, Claw, SmartPhone):
        self.Laser = Laser
        self.Claw = Claw
        self.SmartPhone = SmartPhone
    def does(self):
        print( 'Laser: ' +  self.Laser.does())
        print('Claw: ' +  self.Claw.does())
        print('SmartPhone: ' +  self.SmartPhone.does())
        
laser = Laser()
claw = Claw()
smartPhone = SmartPhone()

robot = Robot(laser, claw, smartPhone)
robot.does()

###################### 第7章课程 ######################

##unicodedata模块转换函数
def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value) #接受不区分大小写的标准名称，返回一个Unicode字符
    value2 = unicodedata.lookup(name) #接受一个Unicode字符，返回大写形式的名称
    print('value = "%s", name = "%s", value2 = "%s"' 
    % (value, name, value2))
    

unicode_test('A')    #纯ASCII字符
# value = "A",
# name = "LATIN CAPITAL LETTER A", 
# value2 = "A"

print('\n')
unicode_test('$')    #ASCII标点符号
# value = "$", 
# name = "DOLLAR SIGN", 
# value2 = "$"

print('\n')
unicode_test('\u20a2')    #ASCII货币字符
# value = "₢", 
# name = "CRUZEIRO SIGN", 
# value2 = "₢"

print('\n')
unicode_test('\u20ac')    #ASCII货币字符
# value = "€", 
# name = "EURO SIGN",
# value2 = "€"

print('\n')
unicode_test('\u2603')    #ASCII货币字符
# value = "☃",
# name = "SNOWMAN",
# value2 = "☃"


## Python3中Unicode字符串用法
# \u及4个十六进制的数字：从Unicode256个基本多语言平面中指定某一特定字符
# \U及8个十六进制的数字，最左为0
# \N{name}引用某一字符，name为该字符标准名称

import unicodedata
print('\n')

print(unicodedata.name('\u00e9'))
# LATIN SMALL LETTER E WITH ACUTE

print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE'))
# é

place = 'caf\u00e9'
print(place)
# café

place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(place)
# café

print('\n')

## Unicode字符名称索引页列出的字符名称是经过修改的，与name()得到的有所不同。
## 真实的Unicode名称需要将逗号舍去，并将逗号后面的内容移到最前面
## E WITH ACUTE, LATIN SMALL LETTER 改为 LATIN SMALL LETTER E WITH ACUTE

## len可计算字符串中Unicode字符的个数，而不是字节数
print(len('$'))     #1
print(len('\U0001f47b'))    # 1
print('\n')

## UTF-8编码和解码，动态为每个Unicode字符分配1-4个字节

place = 'caf\u00e9'
print(type(place))
print('\n')

# 编码
place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))
print('\n')

# 解码
place2 = place_bytes.decode('utf-8')
print(place)
print(type(place))
print('\n')

# 尝试其他解码方式
place4 = place_bytes.decode('latin-1')
print(place4)
place5 = place_bytes.decode('windows-1252')
print(place5)
print('\n')


## %格式化
n = 42
f = 7.03
s = 'string cheese'

str1 = '%d %f %s' % (n, f, s)               #常规格式
str2 = '%10d %10f %10s' % (n, f, s)         #最小域宽10个字符，右对齐
str3 = '%-10d %-10f %-10s' % (n, f, s)      #最小域宽10个字符，左对齐
str4 = '%10.4d %10.4f %10.4s' % (n, f, s)   #最小域宽10个字符，右对齐，字符宽度4
str5 = '%.4d %.4f %.4s' % (n, f, s)         #取消最小域宽，字符宽度4
str6 = '%*.*d %*.*f %*.*s' % (6, 4, n, 6, 4, f, 6, 4, s)         #将最小域宽，字符宽度设置为参数



print(str1)
print('\n')
print(str2)
print('\n')
print(str3)
print('\n')
print(str4)
print('\n')
print(str5)
print('\n')
print(str6)
print('\n')


## %格式化
form1 = '{} {} {}' . format(n, f, s)
form2 = '{2} {0} {1}' . format(f, s, n)    #传入参数的顺序
form3 = '{n} {f} {s}' . format(n = 42, f = 7.03, s = 'string cheese')

d = {'n': 42, 'f': 7.03, 's': 'string cheese'}
#0代表dict，1代表‘other’
form4 = '{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other')   
 
#位置参数
form5 = '{0:d}{1:f}{2:s}' . format(n, f, s)

#命名参数
form6 = '{n:d}{f:f}{s:s}' . format(n = 42, f = 7.03, s = 'string cheese')
 
#设置最小域宽，默认右对齐
form7 = '{0:10d}{1:10f}{2:10s}' . format(n, f, s)

#设置最小域宽，>右对齐
form8 = '{0:>10d}{1:>10f}{2:>10s}' . format(n, f, s)

#设置最小域宽，<左对齐
form9 = '{0:<10d}{1:<10f}{2:<10s}' . format(n, f, s)

#设置最小域宽，^居中
form10 = '{0:^10d}{1:^10f}{2:^10s}' . format(n, f, s)

#设置精度，1.无法对整型设置精度 2.浮点数仍代表小数点后位数 3.字符串最大字符个数
form11 = '{0:>10d}{1:>10.4f}{2:>10.4s}' . format(n, f, s)

print(form1)
print(form2)
print(form3)
print(form4)
print(form5)
print(form6)
print(form7)
print(form8)
print(form9)
print(form10)
print(form11)
print('\n')

#填充字符,替代空格。放在:之后，其他任何排版符之前
bigsale = '{0:!^20s}'.format('BIG SALE')
print(bigsale)

## 正则表达式
import re

result = re.match('You', 'Young Frankenstein')    #You是模式，YoungF是源
print(result.group())    ## You


#先对模式进行编译以加快匹配速度
youpattern = re.compile('You')
#利用编译好的模式进行匹配
result = youpattern.match('Young Frankenstein')


## 1.使用match()进行准确匹配
import re
source = 'Young Frankenstein'
m = re.match('You', source)   #从源字符串的开头开始匹配
if m:       #匹配成功返回了对象，将它输出看看匹配得到的是什么
    print(m.group())

m = re.match('^You', source)   #起始锚点也能起到同样作用
if m:       
    print(m.group())

m = re.match('Frank', source)   #从源字符串的开头开始匹配
if m:       #什么也没有返回。match只能检验以模式串作为开头的源字符串
    print(m.group())

m = re.search('Frank', source)   #search可以检测任何位置的匹配
if m:       #什么也没有返回。match只能检验以模式串作为开头的源字符串
    print(m.group())


#.代表任一单一字符 *代表任意一个他之前的字符，.*代表任意多个字符（含0个）
m = re.match('.*Frank', source)   
if m:       #匹配成功
    print(m.group())

print('\n')

## 2.使用search()寻找首次匹配
import re
source = 'Young Frankenstein'
m = re.search('Frank', source)   #任意位置寻找模式'Frank'，无需通配符.*
if m:       #匹配成功返回了对象，将它输出看看匹配得到的是什么
    print(m.group())

print('\n')

## 3.使用findall()寻找所有匹配
import re
source = 'Young Frankenstein'
m = re.findall('n', source)   #任意位置寻找模式'Frank'，无需通配符.*
print(m)    # ['n', 'n', 'n', 'n']
print('Found', len(m), 'matches')

print('\n')

# 将模式改成'n'后紧跟任意一个字符
import re
source = 'Young Frankenstein'
m = re.findall('n.', source)   #.代表任意单一字符
print(m)    # ['ng', 'nk', 'ns']
print('Found', len(m), 'matches')

print('\n')

# 将模式改成'n'后紧跟任意一个字符，并可选
import re
source = 'Young Frankenstein'
m = re.findall('n.?', source)   #.代表任意单一字符，?代表字符可选
print(m)    # ['ng', 'nk', 'ns', 'n']
print('Found', len(m), 'matches')

print('\n')



# 使用split()按匹配切分
import re
source = 'Young Frankenstein'
m = re.split('n', source)
print(m)    # ['You', 'g Fra', 'ke', 'stei', '']

print('\n')


# 使用sub()替换匹配
import re
source = 'Young Frankenstein'
m = re.sub('n','?', source)   #找到n，并用？替换
print(m)    # You?g Fra?ke?stei?

print('\n')



## 模式匹配
source = '''I wish I may, I wish I might
Have a dish of fish tonight.'''

m = re.findall('wish', source)
print(m)  # ['wish', 'wish']

m = re.findall('wish|fish', source) # 或
print(m)  #['wish', 'wish', 'fish']

m = re.findall('^wish', source) # 从字符串开头开始匹配
print(m)    #[]

m = re.findall('^I wish', source) # 从字符串开头开始匹配
print(m)    #['I wish']

m = re.findall('fish$', source) # 从字符串结尾开始匹配
print(m)    #[]

m = re.findall('fish tonight.$', source) # 从字符串结尾开始匹配,.代表任意单一字符
print(m)    #['fish tonight.']

m = re.findall('[wf]ish', source) # []或的意思
print(m)    #['wish', 'wish', 'fish']

m = re.findall('[wsh]+', source) # []或的意思
print(m)    #['w', 'sh', 'w', 'sh', 'h', 'sh', 'sh', 'h']

m = re.findall('ght\W', source) # 一个非字母非数字字符
print(m)    #['ght\n', 'ght.']

m = re.findall('I (?=wish)', source) # prev(?=next) 如果后面为next，返回prev
print(m)    #['I ', 'I ']

m = re.findall('(?<=I) wish', source) # (?<=prev)next 如果前面为prev，返回next
print(m)    #[' wish', ' wish']

m = re.findall('\bfish', source)    #\b代表空格，与正则表达式冲突
print(m)    #[]

m = re.findall(r'\bfish', source)    #r提示是正则表达式，\b提示单词边界
print(m)    #['fish']


## 定义匹配的输出
source = '''I wish I may, I wish I might
Have a dish of fish tonight.'''

m = re.search(r'(. dish\b).*(\bfish)', source) 
                #(单个字符 + dish + 单词边界)
                #.* 任意多个字符
                #(单词边界 + fish)
print(m.group())    #a dish of fish
print(m.groups())    #('a dish', 'fish')  #每个()以元组形式输出


#(?P<name>expr)  这样的模式会匹配expr，并将匹配结果存储到名为name的组中
m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())  #a dish of fish
print(m.groups())  #('a dish', 'fish')
print(m.group('DISH'))  #a dish

## struct模块将二进制数据结构转化成python中的数据结构

print(len('\x89PNG'))

import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' +\
       b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'

if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24])    #大端方案，L表示4字节无符号长整数
    print('Valid PNG, width', width, 'height', height)
else:
    print('Not a valid PNG')

print(width)

print(0x9a)


m1 = struct.pack('>L', 154)
m2 = struct.pack('>L', 141)
print(m1, m2)

m11 = struct.unpack('>L', m1)
m22 = struct.unpack('>L', m2)
print(m11)
print(m22)

m = struct.unpack('>16x2L6x', data) #大端，跳过16x，截取8字节，跳过6字节
print(m)


###################### 第7章习题 ######################

##1
print('\n第一题')
mystery = '\U0001f4a9'    #\u四位十六进制数    \U八位十六进制数
print(mystery)
print('\U0001f4a9' * 3)


import unicodedata
name = unicodedata.name(mystery)    # 接收Unicode字符，返回大写形式的名称。反向lookup()
print(name)

# 💩
# PILE OF POO

##2
print('\n第二题')
pop_bytes = mystery.encode('utf-8')   #编码
print(pop_bytes)    #字节型变量

#b'\xf0\x9f\x92\xa9'


##3
print('\n第三题')
pop_string = pop_bytes.decode('utf-8')   #解码
print(pop_string)    #字节型变量

#💩

##4
print('\n第四题')
poem = '''
    My kitty cat likes %s,
    My kitty cat likes %s,
    My kitty cat fell on his %s,
    And now thinks he's a %s''' % ('roast beef', 'ham', 'head', 'clam')
print(poem)

##5
print('\n第五题')
letter = '''Dear {}{},

            Thank you for your letter. We are sorry that 
            our {}{} in your {}.
            Please note that it should never be used in a {}, especially
            near any {}.
            
            Send us your receipt and {} for shipping and handling. 
            We will send you another {} that, in our tests, is 
            {}% less likely to have {}.
            
            Thank you for your support.
            
            Sincerely,
            {}
            {}'''.format(
            'salutation', 'name', 'product', 'verbed', 'room', 
            'room', 'animals', 'amount', 'product', 'percent',
            'verbed', 'spokesman', 'job_title')
print(letter)

##6
print('\n第六题')
reponse = {
    'salutation': 'salutation',
    'name': 'name',
    'product': 'product',
    'verbed': 'verbed',
    'room': 'room',
    'animals': 'animals',
    'amount': 'amount', 
    'product': 'product',
    'percent': 'percent',
    'spokesman': 'spokesman', 
    'job_title': 'job_title'}

letter = '''Dear {0[salutation]} {0[name]},

            Thank you for your letter. We are sorry that 
            our {0[product]}{0[verbed]} in your {0[room]}.
            Please note that it should never be used in a {0[room]}, especially
            near any {0[animals]}.
            
            Send us your receipt and {0[amount]} for shipping and handling. 
            We will send you another {0[product]} that, in our tests, is 
            {0[percent]}% less likely to have {0[verbed]}.
            
            Thank you for your support.
            
            Sincerely,
            {0[spokesman]}
            {0[job_title]}'''.format(reponse)
print(letter)

##7
print('\n第七题')
mammoth = '''
    We have seen thee, queen of cheese,
    Lying quietly at your ease,
    Gently fanned by evening breeze,
    Thy fair form no flies dare seize.
    
    All gaily dressed soon you'll go
    To the great Provincial show,
    To be admired by many a beau
    In the city of Toronto.
    
    Cows numerous as a swarm of bees,
    Or as the leaves upon the trees,
    It did require to make thee please,
    And stand unrivalled, queen of cheese.
    
    May you not receive a scar as
    We have heard that Mr. Harris
    Intends to send you off as far as
    The great world's show at Paris.
    
    Of the youth beware of these,
    For some of them might rudely squeeze
    And bite your cheek, then songs of glees
    We could not sing, oh! queen of cheese.
    
    We'rt thou suspended from balloon,
    You'd cast a shade even at noon,
    Folks would think it was the moon
    About to fall and crush them soon.'''
print(mammoth)

    

##8
print('\n第八题')
import re
c_start = re.findall(r'\bc\S*', mammoth)    # 单词边界，非空白符，任意多个
print(c_start)

#['cheese', 'city', 'cheese', 'cheek', 'could', 'cheese', 'cast', 'crush']

##9
print('\n第九题')
import re
c_start = re.findall(r'\bc\w\w\w\b', mammoth)    # 单词边界，字母或数字字符，单词边界
print(c_start)

##10
print('\n第十题')
import re
c_start = re.findall(r'\S*r\b', mammoth)    # 非空白符，任意多个，单词边界
print(c_start)

##11
print('\n第十一题')
import re
c_start = re.findall(r'\b[^aeiou\s]*[aeiou][^aeiou\s]*[aeiou][^aeiou\s]*[aeiou][^aeiou\s]*\b', mammoth)    # 非元音非空格字符、元音字符
print(c_start)

##12
print('\n第十二题')
str_16 = b'47494638396101000100800000000000ffffff21f9' +\
         b'0401000000002c000000000100010000020144003b'
         
import binascii
gif = binascii.unhexlify(str_16)
print(gif)

# b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\
# xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\
# x00\x00\x01\x00\x01\x00\x00\x02\x01D\x00;'

##13
print('\n第十三题')
valid_head = b'GIF89a'
if gif[:6] == valid_head:
    print('valid')
else:
    print('invalid')
    
    
##14
print('\n第十四题')
import struct
width = struct.unpack('>H', gif[6:8])
height = struct.unpack('>H', gif[8:10])
print(width,height)

print(gif[6])

###################### 第8章习题 ######################


##1
print('\n第一题')

test1 = 'This is a test of the emergency test system'

fileobj = open('test.txt', 'w')

fileobj.write(test1)

fileobj.close()

##2
print('\n第二题')

fin = open('test.txt','r')

test2 = fin.read()

print(test2)
# 'This is a test of the emergency test system'

print(test2 == test1)
# True


##3
print('\n第三题')

import csv
## 可避免‘，’自动分单元格问题
author = [
    ['author', 'book'],
    ['J R R Tolkien', 'The Hobbit'],
    ['Lynne Truss', '''"Eats, Shoots & Leaves"''']]

with open('books.csv', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(author)
    
    
##4
print('\n第四题')

import csv
with open('books.csv', 'rt') as fin:
    cin2 = csv.DictReader(fin, fieldnames = ['first', 'last'])
    books = [row for row in cin2]
    print(books)
    
## [
##  OrderedDict([('first', 'author'), ('last', 'book')]),
##  OrderedDict([('first', 'J R R Tolkien'), ('last', 'The Hobbit')]), 
##  OrderedDict([('first', 'Lynne Truss'), ('last', '"Eats, Shoots & Leaves"')])
##  ]


##5
print('\n第五题')
import csv

bookin = [
    ['title', 'author', 'year'],
    ['The Weirdstone of Brisingamen', 'Alan Garner', '1960'],
    ['Perdido Street Station', 'China Mi\u00e9ville', '2000'],
    ['Thud!', 'Terry Pratchett', '2005'],
    ['The Spellman Files', 'Lisa Lutz', '2007'],
    ['Small Gods', 'Terry Pratchett', '1992']]

## 加newline = '' 解决csv空行问题
with open('books.csv', 'w', newline = '') as fout:    #自动关闭
    csvout = csv.writer(fout)
    csvout.writerows(bookin)
 

 
##6
print('\n第六题')

import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''
    CREATE TABLE book(
    title text PRIMARY KEY,
    author text,
    year integer)''')
    
    
    
##7
print('\n第七题')

with open('books.csv', 'rt') as fin:
    csvin = csv.reader(fin)
    books = [row for row in csvin]
    
print(books)

ins = 'INSERT INTO book (title, author, year) VALUES(?, ?, ?)'
i = 0
while True:
    curs.execute(ins, books[i])
    i += 1
    if i == len(books):
        break


##8
print('\n第八题')

curs.execute('SELECT title FROM book ORDER BY title')

print(curs.fetchall())    # 接受全部返回结果

# [('Perdido Street Station',), 
#  ('Small Gods',), 
#  ('The Spellman Files',), 
#  ('The Weirdstone of Brisingamen',), 
#  ('Thud!',), 
#  ('title',)]
   
   
   
##9
print('\n第九题')

curs.execute('SELECT * FROM book ORDER BY year')

print(curs.fetchall())

# [('The Weirdstone of Brisingamen', 'Alan Garner', 1960), 
#  ('Small Gods', 'Terry Pratchett', 1992), 
#  ('Perdido Street Station', 'China Miéville', 2000), 
#  ('Thud!', 'Terry Pratchett', 2005), 
#  ('The Spellman Files', 'Lisa Lutz', 2007), 
#  ('title', 'author', 'year')]

curs.close()
conn.commit()
conn.close()

##10
print('\n第十题')

import sqlalchemy as sa

conn = sa.create_engine('sqlite:///books.db')   #表单一定要加primary key

# col_title = conn.execute('SELECT * FROM book')

col_title = conn.execute('SELECT title FROM book ORDER BY title')

for col in col_title:
    print(col)


# ('Perdido Street Station',)
# ('Small Gods',)
# ('The Spellman Files',)
# ('The Weirdstone of Brisingamen',)
# ('Thud!',)
# ('title',)




##11
print('\n第十一题')

import redis

conn = redis.Redis()     # 目标计算机积极拒绝。可能端口号不正确

# conn.keys('*')

# conn.hmset('test', {'count': 1, 'name': 'Fester bestertester'})

# conn.hkeys('test')

##12

import urllib.request as ur

url = 'http://www.iheartquotes.com/api/v1/random'

conn = ur.urlopen(url)



## 杨辉三角
def triangles():
    N = [1]
    while True:
        yield N
        N.append(0)    # 尾部添0，首尾相加 len长度增1
        N = [N[i - 1] + N[i] for i in range(len(N))]  #[-1][0] +..+ [len-2][len-1]
 
 
m = triangles()

for i in range(10):
        print(next(m))

        
        
## 斐波那契数列
def fib():
    a, b, c = 0, 0, 1
    while True:
        yield c
        b, c = c, b + c


m = fib()

for i in range(6):
    print(next(m))


## 汉诺塔
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)

        
move(3,'A', 'B', 'C')

#高阶函数
def add(x, y, f):
    return f(x) + f(y)
    
print(add(-5, 6, abs))



# map 返回一个迭代器，变量函数只有1个变量
def f(x):
    return x**2
    
r = map(f, [1, 2, 3, 4, 5])
print(r)    # <map object at 0x000001B3A19630B8>
print(list(r))



# reduce  返回一个值，变量函数需有2个变量

def f(x, y):
    return x * 10 + y
    
m = reduce(f, [1, 2, 3, 4, 5])
print(m)


## 字符串转int

# 单个字符变单个数字
def char2num(s):
    dicts = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }
    return dicts[s]

# reduce中连续作用函数    
def f(x, y):
    return x * 10 + y

test = reduce(f,map(char2num, '1234567'))    # str为Iterator
print(test)

print('\nover\n')



## 函数形式

Dicts = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }
    
def str2int(str):
    def char2num(s):
        return Dicts[s]
        
    return reduce(lambda x,y: x * 10 + y, map(char2num, str))

print(str2int('345678'))


# 首字母大写，其他小写的规范名字

def normalize(name):
        return (name.lower()).capitalize()
        
L1 = ['adam', 'LISA', 'barT']

L2 = list(map(normalize, L1))

print(L2)



# 求序列的乘积
def prod(L):
    def fn(x, y):
        return x * y

    return reduce(fn, L)

print(prod([3, 5, 7, 9]))



# 转化成浮点数
def str2float(str):
    def strsplit(s):
        x, y = [], []
        for i in s:
            if i == '.':
                y = x    # y为整数部分，x为小数部分
                x = []
                continue
            x.append(i)
        return y, x[::-1]
                                
    def char2num(s):
        Dicts = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }
        return Dicts[s]
        
    int_num, float_num = strsplit(str)
    
    print(int_num)
    print(float_num)
    
    return reduce(lambda a1,a2:a1 * 10 + a2, map(char2num, int_num)) + 0.1 * reduce(lambda a1,a2:a1 * 0.1 + a2, map(char2num, float_num))

    
print(str2float('123.456'))



## 素数计算

## 计算素数的一个方法是埃氏筛法
# 首先，列出从2开始的所有自然数，构造一个序列
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉
# 不断筛下去，就可以得到所有的素数。

# 先构造一个从3开始的奇数序列
def _odd_iter():
    n = 3
    while True:
        yield n
        n += 2
        
# 然后定义一个筛选函数：筛选出非n的倍数
def _not_divisible(n):
    return lambda x: x % n > 0

# 最后，定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()    # 初始序列,3开始。默认2输出，2的倍数已过滤
    while True:
        n = next(it)
        yield n     # 返回序列的第一个数
        it = filter(_not_divisible(n), it)  #构造新序列，筛掉n的倍数

for i in primes():
    print(i)
    if i > 100:
        break
        
print('\nover\n')


## 判断是否素数       
def is_primes(n):
    prime = []
    for i in primes():
        prime.append(i)
        if i > n:
            break
    return n in prime      

    
print('\n') 

## 1000以内的素数
list = []
   
for i in primes():
    if i > 1000:
        break
    list.append(i)
    
print(list)
    
    
## 孪生素数
for i in list:
    if i + 2 in list:
        print((i, i + 2))

    
## 回文数筛选
def is_palindrome(n):
    return str(n) == str(n)[::-1]
    

output = filter(is_palindrome, range(1,1000))

print(list(output))

print('\n')

if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
    
    
## 排序

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

def by_score(t):
    return t[-1]
    
L2 = sorted(L, key=by_name)
print(L2)
 
L2 = sorted(L, key=by_score, reverse = True)
print(L2)


## 闭包返回一个计数器函数

def createCounter():
    fs = [0]
    def counter():
        fs[0] = fs[0] + 1
        return fs[0]
    return counter

    
counterA = createCounter()

print(counterA(), counterA(), counterA(), counterA())
 
counterB = createCounter()
print(counterB(), counterB(), counterB(), counterB())

print('\nover\n')


## 闭包返回一个计数器函数

def createCounter():
    def f():
        i = 0
        while True:
            i += 1
            yield i
    
    sum = f()
    
    def counter():
        return next(sum)
    
    return counter

    
counterA = createCounter()

print(counterA(), counterA(), counterA(), counterA())
 
counterB = createCounter()
print(counterB(), counterB(), counterB(), counterB())


## 匿名函数 只能有一个表达式，不用写return，返回值就是该表达式的结果

is_odd = lambda n: n % 2 == 1

L = list(filter(is_odd, range(1,20)))

print(L)


# 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间

import functools, time

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        t_start = time.time()
        fn(*args, **kw)
        t_end = time.time()
        print('%s executed in %s ms' % (fn.__name__, t_end - t_start))
        return fn(*args, **kw)
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;
    
f = fast(11, 22)
s = slow(11, 22, 33)

print(f)
print(s)    

# 在函数调用的前后打印出'begin call'和'end call'的日志
def log(func):
    def wrapper(*args, **kw):
        print('begin call')
        f = func(*args, **kw)
        print('end call')
        return f
    return wrapper


@log
def plusaa(a, b):   #似乎装饰器只能针对print型函数，不适用return
    print(a + b)
    
plusaa(1, 4)


# 对象隐藏参数

class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
        
    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('bad gender')

bart = Student('Bart', 'male')

if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
        
print(dir(bart))
       
# 类属性，每创建一个实例，该属性自动增加

class Student(object):
    count = 0
    
    def __init__(self, name):
        self.__name = name
        Student.count += 1

print(Student.count)
        
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
            


# @property添加属性和只读属性
class Screen(object):
    
    @property
    def width(self):
        return self._width
        
    @width.setter
    def width(self, value):
        self._width = value
        
    @property
    def height(self):
        return self._height
        
    @height.setter
    def height(self, value):
        self._height = value
    
    @property
    def resolution(self):
        return self._height * self._width
            

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
    

# 使用__slots__

class Student(object):
    __slots__ = ('name', 'gender')

s = Student()        

s.name = 'Garry'

print(s)

s.gender = 'male'

print(s)

s.score = '66'

# AttributeError: 'Student' object has no attribute 'score'


# 枚举类
from enum import Enum

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
    
# Jan => Month.Jan , 1
# Feb => Month.Feb , 2
# Mar => Month.Mar , 3
# Apr => Month.Apr , 4
# May => Month.May , 5
# Jun => Month.Jun , 6
# Jul => Month.Jul , 7
# Aug => Month.Aug , 8
# Sep => Month.Sep , 9
# Oct => Month.Oct , 10
# Nov => Month.Nov , 11
# Dec => Month.Dec , 12



# 派生自定义
from enum import Enum, unique

@unique     #检查保证没有重复值  
class Month(Enum):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12

#name: Jan   member: Month.Jan   value: 1    (整体为一个items())

# 通过成员的名称来获取成员
# Month['Jan']

# 通过成员值来获取成员
# Month(2)

# 通过成员，来获取它的名称和值
# jan_member = Month.Jan
# jan_member.name
# jan_member.value

day1 = Month.Jan
print(day1)
print(Month['Sep'])
print(Month.Jan.value)

# 枚举类，避免使用字符串

from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1
    
class Student(object):      # 不存在继承关系
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)

if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
    
    
# 调试    
import logging
logging.basicConfig(level = logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10/n)

# 调试    
import pdb

s = '0'
n = int(s)
pdb.set_trace()
print(10/n)



from mydict import Dict

d = Dict(a = 1, b = 2)

print(d['a'])

print(d.a)

b = Dict()
b['m'] = 5
print(b.m)

print(isinstance(d,dict))
print(isinstance(b,dict))
print('m' in b)

# print(b['n'])

# print(b.n)



# doctest 内部代码测试

def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    
# IO 相同目录下
with open('test.txt', 'r') as f:
    print(f.read())
    
    
# 读取二进制文件，图片、视频等
with open('大屏.jpg', 'rb') as f:
    print(f.read())

    
# 读取非UTF-8编码的文本文件
with open('test2.txt', 'r', encoding = 'gbk') as f:
    print(f.read())

# 夹杂非法编码字符
with open('test2.txt', 'r', encoding = 'gbk', errors = 'ignore') as f:
    print(f.read())
    
# 追加写入 'a'
with open('test.txt', 'a') as f:
    f.write(' hello hi!')
    

from io import StringIO     # 只能操作str
from io import BytesIO      # 操作二进制数据

# 写入str
f = StringIO()      # 打开StringIO
    
f.write('hello')        #第一次写入
f.write(' ')        #第二次写入
f.write('world!')        #第三次写入

print(f.getvalue())     # 读取

# 读取str
f = StringIO('Hello!\nHi\nGoodbye!')    #用str初始化一个StringIO
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())    # 踢出\n
    

# 写入二进制
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# 读取二进制
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')    # 用bytes初始化BytesIO
print(f.read())

import os, time
# 计算目录下的文件数
def file_num(di, n):    #di 为当前目录    n为准备访问
    sub_path = os.path.join(di, n)  #合成待访问路径
    if os.path.isfile(sub_path):    # 如果待访问为文件，记为1
        return 1
    else:
        fileNum = 0
        if os.path.isdir(sub_path):     # 如果是一个路径       
            subli = os.listdir(sub_path)    # 获取路径下所有文件
            for x in subli:
                if os.path.isfile(x):   # 是文件则 +1
                    fileNum += 1
                else:
                    fileNum = fileNum + file_num(sub_path, x) # 如果是一个目录
        return fileNum

# 方法2
def file_num2(dir):
    if os.path.isfile(dir):
        return 1
     elif os.path.isdir(dir):
        filenum = 0
        subli = os.listdir(dir)
        for x in subli:
            if os.path.isfile(x):
                filenum += 1
            else:
                newdir = os.path.join(dir, x)
                filenum = filenum + file_num2(newdir)
        return filenum

# 打印dir -l输出内容
dir = 'E:\\学海无涯\\pythonLearning'
def dir_L():
    li = os.listdir(dir)    # 获取目录下所有内容
    # 目标打印样式
    print('mode\tnlike\tfilenum\tuser_id\tgroup_id\tsize\tmonth\tday\ttime\tfilename\t')
    print(li)
    for n in li:
        attrTuple = os.stat(n)
        '''
        os.stat_result(
        st_mode=33206, 
        st_ino=4785074604179011, 
        st_dev=10461841, 
        st_nlink=1, 
        st_uid=0, 
        st_gid=0, 
        st_size=208, 
        st_atime=1530777169, 
        st_mtime=1530777169, 
        st_ctime=1530685403)
        '''
        print(str(attrTuple.st_mode) + '\t', end = '')
        print(str(attrTuple.st_nlink) + '\t', end = '')
        fileNum = file_num(dir, n)
        print(str(fileNum) + '\t', end = '')
        print(str(attrTuple.st_uid) + '\t', end = '')
        print(str(attrTuple.st_gid) + '\t', end = '')
        print(str(attrTuple.st_size) + '\t', end = '')
        timeTuple = time.localtime(attrTuple.st_mtime)
        '''
        time.struct_time(
        tm_year=2018, 
        tm_mon=7, tm_mday=5, tm_hour=15, tm_min=52, 
        tm_sec=49, tm_wday=3, tm_yday=186, tm_isdst=0)
        '''
        print(str(timeTuple.tm_mon) + '月\t', end = '')
        print(str(timeTuple.tm_mday) + '\t', end = '')
        print(str(timeTuple.tm_hour) + ':' + str(timeTuple.tm_min) + '\t', end = '')
        print(n + '\t')

dir_L()



## 系统参数查看

os.name
# 'nt'  -- windows    'posix'  ---Linux/Unix/Max OS X

# 详细系统信息
os.uname()
# windows上不提供

# 获取环境变量
os.environ

# 获取某个环境变量
os.environ.get('PATH')

# 获取当前目录绝对路径
s.path.abspath('.')
# 'E:\\学海无涯\\pythonLearning'


## 操作文件和目录

# 目录下创建新目录
# 1> 先将新目录完整路径表示出来:仅修改了字符串，便于正确处理不同操作系统的路径分隔符
os.path.join('E:\\学海无涯\\pythonLearning', 'new_test')
#'E:\\学海无涯\\pythonLearning\\new_test'

# 2> 创建一个新目录。
os.mkdir('E:\\学海无涯\\pythonLearning\\new_test')

# 删除一个目录
os.rmdir('E:\\学海无涯\\pythonLearning\\new_test')

# 拆分路径
# 同样仅操作了字符串，后一部分总是最后级别目录或文件名
os.path.split('E:\\学海无涯\\pythonLearning')
# ('E:\\学海无涯', 'pythonLearning')

# 获取文件扩展名
os.path.splitext('E:\\学海无涯\\pythonLearning\\books.csv')
# ('E:\\学海无涯\\pythonLearning\\books', '.csv')

# 重命名
os.rename('testtest.py', 'test.txt')
# 删除文件
os.remove('test.py')

# 目录下所有文件
os.listdir()
    '''
    ['books.csv', 
    'books.db', 'learning.py', 'mydict.py', 'mydict_test.py', 
    'new.py', 'stat属性.py', 'test.py', 'test.txt', 'test0522.py', 
    'test2.txt', 'thestudent.py', 'thestudent_test.py', 'zoo.py', 
    '__pycache__', '大屏.jpg']
    '''

## 过滤目录下目录/文件
[x for x in os.listdir() if os.path.isdir(x)]
# ['__pycache__']

[x for x in os.listdir() if os.path.isfile(x)]
# ['books.csv', 'books.db', 'learning.py', 'mydict.py', 'mydict_test.py', 'new.py', 'stat属性.py', 'test.py', 'test.txt', 'test0522.py', 'test2.txt', 'thestudent.py', 'thestudent_test.py', 'zoo.py', '大屏.jpg']

# 在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，
# 并打印出相对路径
def search_str(dir, str):   #在dir路径下寻找字符串str
    if os.path.isfile(dir):
        filename = os.path.split(dir)[1]    # 注意此处是tuple
        if re.search(str, filename) != None:    # None为没找到
            print(filename, ':', dir)
    elif os.path.isdir(dir):
        subli = os.listdir('.')
        for x in subli:
            dir_this = os.path.join(dir, x) # 获取文件完整路径
            if re.search(str, x) != None:
                print(x, ':', dir_this)
            else:
                search_str(dir_this, str)
    return 0

search_str('E:\\学海无涯\\pythonLearning', 'tes')

## json与python的转化    
# dumps()返回一个str，为标准jason(utf-8)
import json
    
obj = dict(name = '小明', age = 20)
s = json.dumps(obj, ensure_ascii = True)
# '{"name": "\\u5c0f\\u660e", "age": 20}'


d = dict(name='Bob', age=20, score=88)
json.dumps(d)
# '{"age": 20, "score": 88, "name": "Bob"}'


## 反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)
# {'age': 20, 'score': 88, 'name': 'Bob'}


## 跨平台的多进程调用
from multiprocessing import Process

def run_proc(name): #执行函数
    print('Run child process %s(%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))    #创建子进程：传入执行函数和函数参数
    print('Child process will start.')
    p.start()   # 子进程启动
    p.join()    #等待子进程结束后再继续往下运行，用于进程间同步
    print('Child process end.')
    
    
'''
Parent process 5356.
Child process will start.

over

Run child process test(14624)...
Child process end.

over
'''


## Only works on Unix/Linux/Mac:
print('Process (%s) start...' % os.getpid())    #获取当前进程ID

pid = os.fork() #调用一次，返回两次。复制当前进程，分别在父进程和子进程内返回。
if pid == 0:    # 子进程内返回0
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:   # 父进程内返回子进程id
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

    
## 利用进程池，批量创建子进程
def long_time_task(name):
    print('Run task %s(%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() *3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
    
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4) # 可以同时跑4个进程，默认大小为CPU核数
    for i in range(5):
        p.apply_async(long_time_task, args = (i,))
    print('Waiting for all subprocesses done...')
    p.close()   # 调用后不能添加新的Process
    p.join()    # 会等待所有子进程执行完毕 必须先调用p.close()
    print('All subprocesses done.')

    '''
Parent process 1480.
Waiting for all subprocesses done...
Run task 0(15940)
Run task 1(1996)
Run task 2(14464)
Run task 3(3708)
Task 0 runs 0.11 seconds.
Run task 4(15940)
Task 3 runs 0.56 seconds.
Task 2 runs 0.83 seconds.
Task 1 runs 2.77 seconds.
Task 4 runs 2.88 seconds.
All subprocesses done.
    '''
    
    
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)


from multiprocessing import Process, Queue

## 进程间通信

# 写数据进程 to Queue
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程 get Queue
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

# 主程序
if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target = write, args = (q,))
    pr = Process(target = read, args = (q,))
    # 启动子进程pw，写入
    pw.start()
    # 启动子进程pw,读取
    pr.start()
    # 等待pw结束
    pw.join()
    # pr是死循环，只能强行终止
    pr.terminate()
    
'''
Process to write: 10572
Put A to queue...
Process to read: 9400
Get A from queue.
Put B to queue...
Get B from queue.
Put C to queue...
Get C from queue.
'''    
    

## 线程调度 

import time, threading

# 新线程执行的代码
def loop():
    # threading.current_thread() 永远返回当前线程的实例
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


# 默认启动主线程，主线程可以启用新的线程
print('thread %s is running...' % threading.current_thread().name)
#   启动一个线程：传入一个函数、线程名，来创建Thread实例
t = threading.Thread(target = loop, name = 'LoopTread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

    
'''
thread MainThread is running...
thread LoopTread is running...
thread LoopTread >>> 1
thread LoopTread >>> 2
thread LoopTread >>> 3
thread LoopTread >>> 4
thread LoopTread >>> 5
thread LoopTread ended.
thread MainThread ended.
'''    
        
        
        
## 线程锁定
balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(10000):
        # 获取锁
        lock.acquire()
        try:
            # 放心改
            change_it(n)
        finally:            # try... finally 来确保锁一定会释放
            # 释放锁
            lock.release()
            
            
# 计算cpu内核数
 multiprocessing.cpu_count()         # 4  
 
 
 # 创建全局ThreadLocal对象：
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
    
def process_thread(std):
    # 绑定ThreadLocal的student
    local_school.student = std
    process_student()
    
t1 = threading.Thread(target = process_thread, args = ('Alice',), name = 'Thread-A')
t2 = threading.Thread(target = process_thread, args = ('Bob',), name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()


'''
Hello, Alice (in Thread-A)
Hello, Bob (in Thread-B)
'''

## 正则表达式 
re.match(r'^\d{3}\-\d{3,8}$', '010-12345')

# <_sre.SRE_Match object; span=(0, 9), match='010-12345'>

re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
# match匹配成功，返回一个match对象；匹配失败，返回None

## 用正则表达式切分字符串，可以识别连续空格
'a b   c'.split(' ')
# ['a', 'b', '', '', 'c']

re.split(r'\s+', 'a b   c')
# ['a', 'b', 'c']

re.split(r'[\s\,]+', 'a,b, c  d')
# ['a', 'b', 'c', 'd']

re.split(r'[\s\,\;]+', 'a,b;; c  d')
# ['a', 'b', 'c', 'd']

# 可将不规范的输入转化成正确的数组


## 利用分组提取子串
# 用()表示要提取的分组

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
m
# <_sre.SRE_Match object; span=(0, 9), match='010-12345'>
m.group(0)   # 永远是原始字符串
# '010-12345'
m.group(1)
# '010'
m.group(2)
# '12345'
m.groups()
# ('010', '12345')

# 正则匹配默认贪婪匹配，增加'?'可以变为非贪婪匹配
# 寻找数字后面的0
re.match(r'^(\d+)(0*)$', '102300').groups()
# ('102300', '')

re.match(r'^(\d+?)(0*)$', '102300').groups()
#('1023', '00')

# 1.re编译正则表达式，如果不合法，报错
# 2.编译后的正则表达式去匹配字符串
# 于是，可以先预编译正则表达式，以便提高重复使用效率

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

re_telephone.match('010-12345').groups()
# ('010', '12345')

re_telephone.match('010-8086').groups()
# ('010', '8086')


## 简单识别电子邮件地址 注意+的使用
def is_valid_email(addr):
    if re.match(r'^([a-zA-Z0-9.]+)(@)([a-zA-Z]+)(.)(com|cn|org)$', addr):
        return True
    else:
        return False
...
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
assert is_valid_email('mr-bob@example.com')


## 提取带名字的email地址
def name_of_email(addr):
    m1 = re.match(r'^([a-zA-Z0-9.]*)(<)([a-zA-Z0-9.\s]+)(>)([a-zA-Z0-9.]*)(@)([a-zA-Z]+)(.)(com|org|cn)$', addr)
    m2 = re.match(r'^([a-zA-Z0-9.]+)(@)([a-zA-Z]+)(.)(com|cn|org)$', addr)
    if m1 != None:
        return m1.group(3)
    elif m2 != None:
        return m2.group(1)
    else:
        return None

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')


## 时间、时区换算

now = datetime.now()
print(now)

print(type(now))

# 2018-08-17 12:06:24.810848    #当前日期和时间
# <class 'datetime.datetime'>    # datetime类型


# 在计算机中，时间实际上是用数字表示的。 ——相对于epoch time的秒数
'''
把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0
（1970年以前的时间timestamp为负数）
timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
对应的北京时间是
timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
'''

dt = datetime(2015, 4, 19, 12, 20)
dt.timestamp()              # 1429417200.0

# datetime是有时区的，timestamp为浮点数没有时区概念。
t = 1429417200.0
datetime.fromtimestamp(t)   #本地时间
# datetime.datetime(2015, 4, 19, 12, 20)

datetime.utcfromtimestamp(t)    #直接转换到标准时区
# datetime.datetime(2015, 4, 19, 4, 20)

# 把str转换成datetime    '%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
# 2015-06-01 18:19:59     #转换后的datetime是没有时区信息的


## 将datetime转换为str
cday
# datetime.datetime(2015, 6, 1, 18, 19, 59)
cday.strftime('%a, %b %d %H:%M')
# 'Mon, Jun 01 18:19'   


## datetime加减
now = datetime.now()
now
# datetime.datetime(2018, 8, 17, 15, 37, 32, 340094)
now + timedelta(hours = 10)
# datetime.datetime(2018, 8, 18, 1, 37, 32, 340094)
now - timedelta(days = 1)
# datetime.datetime(2018, 8, 16, 15, 37, 32, 340094)
now + timedelta(days = 2, hours = 12)
# datetime.datetime(2018, 8, 20, 3, 37, 32, 340094)

# 创建时区 UTC+8:00
tz_utc_8 = timezone(timedelta(hours = 8))
now = datetime.now() 
# datetime.datetime(2018, 8, 17, 15, 37, 32, 340094)
dt = now.replace(tzinfo = tz_utc_8)
dt
# datetime.datetime(2018, 8, 17, 15, 37, 32, 340094, tzinfo=datetime.timezone(datetime.timedelta(0, 28800)))
# 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。


## 时区转换
# 获取UTC时间
datetime.utcnow()
# datetime.datetime(2018, 8, 17, 7, 58, 40, 602124)
# 强制设置时区为UTC+0:00 (获知正确时区，并强制设置，作为基准时间)
utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc)
utc_dt
# datetime.datetime(2018, 8, 17, 8, 2, 46, 819200, tzinfo=datetime.timezone.utc)
print(utc_dt)
# 2018-08-17 08:02:46.819200+00:00

# astimezone()转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours = 8)))
print(bj_dt)
#2018-08-17 16:02:46.819200+08:00

# astimezone()转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours = 9)))
print(tokyo_dt)
#2018-08-17 17:02:46.819200+09:00

# astimezone()转换bj_dt时区为东京时间 任何带时区的datetime都可以转换
tokyo2_dt = bj_dt.astimezone(timezone(timedelta(hours = 9)))
print(tokyo2)
# 2018-08-17 17:02:46.819200+09:00


tz1 = 'UTC+5:00'
tz2 = 'UTC+12:00'
tz3 = 'UTC-4:00'
tz4 = 'UTC-11:00'

## 注意‘\+’‘\-’加减号特殊处理
## 注意贪婪匹配原则，1位数和2位数的处理顺序
m = re.match('^(UTC)(\+|\-)(1[0-2]+|[0-9]+)(:00)$',tz2)
m.groups()
# ('UTC', '+', '5', ':00')
m = re.match('^(UTC)(\+|\-)(1[0-2]+|[0-9]+)(:00)$',tz2)
m.groups()
# ('UTC', '+', '12', ':00')
m = re.match('^(UTC)(\+|\-)(1[0-2]+|[0-9]+)(:00)$',tz3)
m.groups()
# ('UTC', '-', '4', ':00')
 m = re.match('^(UTC)(\+|\-)(1[0-2]+|[0-9]+)(:00)$',tz4)
m.groups()
# ('UTC', '-', '11', ':00')

# 输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，
# 均是str，编写一个函数将其转换为timestamp
def to_timestamp(dt_str, tz_str):
    # 获取时区信息
    m = re.match('^(UTC)(.[0-9]|.1[0-2])(:00)$', tz_str)
    delta_t = int(m.group(2))
    # 设置时区
    tz_utc = timezone(timedelta(hours = delta_t))
    # 获取时间信息
    dt_time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # 更新时间的时区信息
    tz_time = dt_time.replace(tzinfo = tz_utc)
    # 返回时间戳
    print(tz_time.timestamp())
    return True

to_timestamp('2015-6-1 8:10:30', 'UTC+5:00')
# print('\nover\n')
to_timestamp('2015-6-1 3:10:30', 'UTC+0:00')
# print('\nover\n')
to_timestamp('2015-5-31 22:10:30', 'UTC-5:00')
# print('\nover\n')

# 1433128230.0

## 命名tuple：namedtuple('名称', [属性list]):
# 创建一个namedtuple
Circle = namedtuple('Circle', ['x', 'y', 'r'])
# 创建1个实例
c = Circle(1, 2 ,3)
# c.x   c.y   c.r

## 双向队列deque([list])
q = deque(['a','b','c'])
q.append('x')
# deque(['a', 'b', 'c', 'x'])
q.appendleft('y')
# deque(['y', 'a', 'b', 'c', 'x'])
q.pop()
#deque(['y', 'a', 'b', 'c'])
q.popleft()
#deque(['a', 'b', 'c'])


## 默认字典defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
dd['key1']
# 'abc'
dd['key2']
# 'N/A'

## 有序字典 按照插入顺序排列，不是key本身排序
# 无序
d = dict([('a', 1),('b', 2),('c', 3)])
# {'a': 1, 'b': 2, 'c': 3}
# 有序
od = OrderedDict([('a',1),('b',2),('c',3)])
# OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict()
od['z'] = 2
od['y'] = 3
od['x'] = 1
# OrderedDict([('z', 2), ('y', 3), ('x', 1)])


## OrderedDict实现一个IFIO（先进先出）的dict，容量超出，删除最早添加
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
    
    # 初始化 容量
    def __inin__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity
        
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last = False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

## 有报错        
d = OrderedDict([('a', 1), ('c', 3), ('b', 2)])
m = LastUpdatedOrderedDict(d, 3)


# 计数器 实际上也是一个dict的子类
c = Counter()
for ch in 'programming':
    c[ch] += 1
    

# Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})


## 请写一个能处理去掉=的base64解码函数：
def safe_base64_decode(s):
    
    print(type(s))
    l = len(s)
    if l % 4 == 0:
        result = base64.b64decode(s)
    elif l % 4 == 1:
        result = base64.b64decode(s + b'===')
    elif l % 4 == 2:
        result = base64.b64decode(s + b'==')
    elif l % 4 == 3:
        result = base64.b64decode(s + b'=')
    
    print(result)
    
safe_base64_decode(b'YWJjZA==')
safe_base64_decode('YWJjZA==')
safe_base64_decode(b'YWJjZA')
safe_base64_decode('YWJjZA==')

'''
BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
一个4字节整数：表示位图大小；
一个4字节整数：保留位，始终为0；
一个4字节整数：实际图像的偏移量；
一个4字节整数：Header的字节数；
一个4字节整数：图像宽度；
一个4字节整数：图像高度；
一个2字节整数：始终为1；
一个2字节整数：颜色数。
'''

bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

print(type(bmp_data))

def bmp_info(data):
    t = struct.unpack('<ccIIIIIIHH', data[:30])
    print(t)
    if t[:2] == (b'B', b'M'):
        return {
            'size': t[2],
            'width': t[6],
            'height': t[7],
            'color': t[9]
        }
    else:
        return False
        

bi = bmp_info(bmp_data)

assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16


## 摘要函数f()，对任意长度的data计算出固定长度的摘要digest
## 单向函数 得到16进制字符串，固定长度

# MD5，32位16进制字符串
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
# d26a53750bc40b38b65a520292f69306


md6 = hashlib.md5()
md6.update('how to use md6 in '.encode('utf-8'))
md6.update('python hashlib?'.encode('utf-8'))
print(md6.hexdigest())
# 4705aba440e9ba0756fdcbd7d80936d0


# SHA1，40位16进制字符串
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib'.encode('utf-8'))
print(sha1.hexdigest())
# e9282e41aaf5ef53fd4ca3c191ed1e2546dbf3f2



# 根据用户输入的口令，计算出存储在数据库中的MD5口令
# 存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
    }
    

def login(user, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    if md5.hexdigest() == db[user]:
        return True
    else:
        return False
        
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')


# 常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5
# 这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”


# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5
def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
    

# 效果同 md5(), md5.update(),md5.hexdigest()
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()
    
# chr(<数值表达式>) 返回String 表达式取值0-255
# 类定义
class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join(chr(random.randint(48, 122)) for i in range(20))
        self.password = get_md5(password + self.salt)
        

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
    }



def login(username, password):
    user = db[username]
    salt = user.salt
    return user.password == get_md5(password + salt)



assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')


# msg,key 都必须是bytes类型,str类型需先编码
message = b'Hello, world!'
print(message[:4])
key = b'secret'
h = hmac.new(key, message, digestmod = 'MD5')

# 长字符串可多次调用‘hmac.update(msg)’
hh = hmac.new(key, message[:4], digestmod = 'MD5')
hh.update(message[4:])

print(h.hexdigest())
print(hh.hexdigest())


## 改变为hmac算法
# str类型输入，需先编码后调用
def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), digestmod = 'MD5').hexdigest()
    
# chr(<数值表达式>) 返回String 表达式取值0-255
# 类定义
class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join(chr(random.randint(48, 122)) for i in range(20))
        self.password = hmac_md5(self.key, password)
        

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
    }



def login(username, password):
    user = db[username]
    key = user.key
    return user.password == hmac_md5(key, password)



assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')


# 无限迭代器
naturals = itertools.count(1)
# takewhile()函数截取有限序列
ns = itertools.takewhile(lambda x: x < 10, naturals)
list(ns)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# chain()可以把一组迭代对象串联起来，变成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
     print(c)

'''
A
B
C
X
Y
Z
'''

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

A ['A', 'A', 'A']
B ['B', 'B', 'B']
C ['C', 'C']
A ['A', 'A', 'A']

# 忽略大小写
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

A ['A', 'a', 'a']
B ['B', 'B', 'b']
C ['c', 'C']
A ['A', 'A', 'a']


def pi(N):

    # 创建一个序列，取该序列的前2N-1项
    _list = itertools.count(1)
    list_n = list(itertools.takewhile(lambda x: x < 2 * N, _list))
    
    # print(list_n)
    
    # 取一个奇数序列
    list_odd = list(filter(lambda x: x % 2 == 1, list(list_n)))
    
    # print(list_odd)
    
    # 添加±并用4除    
    def fn(x):
        if x % 4 == 1:
            return 4 / x
        elif x % 4 == 3:
            return -4/x
            
    list_ = list(map(fn, list_odd))
    
    # print(list_)
    # 求和
    sum = 0 
    
    for n in list_:
        sum += n
        
    return sum


print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

## request模块抓取URL：get请求到指定页面，返回http响应
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s:%s' % (k, v))
    print('Data:', data.decode('utf-8'))
    
## 返回很丰富

'''
Status: 200 OK
Date:Mon, 27 Aug 2018 01:22:01 GMT
Content-Type:application/json; charset=utf-8
Content-Length:2138
Connection:close
Vary:Accept-Encoding
X-Ratelimit-Remaining2:99
X-Ratelimit-Limit2:100
Expires:Sun, 1 Jan 2006 01:00:00 GMT
Pragma:no-cache
Cache-Control:must-revalidate, no-cache, private
Set-Cookie:bid=WftOALOQgTo; Expires=Tue, 27-Aug-19 01:22:01 GMT; Domain=.douban.com; Path=/
X-DOUBAN-NEWBID:WftOALOQgTo
X-DAE-Node:beleg2
X-DAE-App:book
Server:dae
X-Frame-Options:SAMEORIGIN
Data: {
    "rating":{"max":10,"numRaters":16,"average":"7.4","min":0},
    "subtitle":"",
    "author":["廖雪峰"],
    "pubdate":"2007",
    "tags":[
            {"count":21,"name":"spring","title":"spring"},
            {"count":13,"name":"Java","title":"Java"},
            {"count":6,"name":"javaee","title":"javaee"},
            {"count":5,"name":"j2ee","title":"j2ee"},
            {"count":4,"name":"计算机","title":"计算机"},
            {"count":4,"name":"编程","title":"编程"},
            {"count":3,"name":"藏书","title":"藏书"},
            {"count":3,"name":"POJO","title":"POJO"}
            ],
    "origin_title":"",
    "image":"https://img3.doubanio.com\/view\/subject\/m\/public\/s2552283.jpg",
    "binding":"平装",
    "translator":[],
    "catalog":"",
    "pages":"509",
    "images":{
            "small":"https://img3.doubanio.com\/view\/subject\/s\/public\/s2552283.jpg",
            "large":"https://img3.doubanio.com\/view\/subject\/l\/public\/s2552283.jpg",
            "medium":"https://img3.doubanio.com\/view\/subject\/m\/public\/s2552283.jpg"},
            "alt":"https:\/\/book.douban.com\/subject\/2129650\/",
            "id":"2129650",
            "publisher":"电子工业出版社",
            "isbn10":"7121042622",
            "isbn13":"9787121042621",
            "title":"Spring 2.0核心技术与最佳实践",
            "url":"https:\/\/api.douban.com\/v2\/book\/2129650",
            "alt_title":"",
            "author_intro":"",
            "summary":"本书注重实践而又深入理论，由浅入深且详细介绍了Spring 2.0框架的几乎全部的内容，并重点突出2.0版本的新特性。
                        本书将为读者展示如何应用Spring 2.0框架创建灵活高效的JavaEE应用，并提供了 一个真正可直接部署的完整的Web应用程序——Live在线书店(http:\/\/www.livebookstore.net)。
                        \n在介绍Spring框架的同时，本书还 介绍了与Spring相关的大量第三方框架，涉及领域全面，实用性强。本书另一大特色是实用性强，易于上手，以实际项目为出发点，介绍项目开发中应遵循的最佳开发模式。
                        \n本书还介绍了大量实践性极强的例子，并给出了完整的配置步骤，几乎覆盖了Spring 2.0版本的新特性。
                        \n本书适合有一定Java基础的读者，对JavaEE开发人员特别有帮助。本书既可以作为Spring 2.0的学习指南，也可以作为实际项目开发的参考手册。",
            "price":"59.8"}
'''


# 模拟浏览器发送get请求，使用Request对象添加HTTP头
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0(iPhone;CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    print('State:', f.status, f.reason)
    for k,v in f.getheaders():
        print('%s:%s'% (k, v))
    print('Data:', f.read().decode('utf-8'))


## Post发送请求：将参数data以bytes形式传入
# 模拟微博登陆

print('Login to weibo.cn')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('cliend_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcom?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])
   
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0(iPhone;CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
    
    
## 复杂控制：使用Proxy访问网站，利用ProxyHandler处理

proxy_handler = urllib.request.ProxyHandler({'http':'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')

opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass

    
## 利用urllib读取JSON，然后将JSON解析为Python对象：
# json为一个utf-8编码的str。所以先将data(bytes)解码
def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read()
        return(json.loads(data.decode('utf-8')))
        
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)

print(data)

print('\n\n\n')

assert data['query']['results']['channel']['location']['city'] == 'Beijing'

print('ok')



'''
{
"query":{
        "count":1,
        "created":"2018-08-27T02:49:14Z",
        "lang":"en-US",
        "results":{"channel":{
                                "units":{"distance":"mi","pressure":"in","speed":"mph","temperature":"F"},
                                "title":"Yahoo! Weather - Beijing, Beijing, CN",
                                "link":"http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/",
                                "description":"Yahoo! Weather for Beijing, Beijing, CN",
                                "language":"en-us",
                                "lastBuildDate":"Mon, 27 Aug 2018 10:49 AM CST",
                                "ttl":"60",
                                "location":{"city":"Beijing","country":"China","region":" Beijing"},
                                "wind":{"chill":"84","direction":"135","speed":"4"},
                                "atmosphere":{"humidity":"58","pressure":"1007.0","rising":"0","visibility":"16.1"},
                                "astronomy":{"sunrise":"5:38 am","sunset":"6:53 pm"},
                                "image":{
                                        "title":"Yahoo! Weather","width":"142",
                                        "height":"18","link":"http://weather.yahoo.com",
                                        "url":"http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif"},
                                "item":{
                                        "title":"Conditions for Beijing, Beijing, CN at 10:00 AM CST",
                                        "lat":"39.90601",
                                        "long":"116.387909",
                                        "link":"http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/",
                                        "pubDate":"Mon, 27 Aug 2018 10:00 AM CST",
                                        "condition":{"code":"30","date":"Mon, 27 Aug 2018 10:00 AM CST","temp":"84","text":"Partly Cloudy"},
                                        "forecast":[{"code":"39","date":"27 Aug 2018","day":"Mon","high":"91","low":"76","text":"Scattered Showers"},
                                                    {"code":"30","date":"28 Aug 2018","day":"Tue","high":"89","low":"71","text":"Partly Cloudy"},
                                                    {"code":"34","date":"29 Aug 2018","day":"Wed","high":"90","low":"72","text":"Mostly Sunny"},
                                                    {"code":"30","date":"30 Aug 2018","day":"Thu","high":"84","low":"70","text":"Partly Cloudy"},
                                                    {"code":"28","date":"31 Aug 2018","day":"Fri","high":"81","low":"71","text":"Mostly Cloudy"},
                                                    {"code":"28","date":"01 Sep 2018","day":"Sat","high":"82","low":"69","text":"Mostly Cloudy"},
                                                    {"code":"11","date":"02 Sep 2018","day":"Sun","high":"82","low":"69","text":"Showers"},
                                                    {"code":"34","date":"03 Sep 2018","day":"Mon","high":"87","low":"70","text":"Mostly Sunny"},
                                                    {"code":"30","date":"04 Sep 2018","day":"Tue","high":"87","low":"70","text":"Partly Cloudy"},
                                                    {"code":"30","date":"05 Sep 2018","day":"Wed","high":"86","low":"67","text":"Partly Cloudy"}],
                                        "description":"<![CDATA[<img src=\"http://l.yimg.com/a/i/us/we/52/30.gif\"/>\n<BR />\n<b>Current Conditions:</b>\n<BR />Partly Cloudy\n<BR />\n<BR />\n<b>Forecast:</b>\n<BR /> Mon - Scattered Showers. High: 91Low: 76\n<BR /> Tue - Partly Cloudy. High: 89Low: 71\n<BR /> Wed - Mostly Sunny. High: 90Low: 72\n<BR /> Thu - Partly Cloudy. High: 84Low: 70\n<BR /> Fri - Mostly Cloudy. High: 81Low: 71\n<BR />\n<BR />\n<a href=\"http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/\">Full Forecast at Yahoo! Weather</a>\n<BR />\n<BR />\n<BR />\n]]>",
                                        "guid":{"isPermaLink":"false"}}}}}}



{'query':{
        'count': 1, 
        'created': '2018-08-27T02:49:14Z', 
        'lang': 'en-US', 
        'results': {    }
        }
}

'''



class DefaultSaxHandler(object):

    # 节点名称、节点属性
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs:%s' % (name, str(attrs)))
    
    # 节点名称
    def end_element(self, name):
        print('sax:end_element: %s' % name)

    # 节点数据
    def char_data(self, text):
        print('sax:chardata: %s' % text)
        
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()   #创建对象实例
parser = ParserCreate()   #创建一个expat解析器
# 为解析器设置回调函数
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
# 开始解析xml
parser.Parse(xml)


'''
sax:start_element: ol, attrs:{}
sax:chardata:

sax:chardata:
sax:start_element: li, attrs:{}
sax:start_element: a, attrs:{'href': '/python'}
sax:chardata: Python
sax:end_element: a
sax:end_element: li
sax:chardata:

sax:chardata:
sax:start_element: li, attrs:{}
sax:start_element: a, attrs:{'href': '/ruby'}
sax:chardata: Ruby
sax:end_element: a
sax:end_element: li
sax:chardata:

sax:end_element: ol
'''





## xml解析雅虎天气预报信息

# 解析XML时，注意找出自己感兴趣的节点，
# 响应事件时，把节点数据保存起来。
# 解析完毕后，就可以处理数据。
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

# 读取url对应网页数据
with request.urlopen(URL, timeout=4) as f:
    data = f.read()     #bytes型记得decode

# print(data)

#定义全局变量
weather_dict = {}
which_day = 0


#定义解析类
class WeatherSaxHandler(object):

    def start_element(self, name, attrs):   # attrs为属性，本质为字典
        print(name, str(attrs))
        global weather_dict, which_day
        # 判断并获取XML文档中地理位置信息
        # sax:start_element: yweather:location, attrs: {'xmlns:yweather': 'http://xml.weather.yahoo.com/ns/rss/1.0', 'city': 'Beijing', 'country': 'China', 'region': ' Beijing'}
        # sax:end_element: yweather:location
        if name == 'yweather:location':
            weather_dict['city'] = attrs['city']
            weather_dict['country'] = attrs['country']
        # 获取天气预测信息
        if name == 'yweather:forecast':
            weather = {
                        'text': attrs['text'],
                        'date' : attrs['date'],
                        'day': attrs['day'],
                        'low': attrs['low'],
                        'high': attrs['high']}
            weather_dict[which_day] = weather
            which_day += 1


            
    def end_element(self, name):
        pass

    def data_element(self, text):
        pass

        

handler = WeatherSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.data_element


parser.Parse(data.decode('utf-8'))


print(which_day)

print(weather_dict)

assert weather_dict['city'] == 'Beijing'
print(weather_dict[2])



## HTML解析网页中的文本、图像 等……
'''
嵌套关系：<head><title></title></head> 父子

并列关系：<head></head><body></body> 兄弟姐妹

双标记 <标记名></标记名> :<front ></front >、<p > </p> 等

单标记 <标记名/> ：注释、 <br/> 、<!Doctype html>、<hr/>
'''

class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)    
        
    def handle_data(self, data):
        print(data)
        
    def handle_comment(self, data):
        print('<!--', data, '-->')
    
    # 特殊字符 英文表示的&nbsp;
    def handle_entityref(self, name):
        print('&%s;' % name)
        
    #特殊字符 数字表示的&#1234;
    def handle_charref(self, name):
        print('&#%s;' % name)
        

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')


'''
<html>


<head>
</head>


<body>


<!--  test html parser  -->


<p>
Some
<a>
html
</a>
 HTML tutorial...
<br>
END
</p>


</body>
</html>
'''





'''
找一个网页，例如https://www.python.org/events/python-events/，
用浏览器查看源码并复制，
然后尝试解析一下HTML，
输出Python官网发布的会议时间、名称和地点。
'''

html_txt = ''

try:
    page = urllib.request.urlopen('https://www.python.org/events/python-events/')
    html_txt = page.read()      #读取网页内容
finally:
    page.close()
    
'''
<li>
<h3 class="event-title"><a href="/events/python-events/733/">PyCon Nigeria</a></h3>
<p>
<time datetime="2018-09-13T00:00:00+00:00">13 Sept. &ndash; 16 Sept. <span class="say-no-more"> 2018</span></time>
<span class="event-location">Lagos, Nigeria</span>
</p>
</li>
'''
    
class MyHTMLParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self._title = [False]
        self._time = [False]
        self._place = [False]
        self.time = ''      #用于拼接时间
    
    # attrs存储形式：[('class', 'event-title')]
    def _attr(self, attrlist, attrname):
        for attr in attrlist:
            if attr[0] == attrname:
                return attr[1]
        return None
        
    def handle_starttag(self, tag, attrs):
        # print('<%s>' % tag)
        if tag == 'h3' and self._attr(attrs, 'class') == 'event-title':
            self._title[0] = True
        if tag == 'time':
            self._time[0] = True
        if tag == 'span' and self._attr(attrs, 'class') == 'event-location':
            self._place[0] = True

    def handle_endtag(self, tag):
        #print('</%s>' % tag)
        if tag == 'time':
            self._time.append(self.time)
            self.time = ''
            self._time[0] = False
            
    def handle_startendtag(self, tag, attrs):
        #print('<%s/>' % tag)    
        pass
        
    def handle_data(self, data):
        #print(data)
        if self._title[0] == True:
            #print('title:%s' % data)
            self._title.append(data)
            self._title[0] = False
        if self._time[0] == True:
            #print('time:%s' % data)
            self.time += data       #拼接time
        if self._place[0] == True:
            #print('place:%s' % data)
            self._place.append(data)
            self._place[0] = False
            
        
    def handle_comment(self, data):
        # print('<!--', data, '-->')
        pass
        
    # 特殊字符 英文表示的&nbsp;
    def handle_entityref(self, name):
        #print('&%s;' % name)
        if self._time[0] == True:
            self.time += '-'    # &ndash -> '-'
        
    #特殊字符 数字表示的&#1234;
    def handle_charref(self, name):
        #print('&#%s;' % name)
        pass
        
    def show_content(self):
        for n in range(1, len(self._title)):
            print('Title: %s' % self._title[n])
            print('Time: %s' % self._time[n])
            print('Place: %s' % self._place[n])
            print('--------------------------')
            
            
parser = MyHTMLParser()
parser.feed(html_txt.decode('utf-8'))

parser.show_content()

print(parser._title)
print(parser._time)
print(parser._place)



# 安装Pillow
# 如果安装了Anaconda，Pillow就已经可用了。否则，需要在命令行下通过pip安装：
# $ pip install pillow
# 如果遇到Permission denied安装失败，请加上sudo重试。


## 图片大小缩放

# 打开一个jpg图像文件
im = Image.open('test.jpg')
# 获取图像尺寸
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%
im.thumbnail((w//2, h//2))      #取整除法
print('Resize image to: %sx%s' %(w//2, h//2))
# 把缩放后的图像用jpeg格式保存
im.save('thumbnail.jpg', 'jpeg')


## 图片模糊效果

im = Image.open('test.jpg')
# 应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')



## 绘图方法。生成字母验证码图片。

# 随机字母 返回数值表达式sting型
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240 * 60 初始化画布
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Draw对象 画布内
draw = ImageDraw.Draw(image)

# 填充每个像素 画布
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill = rndColor())

# 创建Font对象
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)

# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font = font, fill = rndColor2())

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')



im = Image.open('test.jpg')
# 三个属性
print(im.format)    # JPEG。识别图像源格式--None
print(im.size)      #(440, 617)。宽度，高度，tuple
print(im.width)
print(im.height)
print(im.mode)      # RGB。此外还有L，CMTK

im.show()       # 输出原图 均显示bmp格式

# 图像格式转化    endswith(<str>)
def img2png(imgFile):
    if imgFile.endswith(('.bmp', '.gif', '.jpg')):
        with Image.open(imgFile) as im:
            im.save(imgFile[:-3] + 'png')

img2png('test.jpg')

im2 = Image.open('test.png')
im2.show()

# 图像缩放，参数表示新的宽度高度
im = im.resize((100, 100))


blank = Image.new('RGB', (512, 512), 'white')

draw = ImageDraw.Draw(blank)

draw.line([0,0,120,120], fill = 'red')    
# (x1,y1,x2,y2) [x1,y1,x2,y2][(xx,y1),(x2,y2)]

draw.point([55,60], fill = 'black')
draw.point([65,60], fill = 'black')
draw.point([70,60], fill = 'black')
draw.point([75,60], fill = 'black')
draw.point([80,60], fill = 'black')

draw.line([120,120,250,120], fill = 'red')    
draw.line([120,120,120,250], fill = 'red')    
draw.line([250,120,250,250], fill = 'red')    
draw.line([120,250,250,250], fill = 'red')    

# 方形内，相切画弧形。顺时针变大，与坐标轴相反
draw.arc([120,120,250,250], 180, 360, fill = 'yellow')
# startAngle, endAngle

# 改变方形
draw.arc([120,120,250,400], 90, 270, fill = 'blue')

# 画圆形
draw.ellipse([120,120,250,250], outline = 'black', fill = 'red')

# 画圆形
draw.ellipse([120,120,250,400], outline = 'black', )

# chord 弦  pieslice 扇形 
# polygon 多边形，连接顶点很棒棒 rectangle 矩形

# 图像内插入文字
draw.text(position, string, options)
# position 指定字符串左上角坐标
# options为fill或font

blank.save('blank.jpg', 'jpeg')

blank.show()


r = requests.get('https://www.douban.com/')
# <Response[200]>
r.status_code
# 200 
r.text
# '<!DOCTYPE HTML>\n<html>\n<head>\n<meta name="description" content="提供图书、电影、音乐唱片的推荐、评论和...'

## 区别以下 urllib.requests 模块


'''
## request模块抓取URL：get请求到指定页面，返回http响应
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
'''

'''
# 模拟浏览器发送get请求，使用Request对象添加HTTP头
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0(iPhone;CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
'''


# 对于带参数的URL，传入一个dict作为params参数
# 'https://www.douban.com/search?q=python&cat=1001'
r = requests.get('http://www.douban.com/search', params = {'q': 'python', 'cat': '1001'})
r.url      # 真实url
r.encoding      #自动检测编码
# 'utf-8'
r.content   # 无论响应是文本还是二进制，都可以用content属性获取bytes对象
# b'<!DOCTYPE html>\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n...'



# 对于特定类型的响应，例如json，可以直接获取
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
r.json()
# {'query': {'count': 1, 'created': '2017-11-17T07:14:12Z', ...



# 传入HTTP Header：传入一个dict
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
r.text
# '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n <title>豆瓣(手机版)</title>...'

## Post请求：传入data参数作为请求数据
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})


# requests 传递Json数据，直接传入json参数

params = {'key': 'value'}
r = request.post(url, json = params)    # 内部自动序列化为Json

# 上传文件,files参数.读取文件，需要使用‘rb’二进制方法读取
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files = upload_files)


r.headers
# {Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Content-Encoding': 'gzip', ...}

r.headers['Content-Type']
# 'text/html; charset=utf-8'


# 特殊处理的cookies，不必解析
r.cookies['ts']
# 'example_cookie_12345'

# 请求中传入Cookies，只需传入一个dict
cs = {'token': '12345', 'status': 'working'}
r = requests.get(url, cookies=cs)

# 以秒为单位指定超时
r = requests.get(url, timeout = 2.5)


chardet.detect(b'Hello, world!')
# {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
# confidence 表示监测的概率是1.0（即 100%）


data = '离离原上草，一岁一枯荣'.encode('gbk')
chardet.detect(data)
# {'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}

data = '离离原上草，一岁一枯荣'.encode('utf-8')
chardet.detect(data)
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

data = '最新の主要ニュース'.encode('euc-jp')
chardet.detect(data)
# {'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}





## 获取CPU信息
# CPU逻辑数量
psutil.cpu_count()
4
# CPU物理核心
psutil.cpu_count(logical = False)
2       # 双核超线程， 4则是4核非超线程


# 统计CPU的用户、系统、空闲时间
psutil.cpu_times()
scputimes(user=8915.4375, system=7503.78125, idle=195506.48437499997, interrupt=173.640625, dpc=148.6875)


for x in range(10):
    psutil.cpu_percent(interval = 1, percpu = True)

'''
[9.2, 4.7, 6.2, 3.1]
[4.7, 3.1, 6.2, 9.4]
[24.6, 29.7, 35.9, 25.0]
[3.1, 0.0, 1.6, 12.5]
[4.7, 6.2, 1.6, 7.8]
[1.6, 0.0, 4.7, 7.8]
[6.2, 3.1, 3.1, 7.8]
[24.6, 31.2, 21.9, 21.9]
[16.7, 4.7, 14.1, 12.5]
[10.8, 1.6, 3.1, 3.1]
'''


## 获取内存信息
# 获取物理内存
psutil.virtual_memory()
# svmem(total=8589934592, available=2866520064, percent=66.6, used=7201386496, free=216178688, active=3342192640, inactive=2650341376, wired=1208852480)
# （字节）总内存 8GB，已使用6.7GB，使用率66.6%

# 交换区内存信息
psutil.swap_memory()
#sswap(total=1073741824, used=150732800, free=923009024, percent=14.0, sin=10705981440, sout=40353792)


## 获取磁盘信息
psutil.disk_partitions() # 磁盘分区信息
[sdiskpart(device='/dev/disk1', mountpoint='/', fstype='hfs', opts='rw,local,rootfs,dovolfs,journaled,multilabel')]
# HFS 文件格式  rw 可读写 journaled 支持日志

psutil.disk_usage('/') # 磁盘使用情况
sdiskusage(total=998982549504, used=390880133120, free=607840272384, percent=39.1)

psutil.disk_io_counters() # 磁盘IO
sdiskio(read_count=988513, write_count=274457, read_bytes=14856830464, write_bytes=17509420032, read_time=2228966, write_time=1618405)


## 获取网络接口和网络连接信息
psutil.net_io_counters() # 获取网络读写字节／包的个数
#snetio(bytes_sent=3885744870, bytes_recv=10357676702, packets_sent=10613069, packets_recv=10423357, errin=0, errout=0, dropin=0, dropout=0)

psutil.net_if_addrs() # 获取网络接口信息
{
  'lo0': [snic(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0'), ...],
  'en1': [snic(family=<AddressFamily.AF_INET: 2>, address='10.0.1.80', netmask='255.255.255.0'), ...],
  'en0': [...],
  'en2': [...],
  'bridge0': [...]
}

psutil.net_if_stats() # 获取网络接口状态
{
  'lo0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=16384),
  'en0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=1500),
  'en1': snicstats(...),
  'en2': snicstats(...),
  'bridge0': snicstats(...)
}


$ sudo python3      # 获取系统权限

psutil.net_connections()    # 获取当前网络连接信息
[
    sconn(fd=83, family=<AddressFamily.AF_INET6: 30>, type=1, laddr=addr(ip='::127.0.0.1', port=62911), raddr=addr(ip='::127.0.0.1', port=3306), status='ESTABLISHED', pid=3725),
    sconn(fd=84, family=<AddressFamily.AF_INET6: 30>, type=1, laddr=addr(ip='::127.0.0.1', port=62905), raddr=addr(ip='::127.0.0.1', port=3306), status='ESTABLISHED', pid=3725),
    sconn(fd=93, family=<AddressFamily.AF_INET6: 30>, type=1, laddr=addr(ip='::', port=8080), raddr=(), status='LISTEN', pid=3725),
    sconn(fd=103, family=<AddressFamily.AF_INET6: 30>, type=1, laddr=addr(ip='::127.0.0.1', port=62918), raddr=addr(ip='::127.0.0.1', port=3306), status='ESTABLISHED', pid=3725),
    sconn(fd=105, family=<AddressFamily.AF_INET6: 30>, type=1, ..., pid=3725),
    sconn(fd=106, family=<AddressFamily.AF_INET6: 30>, type=1, ..., pid=3725),
    sconn(fd=107, family=<AddressFamily.AF_INET6: 30>, type=1, ..., pid=3725),
    ...
    sconn(fd=27, family=<AddressFamily.AF_INET: 2>, type=2, ..., pid=1)
]


list_pid = psutil.pids()    #获取所有进程id

## 寻找python所在进程
for i in list_pid:
    m = psutil.Process(i)
        if re.search('ython', m.name()) is not None:
            print(i)

# 9736

 print(psutil.Process(9736).name())
# python.exe
p = psutil.Process(9736)

p.name()    #进程名称
# 'python.exe'

p.exe()     #进程exe路程
# 'C:\\Users\\洛七\\AppData\\Local\\Programs\\Python\\Python36\\python.exe'

p.cwd() #进程工作目录
# 'E:\\cookies\\ieleven'

p.cmdline()     #进程启动的命令行
# ['python']

p.ppid()    #父进程id
# 9696

p.parent()      #父进程
# psutil.Process(pid=9696, name='cmd.exe', started='10:47:24')

p.children()    #子进程
# []

p.status()      #进程状态
# 'running'

p.username()    #进程用户名
# 'DESKTOP-BC4KCNS\\Shining.Chan'

p.create_time()     #进程创建时间
# 1537238913.0

datetime.fromtimestamp(p.create_time())
# datetime.datetime(2018, 9, 18, 10, 48, 33)

p.terminal()    #进程终端

p.cpu_times()   #进程使用cpu时间
# pcputimes(user=0.34375, system=4.796875, children_user=0.0, children_system=0.0)

p.memory_info()     #进程使用的内存
# pmem(rss=10350592, vms=8355840, num_page_faults=213182, peak_wset=14778368, wset=10350592, peak_paged_pool=179240, paged_pool=178840, peak_nonpaged_pool=14168, nonpaged_pool=13440, pagefile=8355840, peak_pagefile=8941568, private=8355840)

p.open_files()      #进程打开的文章
# [popenfile(path='C:\\Windows\\System32\\zh-CN\\KernelBase.dll.mui', fd=-1), popenfile(path='C:\\Windows\\System32\\zh-CN\\kernel32.dll.mui', fd=-1)]

p.connections()     #进程相关网络连接
# []

p.num_threads()     #进程的线程数量
# 5

p.threads()     #所有线程信息
# [pthread(id=13180, user_time=0.359375, system_time=4.890625), pthread(id=12988, user_time=0.0, system_time=0.0), pthread(id=3688, user_time=0.0, system_time=0.0), pthread(id=14664, user_time=0.0, system_time=0.0), pthread(id=14848, user_time=0.0, system_time=0.0)]

p.environ()     #进程环境变量
# {'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\洛七\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-BC4KCNS', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\洛七', 'LOCALAPPDATA': 'C:\\Users\\洛七\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-BC4KCNS', 'NUMBER_OF_PROCESSORS': '4', 'ONEDRIVE': 'C:\\Users\\洛七\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;E:\\Program Files (x86)\\nodejs\\;E:\\Program Files (x86)\\Git\\cmd;E:\\Program Files (x86)\\Git\\bin;E:\\Program Files (x86)\\Git\\mingw32\\libexec\\git-core;C:\\Users\\洛七\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\;C:\\Users\\洛七\\AppData\\Local\\Programs\\Python\\Python36\\;C:\\Users\\洛七\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\洛七\\AppData\\Roaming\\npm', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 58 Stepping 9, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '3a09', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PROMPT': '$P$G', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\洛七\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\洛七\\AppData\\Local\\Temp', 'USERDOMAIN': 'DESKTOP-BC4KCNS', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-BC4KCNS', 'USERNAME': 'Shining.Chan', 'USERPROFILE': 'C:\\Users\\洛七', 'WINDIR': 'C:\\WINDOWS'}

p.terminate()       #结束进程


psutil.test()       # 类似unix中ps命令效果
'''
USER         PID %MEM     VSZ     RSS TTY           START    TIME  COMMAND
root           0 24.0 74270628 2016380 ?             Nov18   40:51  kernel_task
root           1  0.1 2494140    9484 ?             Nov18   01:39  launchd
root          44  0.4 2519872   36404 ?             Nov18   02:02  UserEventAgent
root          45    ? 2474032    1516 ?             Nov18   00:14  syslogd
root          47  0.1 2504768    8912 ?             Nov18   00:03  kextd
root          48  0.1 2505544    4720 ?             Nov18   00:19  fseventsd
_appleeven    52  0.1 2499748    5024 ?             Nov18   00:00  appleeventsd
root          53  0.1 2500592    6132 ?             Nov18   00:02  configd
'''


$ pip3 install virtualenv     #提供隔离的python运行环境，解决不同应用多版本冲突问题