__author__ = 'kuanweichen'


aList = range(1, 6)
print aList
bList = aList
print bList
aList[2] = 'hello'
print aList
print bList
print aList == bList
print aList is bList

cList = range(6, 1, -1)
dList = []
for num in cList:
    dList.append(num)
print cList == dList
print cList


listA = [0,1,3,4]
listA.insert(0, 100)
listA.remove(3)
listA.append(7)
print listA
listB=['x', 'z', 't', 'q']
listA+listB
listB.sort()
listB.pop()
listA.extend([4, 1, 6, 3, 4])
print listA
print listA.index(1)
print listA.pop(4)
listA.reverse()
print listA


def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print applyEachTo([inc, square, halve, abs], 3.0)

animals = {'a': ['aardvark'], 'b': 'baboon', 'c': 'coati'}
print animals.keys()
animals['a'].append('anteater')
print animals
for e in animals:
    print e
