class A(object):
    def set(self,a,b):
        x=a
        a=b
        b=x
        print(a,b)
#获取对象属性后返回值可直接使用：getattr()
a=A()
c=getattr(a,'set')
c(a='1',b='2')
