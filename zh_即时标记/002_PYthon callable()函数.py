'''
描述
callable() 函数用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功。

对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True。

语法
callable()方法语法：

callable(object)

>> > callable(0)
False
>> > callable("runoob")
False

>> >

def add(a, b):
    ...
    return a + b


...
>> > callable(add)  # 函数返回 True
True
>> >

class A:  # 类
    ...

    def method(self):

        ...
    return 0


...
>> > callable(A)  # 类返回 True
True
>> > a = A()
>> > callable(a)  # 没有实现 __call__, 返回 False
False
>> >

class B:
    ...

    def __call__(self):

        ...
    return 0
'''

...
>> > callable(B)
True
>> > b = B()
>> > callable(b)  # 实现 __call__, 返回 True
True