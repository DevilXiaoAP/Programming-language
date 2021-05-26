def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("concat %f seconds\n" % t1.timeit(number=1000))

t2 = Timer("test2()", "from __main__ import test2")
print("append %f seconds\n" % t2.timeit(number=1000))

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension %f seconds\n" % t3.timeit(number=1000))

t4 = Timer("test4()", "from __main__ import test4")
print("list %f seconds\n" % t4.timeit(number=1000))

import timeit
#list pop pop(0)
popzero = timeit.Timer("x.pop(0)","from __main__ import x")
popend = timeit.Timer("x.pop()","from __main__ import x")

x = list(range(2000000))
print("popzero %f seconds\n" % popzero.timeit(number=1000))

x = list(range(2000000))
print("popend %f seconds\n" % popend.timeit(number=1000))

print("pop(0) pop")
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%15.f, %15.5f" %(pz,pt))