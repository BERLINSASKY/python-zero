import unittest
import logging
import timeit
import a
from abc import ABCMeta, abstractmethod
import sqlite3
from PIL import Image
import datetime
from random import randint
import re
import pylint
from time import time
import pyfiglet
import termcolor
import modules as e
import random
import os
from functools import reduce
print(type((1, 2, 3)))

# بقدر بعرف الكلمات المحجوزة عن طريق
help('keywords')

a, b, c = 1, 2, 3
print(a, b, c)

# اذا بدي اكتب ال \ بيطلعلي ايرور
print('hello\\')

print(""" ilove 
my car "hello"
warld
    
""")

# concetination
msg = "i love "
l = "python"
print(msg + l)


print(len("ilove python"))
o = 'love pyhon but easy'
print(o.title())

c, d, e = "1", "10", "100"
print(c.zfill(3))


d = 'hello i am abdullah'
print(d.split(" ", 2))
print(d.split())
o = 'osama'
print(o.center(9, '#'))


i = 'i love my syria , syria is beauty ,fk u syria'
print(i.count('syria'))


p = 'hello ahmad'
print(p.find('k'))  # بتطالع -1
# print(p.index('k')) بتطالع ايرور

k = 'abdullahsermani2003'
print(k.ljust(30, "@"))

e = """i
am
abdullah
"""
print(e.splitlines())

a = 'ahmad sermani'
print(a.replace('ahmad', 'abdullah'))

lis = ['ahmad', 'sermani']
print(' '.join(lis))


name = 'abdullah'
age = 23
print('my name is %s my age is %d' % (name, age))


name = 'abdullah '
rank = 2
print('hello my name is {}'.format(name))
print('hello my name is {:s} and my rank is {:.3f}'.format(name, rank))

# {:.5s} بتشتغل شغل ال slice
text = 'hello i am abdullah welcome'
print('{:.5s} kefaaaaaaaaaaaaaak'.format(text))

a, b, c = "one", 'two', "three"
print('hello {2} {1} {0}'.format(a, b, c))


name = 'abdullah'
age = 30
rank = 40
print(f'hello i am {name} and my age is {age} and our rank is {rank}')


a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)


a = [1, 2, True, 'sasky', 'ahmad', False]
print(a[1:5])
# steps
print(a[1:5:2])
a[0:2] = [3, 4]
print(a)


b = ['ahmad', 'abdullah', 'sana', 'fateh', 'mahmoud']
b.append('ibrahim')
b.insert(2, 'haytham')
print(b)


a = ('osama')
print(type(a))

a = ('osama',)
print(type(a))


a = 'osama'
b = ('ahmad', 1, 2)
c = ['abdullah', 5, 6]
print(a*6)
print(b*6)
print(c*6)


a = (1, 2, 3, 1, 1, 1, 1)
print(a.count(1))
print(f'the position of 7 is {a.index(3)}')

a = ('a', 'b', 5, 'c')
c, b, _, d = a
print(c)
print(b)
print(d)


a = {'ahmad', 'osama', 'sana', 'ahmad'}
print(a)


a = {1, 2}
b = {3, 4}
c = ['a', 'b']
print(a | b)
print(a.union(b))
print(a.union(c))
a.add(5)
print(a)
a.discard(5)
print(a)
a.remove(1)
print(a)

a = {1, 2, 3}
b = {'a', 'b'}
a.update(b)
print(a)

a = {1, 2, 3, 4}
b = {1, 2, 3}
print(a)
print(a.difference(b))
a.difference_update(b)
print(a)

a = {1, 2, 3}
b = {1, 4, 'a'}
print(a)
print(a.intersection(b))  # التشابه
print(a)

print('=' * 10)

a = {1, 2, 3, 4}
b = {1, 2, 3, 'b'}
print(a)
print(a.difference(b))  # فرق اي عن بي
print(a.symmetric_difference(b))  # الفرق بين التنين
a.difference_update(b)
print(a)


a = {1, 2, 3, 4}
b = {1, 2, 3}
print(a.issuperset(b))  # هل اي تحوي جميع عناصر بي
print(a.issubset(b))  # هل بي تحوي جميع عناصر ال اي

print('='*100)
a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {7, 8, 9}
print(a.isdisjoint(b))  # هل اي مختلفة تماما عن بي
print(a.isdisjoint(c))  # هل اي مختلفة تماما عن سي


user = {
    'name': 'abdullah',
    'age': 14,
    'country': 'aleppo',
    'dec': {'a': 1, 'b': 2}
}
print(user['name'])
print(user.get('age'))
print(user.keys())
print(user.values())
print(user['dec']['a'])

user = {

    'name': 'ahmad'
}
# user.clear()
print(user)

user['age'] = 23
print(user)

user.update({
    'country': 'aleppo'
})
print(user)
user.setdefault('ages', 5)
print(user)

user.update({'from': 'ariha'})
print(user)

print(user.popitem())
print(user)


a = {
    'name': 'ahmad',
    'car': 'rio'
}
items = a.items()  # اذا صار اي تغيير بتحفظو
old = a.copy()  # اذا صار اي تغيير ما بتحفظو
print(items)
print(old)
a.update({'age': 40})
print(items)
print(old)


a = ('a', 'b', 'c')
b = 'X'
print(dict.fromkeys(a, b))


print(bool([1, 2, 3]))
print(bool([]))
print('='*100)

x = 5
a = 'd'
y = 3
if x < 10 and a == "d" or y == 3:
    print(True)

print(not x < 10)


x = input('what\'s your name').strip().capitalize()
y = input('what is your last name').strip().capitalize()
print(f'hello {x:.1s} {y:.2s} how r u ')


email = 'abdullahsermani@gmail.com'
email.index('@')
print(email[0:email.index('@')])

a = 5
if a == 5:
    print(f'the value of a is {a:d}')
print(f'the value of a is {a}' if a == 5 else 'dont print any thing')


lista = ['ahmad', 'abdullah', 'sana', 'fateh', 'mahmoud', 'ibrahim']
name = ' abdullah'.strip()
if name in lista:
    print('this is the member of family')


x = 0
while x < 5:
    print('hello')
    x += 1
else:
    print('end of loop')


x = {'a': 'ahmad',
     'b': 'abdullah'}

for z in x:
    print(f'the value {z} contains {x[z]}')

for k, l in x.items():
    print(f'the value {k} contains {l}')


x = {
    '3': {
        '4': 'c'

    }

}
for k, l in x.items():
    print(f'the key is {k} and the value is {l}')
    for r, t in l.items():
        print(f'the key is {r} and the value is {t}')


def function():
    return 'hello abdullah'


print(function())

t = [1, 2, 3, 4]
print(t)
# اذا بدي اعرض بدون ما يحطلي العناصر ضمن ليست
print(*t)


# اذا بدي دخل عدد كبير من البراميترز
def hello(*lista):
    print(type(lista))
    for name in lista:
        print(f'hello {name}')


hello('abdullah', 'ahmad', 'fateh')


def hello(**lista):
    print(type(lista))
    for key, value in lista.items():
        print(f'the key is {key} and the value is {value}')


hello(ahmad='sermani', age=25)

dec = {'abdullah': 'sermani',
       'age': 22
       }
hello(**dec)


def x():
    global x
    x = 5


x()
print(x)

# lampda fun


def hello(name, age): return f'hello {name} age is {age}'


print(hello('ahmad', 20))

print(r'hello\n fuck u')  # بتوقف الاوامر الي جوا

print('*'*100)
print('*'*100)
# اذا بدي حط ملف لافتحو غالبا بيطلعلي ايرور لان بكون الموقع الافتراضي غلط
#  os.getcwd()عن طريق ال
# بقدر جيب الموقع الي لازم حط فيو الملف
print(os.getcwd())  # main corrent working directory
print(os.path.abspath(__file__))  # the location of this file
# working directory for the open file
print(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # change the main dir
print(os.getcwd())
print('*'*100)
file = open('abd.txt', 'r')
# print(file.read())
for line in file:
    if line.startswith('fuck'):
        break
    print(line)
file.close()

FILE = open(r'C:\Users\ASUS\Desktop\backend\python zero\abd.txt', 'r')
print(FILE.read())
FILE.close()


file = open('abd.txt', 'w')
file.write('hello python\n'*20)  # بشيل محتوى الملف وبيكتب شي جديد

mylist = ['ahmad\n', 'abdullah\n']
file.writelines(mylist)
file.writelines('abdullah hellooo')
file.close()

file1 = open('abd.txt', 'a')  # بتضيف للمحتوى الموجود
file1.write('\nhello again')
file1.close()


file2 = open('abd.txt', 'a')

file2.truncate(5)  # بتقص من المحتوى الموجود
file2.close()


file3 = open('abd.txt', 'a')
print(file3.tell())  # tell me where is the cruser
file3.close()

file4 = open('abd.txt', 'a')
file4.write('\nhello python\n'*20)
file4.close()

file5 = open('abd.txt', 'r')
file5.seek(30)
file5.read()
file5.close()

print('*'*100)


x = [1, 2, 3, []]
if all(x):
    print('all true')
else:
    print('there is one false')

if any(x):
    print('one at least true')
else:
    print('all false')


print(bin(2))  # بترجعلي الرقم bin


x = 1
print(id(x))  # address

# sum([],start)
# ليست بالعناصر الي بدي اجمعا اما محل الصفر بحط الرقم الي بدي ضيف عليه هي الليست
x = sum([1, 2, 3, 4], 0)
print(x)


# range(start,end,step)
print(list(range(2, 5, 1)))


print('hello', 'abdullah', sep='|')

a = 'abdullah'
print(a[slice(0, 3)])


# وظيفة ال map
# بكون عندي فانكشن الها برامترايز وبكون عندي ليست وبدي دخل هالليست كبرامترايز للفنكشن
# map(function with paramitares , list)
# map called map because it map the function for every element in list
x = ['ahmad', 'abdullah', 'sana']

for name in list(map((lambda text: f'hello {text}'), x)):
    print(name)


names = ['ahmad', 'abdullah', 'ibrahim']

for x in list(filter(lambda name: name.startswith('i'), names)):
    print(x)


# reduce
# تعمل هذه الفانكشن على تقليل عدد العناصر للوصول لعنصر واحد بالاخير

def sum(num1, num2):
    return num1 + num2


num = [1, 2, 3, 4, 5]
res = reduce(sum, num)
print(res)
# العملية الي صارت
# ((((1+2)+3)+4)+5)


# enumerate()
# بتضفلي كاونتر يعني عداد
myskills = {'html', 'css', 'python', 'django', 'git&github'}
myskillswithcounter = enumerate(myskills)

# for skill in myskillswithcounter :
#    print(skill)

for counter, skill in myskillswithcounter:
    print(f'{counter} - {skill}')


print('*'*100)

a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

a = 'ahmad'
for x in reversed(a):
    print(x)


print(random)
# بتولدلي راندوم نامبر
print(random.random())
# dir
# بتطالعلي كل الفانكشن الموجودة ضمن الموديول
print(dir(random))

print(f'print random int {randint(100,222)}')

# اذا بدي اضيف مسار لمسارات البايسون
# import sys
# sys.path.append(r'C:\Users\ASUS\Desktop\backend\python')
# print(sys.path)


# عطيتها للموديول اسم e
# alias اسم مستعار
# e.hello()


print(dir(pyfiglet))

print('*'*100)
print(pyfiglet.figlet_format('hello'))
print(termcolor.colored('abdullah', color='yellow'))
print(termcolor.colored(pyfiglet.figlet_format('abdullah'), color='yellow'))

print('*'*100)


print(datetime.datetime.now())
print(datetime.datetime.now().second)
print(datetime.datetime.now().time())
print(datetime.time.max)
print(datetime.datetime.max)
print(datetime.datetime(2002, 8, 11))
# print(datetime.datetime(2002,8,11,59,59,400))
mybirth = datetime.datetime(2002, 8, 11)
datenow = datetime.datetime.now()
print(f'my birth is {mybirth}')
print(f'date now is {datenow}')
print(f'i lived for {(datenow-mybirth).days} days ')
mybirth = datetime.datetime(2002, 8, 11)
print(mybirth.strftime('%B'))
print(mybirth.strftime('%d %B %y'))


print('*'*100)


# iterable like (list , string ,tuple , dictionary ,set)
# منقدر منمر على العناصر بحلقة فور
# iterator
# بيستخدم ليجبلي عنصر واحد من الاتريبل
# اول شي بحول الاتريبل لاتريتر عن طريق
# iter()
# بس خلصو العناصر ما بيطبعلي شي لانو صارت الاتريتور فارغة
# محل ما بوقف بكمل
mystring = 'osama'
myiterator = iter(mystring)
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
# for i in myiterator :
# print(i)

# generator
# هو متل الفانكشن بس بيستخدم
# yield
# بدال Return
# وهو بيدعم الاتريتور
# يعني في كل امر نيكست
# برجعلي yeild


def generator():
    yield 1
    yield 2
    yield 3
    yield 4


mygen = generator()

print('hello')
print(next(mygen))
print('how r u ')
print(next(mygen))
print('fuck u')
print(next(mygen))
# حلقة فور هون بتكمل من عند اخر شي , اخر شي كان 3 بتكمل من الاربعة وبتوقف
for i in mygen:
    print(i)


print('*'*100)


# decorator تستخدم للتزيين
# مثال
def decorater(func):

    def nastedfucn():
        print('before')
        func()
        print('after')

    return nastedfucn


# بحط @ واسم الفانكشن الي مسؤولة عن التزيين مشان يتطبق التزيين على هاي الفانكشن
@decorater
def hello():
    print('hello from hello func')


hello()

print('*'*100)

# decorate func with paramitars


def docorater(func):
    def nasted(num1, num2):
        if num1 < 0 or num2 < 0:
            print('be aware of this number')
        func(num1, num2)
    return nasted


@docorater
def cal(n1, n2):
    print(n1+n2)


cal(-10, 20)

print('='*100)
# مثال عن الديكوريشن لحساب سرعة التنفيذ


def speedtest(func):
    def nasted():
        start = time()
        func()
        end = time()
        print(f'the run func take time {end - start}')
    return nasted


@speedtest
def func():
    for i in range(100):
        print(i, end=' ')


func()

print('='*100)

# zip
# بتدمج وبتطالعلي طول اقل list

list1 = [1, 2, 4, 5, 6]
list2 = ['a', 'b']
ultimatelist = zip(list1, list2)
print(ultimatelist)
for id2, id1 in ultimatelist:
    print(f'this is from list1 {id2}')
    print(f'this is from list2 {id1}')

print('='*100)
# مكتبة pillow
# هي مكتبة مسؤولة عن تعديل الصور
img = Image.open(r'C:\Users\ASUS\Desktop\backend\python zero\1305320.jpg')
# img.show()
# newimg = img.crop((100,100,100,100))
# newimg.show()
print('='*100)


def sayhello(name):
    # this is documentation
    '''this is fucnction say hello'''
    print(f'hello {name}')


# this __doc__ to show the documentation
# decumentation is to show details i wrote about func
print(sayhello.__doc__)
# هون بيطلع ال doumintation
# help(sayhello)


print('='*100)

# مكتبة pylint
# مسؤولة عن تنظيم الكود وكشف الاخطاء
# للكشف عن الاخطاء نكتب في الكونسول
# pylint.exe location_of_file

print('='*100)


# raise exception
# رفع الخطا

x = input('enter the pos number')
if int(x) < 0:
    raise Exception('wrong input')

x = int(input('enter the number'))
if type(x) != int:
    raise ValueError('only int accepted')


try:  # test the code and test error
    x = int(input('enter the integer'))

except:  # handle the error that found
    print('this is not integer')

else:  # if there is no error
    print('good , this is integer')

finally:  # if u catch an error or not that will happen
    print('what ever its happens')

print('='*100)

try:
    # (10/0)
    # print(h)
    x = 10
except ZeroDivisionError:
    print('error devision')

except NameError:
    print('wrong name')

except:
    print('error happens')


print('='*100)

x = 'hel'
if x is not int:
    print('fuck')


print('='*100)

# hint


def say_hello(name) -> str:
    print(f'hello {name}')


say_hello('abdullah')


print('='*100)

# تعلم لغة Python درس 095# - تعلم Regular Expressions الجزء الأول - مقدمة


my_string = re.search(r'[A-Z]{2}', 'AAbdullah SSermani')
print(my_string)
print('')
# position of search
print(my_string.span())
print(my_string.group())
print('')
is_email = re.search(r'[A-z0-9\.]+@[A-z0-9]+\.com|net',
                     "abdullahsermani2003@gmail.com")

if is_email:
    print(f'this is an email {is_email.group()}')
else:
    print(f'unvalid email ')

print('')

email_input = input('plz enter your email')
search = re.findall(r'[A-z0-9\.]+@[A-z0-9]+\.com|net', email_input)
empty_list = []

if search != []:
    empty_list.append(search)
    print('email added')
else:
    print('unvalid email')

for email in empty_list:
    print(email)

print('')

str1 = 'helllo i am abdullah'
ser1 = re.split(r'\s', str1, 2)
print(ser1)

print('')
str2 = 'how_to write -avery_good-article'
ser2 = re.split(r'-|_', str2)
print(ser2)
print('')


a = 'i love python'
print(re.sub(r'\s', '-', a))


print('')
web = 'https\\www.google.com'
serweb = re.search(r'(\w+)\.(\w+)\.(\w+)', web, re.IGNORECASE)
print(serweb.group())
print(serweb.groups())
for group in serweb.groups():
    print(group)


print('='*100)

# اي ميثود في البايسون قبلها __وبعدها __ تسمى
# بالماجيك ميثود او الداندار


class Member:
    # الاتربيوت الخاصة بالكلاس يتم مناداتها داخل الكلاس عن طريق اسم الكلاس نفسو
    # Member.not_allowed_names
    not_allowed_names = ['hell', 'shit', 'fuck']
    counter = 0
    # هذه الفانككشن تعتبر بمثابة الكونستركتر
    # يتم مناداتها عند استدعاء اوبجيكت من الكلاس
    # الاتربيوت الخاصة بالاوبجيككت يتم مناداتها داخل الكلاس عن طريق
    # self.fname
    # ال self
    # خاصة بالاوبجيكت

    def __init__(self, first_name, last_name):
        print('hello abdullah')
        self.fname = first_name
        self.lname = last_name
        Member.counter += 1

    # class method
    # هي ميثود مسؤولة عن تعديل اي شي بالكلاس نفسو
    # ليس لها علاقة بالاوبجيكت
    # يمكن استدعائها عن طريق الكلاس نفسو
    # يجب كتابة البرامترايز cls
    # كاول برامترايز
    # يجب كتابة قبلها
    # @classmethod

    @classmethod
    def show_counter(cls):
        print(f'we have {cls.counter} Users')

    def full_name(self):
        if self.fname in Member.not_allowed_names:
            raise ValueError('name not allowed')
        return f'{self.fname} {self.lname}'

    @staticmethod
    # لا تقبل برامترايز
    # يمكن كتابة بداخلها برامترايز
    def sayhello():
        print('hello from static method')

    # magic method
    def __len__(self):
        return len(self.not_allowed_names)


# عند طبااعة print(member_one)
# ستظهر هذه المعلومات


    def __str__(self):
        return f'hello abdullah this is from __str__'


member_one = Member('abdullah', 'sermani')
member_two = Member('ahmad', 'sermani')
member_three = Member('sana', 'sermani')
print(member_one.__class__)

print(member_one.lname)
print(member_one.full_name())
print(member_one.not_allowed_names)
print(Member.counter)
Member.show_counter()
Member.sayhello()
print(member_one)
print(len(member_one))


# inheretinc الورااثة
class Food:  # base class
    def __init__(self, nam):
        self.nam = nam
        print(f'{nam}food is created from main class')

    def eat(self):
        print('print method from main class')


class Apple(Food):  # Derived class
    # derived يعني الكلاس الوارث
    # ال init
    # في الكلاس الوارث
    # بتعمل override
    # على ال init
    # من الكلاس المورث
    def __init__(self, nam):
        # لتوريث ما داخل ال
        # init
        # في الكلاس المورث
        # super().__init__(nam)
        super().__init__(nam)
        print(f'{nam} is crated from derived class')


# food_one = Food('pizza')
food_two = Apple('pizza')
food_two.eat()


class baseone:
    def __init__(self) -> None:
        print('base one')

    def funcone(self):
        print('one')


class basetwo:
    def __init__(self) -> None:
        print('base two')

    def functwo(self):
        print('two')


class derived(baseone, basetwo):
    pass


o1 = derived()
# message risoliotion order
# بتطالعلي ترتيب الميثود
print(derived.mro())
o1.funcone()
o1.functwo()


# polymarphism
class A:
    def doing(self):
        print('from class a')
        raise NotImplementedError


class B(A):
    def doing(self):
        print('from class b')


class C(A):
    def doing(self):
        print('from class c')


instance = B()
instance.doing()

print(' ')

# Encapsulation
# protected _var
# can acces from the same class and the derived classes
# private __var
# can acces just from the same class


class abd:
    def __init__(self, name, price, why) -> None:
        self.name = name
        self._price = price
        self.__why = why

    def say_why(self):
        print(f'{self.__why}')


a = abd('ahmad', 200, 'fuck u')
print(a.name)
# يمكن طباعة العناصر
# protected
# من خارج الكلاس
print(a._price)
# print(a.__why)
a.say_why()
# يمكن طباعة الععناصر ال private
# من خلال التعليمة
# opject._class__privatevar
print(a._abd__why)

print(' ')

# GETTERS AND SETTERS


class sex:
    def __init__(self) -> None:
        pass

    def setname(self, name):
        self.__name = name

    def getname(self):
        print(f'{self.__name}')


a = sex()
a.setname('abdullah')
a.getname()

print(' ')
# Property Decorator


class r:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhello(self):
        print(f'hello {self.name}')
    # باضافة هذه الاشارة
    #  @property
    # يمكن معامله هذه الميثود ك
    # property
    # اي يصبح استدعائها بلا اقواس

    @property
    def age_in_days(self):
        return self.age * 365


o = r('ahmad', 20)
o.sayhello()
print(o.age_in_days)

print('    ')

# Abstract Base Class
# import
# لل ابتسراكت كلاس والابستراكت ميثود
# from abc import ABCMeta,abstractmethod
# نجعل الكلاس نوعه ابستراكت من خلال
# metaclass = ABCMeta


class proggraming(metaclass=ABCMeta):
    # نجعل المثيود ابستراكت من خلال اضافة
    # @abstractmethod
    @abstractmethod
    def has_opp(self):
        pass

    def fuck(self):
        print('fuck u')


class python(proggraming):
    def has_opp(self):
        return 'yes'


class php(proggraming):
    def has_opp(self):
        return 'no'


one = python()
print(one.has_opp())
one.fuck()


print('  ')


# data base


# انشاء ملف داتا بيز والاتصال فيه
db = sqlite3.connect('data.db')
# انشاء تايبل داخل ملف الداتا بيز ووضع فيه ثلاث متغيرات
db.execute(
    "CREATE TABLE if not exists skills (name TEXT , progress INTEGER , user_id INTEGER )")
# setting up the curser
cr = db.cursor()
cr.execute("CREATE TABLE if not exists users(user_id INTEGER , name TEXT)")

# inserting data
cr.execute("insert into users(user_id ,name) values(1,'ahmad')")
cr.execute("insert into users(user_id ,name) values(2,'abdullah')")
cr.execute("insert into users(user_id ,name) values(3,'sana')")
# Save (commit) changes
db.commit()

my_list = ['fateh', 'ibrahim', 'haytham']
for i, x in enumerate(my_list, 4):
    cr.execute(f"insert into users(user_id,name) values ({i},'{x}')")

db.commit()

# update data
cr.execute("update users set name = 'gamal' where user_id = 1 ")
db.commit()

# delete data
cr.execute("delete from users where user_id = 6")
db.commit()


# لجلب البيانات من قواعد البيانات
# cr.execute("select name,user_id from users")
# order by ترتيب حسب
# limit عدد البيانات التي اريد استخدامها
# offset يعمل سكيب للاسطر
cr.execute(
    "select * from users where user_id in(1,2,3) order by user_id limit 4 offset 2")
print(cr.fetchall())

# print(cr.fetchone())
# print(cr.fetchmany(2))

# قفل ملف الداتا بيز
db.close()


print('  ')


# ---------------------------------------------------------------------
# تعرف على __name__ و "__main__"
# اذا كنت بعمل ران للكود من الملف نفسو
# بتكون قيمة ال name
# هي main
# اي في حال كنت عامل امبورت لموديول
# وهالموديول فيها تعليمة
# if __name__ == '__main__' :
# print('hello')
# فما رح تنطبع الهلو هون

# ---------------------------------------------------------------------

# مكتبة timeit
# بتعمل ران للكود الي بعطيها ياه وبتكررو مليون مرة
# وبتعطينني اقصر وقت اشتغل فيها الكود خلال هالمليون مرة
print(dir(timeit))
print(timeit.timeit(stmt="'abdullah' * 1000 "))
# اذا كان عندي امبورت لموديول ما رح يقدر يتعرف عليها
# لهيك بحط بالسيت اب
# امبورت لهذه المويول
print(timeit.timeit(stmt="random.randint(1,100)", setup="import random"))
# ميثود ريبيت
# بتعمل ريبيت للميثود الماضية اربع مرات
# يعني بتعمل اربع ملاايين مرة
print(timeit.repeat(stmt="random.randint(1,100)", setup="import random", repeat=4))
# ---------------------------------------------------------------------

# نكتب بالكونسول
# explorer .
# بيفتحلي ال
# warking directory
# ---------------------------------------------------------------------


# إضافة ال Logging
# لل Code


# levelname
# ال critical
# او ال warning


# ال message
# هو الرسالة بما داخل ال
# critical
# او ال warning

# asctime هو التاريخ

# datefmt هو تنسيق التاريخ
print(dir(logging))
logging.basicConfig(filename="my_app.log", filemode="a",
                    format="'%(name)s'  || %(levelname)s  || %(message)s (%(asctime)s)",
                    datefmt="%d - %B - %Y, %H:%M:%S")
logging.critical("this is critical message")
my_logger = logging.getLogger("abdullah")
my_logger.warning("fuck u this iis from warning")
print('')
print('')
print('')
# ---------------------------------------------------------------------

# Unittest
# the modules that run unit testing (pytest ,unittest)
# كلمة assert
# هي مفتاح للتيست


def test_case_one():
    assert 3*4 == 12, "should be 12"


def test_case_two():
    assert 10*5 == 100, "should be 50"


# يجب عدم عمل امبورت للتيست كيز
# لذلك نكتب هذه التعليمة لتنفيذها ضمن هذا الكود تحديدا اي ضممن هذا الملف
if __name__ == '__main__':
    test_case_one()
    # test_case_two() #رح يطلعلي ايرور لان غلط
    print("all text case is ok")

print('')
print('')

#----------------------------------------------------------------------------
# مكتبة string
#Random Serial Numbers انشاء
import string
#print(string.digits)
#print(string.ascii_letters)
#print(string.ascii_lowercase)
#print(string.ascii_uppercase)
def makeserial(count) :
    all_char = string.digits + string.ascii_letters
    
    char_count = len(all_char)
    serial_list = []
    
    while count > 0 :
        x= random.randint(0,char_count -1)
        serial_list.append(all_char[x])
        count-=1
    for i in serial_list :
        print(i,end="")
    #print(''.join(serial_list))

makeserial(30)


print('')
print('')

#----------------------------------------------------------------------------
# flask
# نعمل امبورت من فلاسك لل FLASK


# render_template
# هي وظيفتا لما بعمل ريتورن بترجعلي صفحة ال 
# html 
# الي انا عاملا
from flask import Flask,render_template
skills_app = Flask(__name__)

@skills_app.route('/')
def main_page():
    return render_template("homepage.html",pagetitle='home',test = 'hello from home',custom_css ='home')

@skills_app.route('/about')
def about () :
    return render_template('about.html',pagetitle='about',test = 'hello from about',custom_css ='about')

@skills_app.route('/vid')
def vid():
    return render_template('vid.html',pagetitle = 'vid',test ='hello from vid page')

if __name__ == '__main__' :
    #port 5000
    #127.0.0.1:5000
    #skills_app.run(port=5000)
    pass

print('')
#-------------------------------------------------------------------------------------------------


#تعلم لغة Python درس 141# - تعلم Web Scraping وكيف تتحكم في المتصفح بواسطة Selenium
# Web Scraping
# ألتحكم بالمتصفح ليفتحلي الي بدي ياه


#-------------------------------------------------------------------------------------------------

#numpy
import numpy as np

mylist = [1,2,3,4]
my_array = np.array([1,2,3,4])
print(type(mylist))
print(type(my_array))

print(mylist[0])
print(my_array[0])
print('')
#dimintions array
d = np.array([[[6,7],[8,9]],[[1,2],[4,5]]])
print(d[1][1][0])
# ويمكن كتابتها بالطريقة
print(d[1,1,1])
# ndim\\number of dimentions
print(d.ndim)
print('')

#ndmin \\ number dimentions minimum
# اقل عدد لل 
# dimentions
arr = np.array([1,2,3] , ndmin=3)
print(arr[0]) # [[1,2,3]]
print(arr[0][0][1]) # 2
print(arr[0,0,2]) # 3

print('')

list1 = ['1','2','3']
list2 = np.array(['1','2','3'])
#id
# مكان التخزين
# address

# array
# التخزين بنفس المكان

# ال list
# باماكن متباعدة
print(id(list1[0]))
print(id(list1[1]))
print(id(list2[0]))
print(id(list2[1]))

list1 = [1,2,'a',True]
list2 = np.array([1,2,'a',True])

# في ال array
# يجب ان تكون البيانات متجانسة
print(list1)# بيحطلي كل عنصر حسب نوعو
print(list2)# رح يعتبرلي ياهن كلن string

print('')

num = 1000000
mylist = range(0,num)
mylist0 = range(0,num)

mylist1 = np.arange(0,num)
mylist2 = np.arange(0,num)

import time
list_start = time.time()
list_result=[]
for i,n in zip(mylist,mylist0) :
    list_result.append(i+n)
#print(list_result)
print(f'the time is {time.time()-list_start}')
# ويمكن كتابتها بالشكل
#list_result1 =[(i+n) for i,n in zip(mylist,mylist0)]
#print(list_result1)
array_start = time.time()
array_result = mylist1 + mylist2
#print(array_result)

#وقت التنفيذ بال arry
# اسرع باضعاف مضاعفة من السيت
print(f'the time is {time.time()-array_start}')

print('')

#استخدام الذاكرة في ال اراي
arr = np.arange(100)
print(arr , end = " ")
print('')
print(arr.itemsize)# حجم العنصر بالبايت
print(arr.size) # حجم المصفوفة
print(f'all bytes is {arr.size * arr.itemsize}')

print('=====')
#استخدام الذاكرة في الليست
list1 = range(100)
import sys
print(sys.getsizeof(list1[0]))
print(len(list1))
print(f'all bytes is {len(list1) *sys.getsizeof(list1[0])}')

print('=====')

#slicing and indexing in arrays
arr = np.array([1,2,3,4,5,6])
print(arr.ndim)
print(arr[1:4:1])
print('')

arr1 = np.array([['A','B','C'],['D','E','F'],['G','H','I']])
print(arr1.ndim)
print(arr1[0][0:2])
print(arr1[0:3, 0:2])
print('')
#أنواع البيانات والتحكم في المصفوفات
arr = np.array([1,2,3])
arr1 = np.array(['a','b','c'])
arr2 = np.array([1.2,1.3,1.4])
print(arr.dtype)
print(arr1.dtype)
print(arr2.dtype)
print('')

#create  array with specific data type
arr = np.array([1,2,3],dtype=float)
arr1 = np.array(['a','b','c'])
arr2 = np.array([1.2,1.3,1.4],dtype=int)
print(arr.dtype)
print(arr2.dtype)
print(arr[0])
print('')

#change data type of exesting array

arr = np.array([1,2,3])
arr = arr.astype(float)
print(arr.dtype)
print(arr)
print('')

arr = np.array([1,2,3,0])
arr = arr.astype(bool)
print(arr.dtype)
print(arr)
print('')
#test capacity
# الفرق بين int32
# وال int 64
arr = np.array([100,200,300,400],dtype='f') #change to float 32
print(arr.dtype)
print(arr)
print(arr[0].itemsize)
print('')
arr=arr.astype('float')#change to float 64
print(arr.dtype)
print(arr)
print(arr[0].itemsize)

print('')

#العمليات الحسابية
arr = np.array([1,2,3])
arr1 = np.array([4,5,6])
print(arr + arr1)
print(arr1 -arr )
print(arr1 * arr )
print(arr1 / arr )
print('')

arr = np.array([[1,2,3],[1,2,3]])
arr1 = np.array([[4,5,6],[1,2,3]])

print(arr + arr1)
print(arr1 -arr )
print(arr1 * arr )
print(arr1 / arr )

print('')

arr = np.array([1,2,3])
print(arr.min())
print(arr.max())
print(arr.sum())
print('')


arr=[1,2,3]
print(min(arr))
print(max(arr))
print(sum(arr,arr))
print('')

arr = np.array([[1,2],[3,0]])
print(arr.min())
print(arr.max())
print(arr.sum())
print('')

arr = np.array([[1,2],[3,4]])
print(arr.ndim)
arr=arr.ravel()
print(arr)
print(arr.ndim)
print('')

arr = np.array([[[1,2],[2,3]],[[4,5],[1,2]]])
print(arr.ndim)
arr=arr.ravel()
print(arr)
print(arr.ndim)
print('')



#shape and reshape
arr = np.array([1,2,3,4])
print(arr.ndim)
print(arr.shape)
print('')



arr = np.array([[1,2,3,4],[1,2,3,4]])
print(arr.ndim)
print(arr.shape)
print('')

arr = np.array([[[1,2,3,4],[1,2,3,4]]])
print(arr.ndim)
print(arr.shape)
print('')



arr = np.array([1,2,3,4,5,6,7,8])
reshaped_arr = arr.reshape(2,4)
print(reshaped_arr)
print(reshaped_arr.ndim)
print(reshaped_arr.shape)
print('')




arr = np.array([[[1,2,3,4],[1,2,3,4]]])
reshaped_arr = arr.reshape(-1)
print(reshaped_arr)
print(reshaped_arr.ndim)
print(reshaped_arr.shape)
print('')












































































































































































































