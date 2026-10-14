numbers=[1,2,3,4,5,3]
print(numbers, type(numbers))
print(len(numbers))
print(numbers[3])
print(numbers[1:5])
print(numbers[3:])
print(numbers[-4:-1])
print(numbers[::-1])
numbers.count(3)

# list constructor
stu=list(["abhi",45.7,True,1,2,3,4])
print(stu, type(stu))
#addinging elements
num=[1,2,3,4,5]
num.append(6)
num.insert(0,3)
num.extend([7,8,9])
print(num)
# remoing elements
num.pop()
num.pop(1)
num.remove(7)
num.clear()
del num
# chnging elements
num1=[1,2,3,4,5,3]
num1[5]=6
num1[1:4]=[20,30,40]
print(num1)
a =[1,2,3]
b=a.copy
print(b.index(3))

lst = [1,3,2]
lst.sort(reverse=True)
print(lst)