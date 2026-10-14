# sort (original)sort not in result and sorted()(newlist)in result
marks =[60,73,48,50]
new_marks=sorted(marks,reverse=True)
print(new_marks)
print(marks)

age = [2,30,1,18]
age.sort(reverse=True)
print(age)

marks.sort()
print(marks)

names=["apple","mango","banana"]
names.sort()
print(names)

names={"apple","mango","banana"}
print(sorted(names))

# cannot be used
# names={"apple","manogo","banana"}
# names.sort()
# print(names)

cities=["Bengaluru","Pune","bengaluru","Chennai","Pune"]
u_cities={city.lower() for city in cities}
print(u_cities)
print(type(u_cities))

numbers=[2,3,2,4,3]
unique_squares=set()
for number in numbers:
    unique_squares.add(number*number)
print(unique_squares)

unique_squares={number*number for number in numbers}
print(unique_squares)
print(type(unique_squares))

numbers=[2,3,2,4,3]

sequare_list=[number*number for number in numbers]
squares_set={number*number for number in numbers}

print(sequare_list)
print(squares_set)

# Dictionary 
numbers=[2,3,4,5]
cube_by_number={}
for number in numbers:
    unique_squares.add(number * number)
print(unique_squares)
    
unique_squares={number*number for number in numbers}
print(unique_squares)
print(type(unique_squares))

numbers = [2,3,2,4,3]
sequare_list =[number*number for number in numbers]
squares_set ={number*number for number in numbers}

print(sequare_list)
print(squares_set)
 
# dictionary 
numbers=[2,3,4,5]
cube_by_number={}
for number in numbers:
    cube_by_number[number] = number**3
    print(cube_by_number)

cube_by_number={number:number**3 for number in numbers}
print(cube_by_number)
print(type(cube_by_number))