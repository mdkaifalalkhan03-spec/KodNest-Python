marks=[70,81,60]
stu_marks= marks
stu_marks[0]=100
print(marks)
print(stu_marks)

# modification/mutation
num = [10,20]
values=num
values.append(30)
print(num)
print(values)

first=[1,2,3]
second=first
print(first is second)
print(first == second)

num=[10,20]
values=num
values=[100,200]
print(num)
print(values)

first=[1,2,3]
second=[1,2,3]
print(first is second)
print(first==second)