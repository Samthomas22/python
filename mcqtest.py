'''i = 1
while True:
    if i%3 == 0:
        break
    print(i)

    i + = 1

print(min(max(False,-3,-4), 2,7))

def f(x):
    def f1(*args, **kwargs):
        print("Sanfoundry")
        return x(*args, **kwargs)
    return f1

for i in [1, 2, 3, 4][::-1]:
    print (i)

class tester:
    def __init__(self, id):
        self.id = str(id)
        id="224"

temp = tester(12)
print(temp.id)

z = set('abc')
z.add('san')
z.update(set(['p', 'q']))
print(z)

list1 = [1,2,3,4]
list2 = [2,4,5,6]
list3 = [2,6,7,8]
result = list()
result.extend(i for i in list1 if i not in (list2+list3) and i not in result)
result.extend(i for i in list2 if i not in (list1+list3) and i not in result)
result.extend(i for i in list3 if i not in (list1+list2) and i not in result)
print(result)

print('*', "abcde".center(6), '*', sep='')

list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(A[1][2])
'''
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)
'''
print("Hello {0[0]} and {0[1]}".format(('foo', 'bin')))

x = [[0], [1]]
print((' '.join(list(map(str, x))),))

d = {"john":40, "peter":45}
print(d)

d1 = {"john":40, "peter":45}
d2 = {"john":466, "peter":45}
print(d1 == d2)

d = {"john":40, "peter":45}
print(list(d.keys()))

d = {"john":40, "peter":45}
print(len(d))

i = 1
while True:
    if i%2 == 0:
        break
    print(i)
    i=i+2

i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i + = 1


class test:
    def __init__(self, a):
        self.a = a

    def display(self):
        print(self.a)


obj = test()
obj.display()


class Demo:
    def __init__(self):
        pass

    def test(self):
        print(__name__)

obj = Demo()
obj.test()'''


