#Methond-1
numbers = [1,4,6,7,3,8,4]

add = sum(numbers)
print(add)

avg = len(numbers)

print("sum of all the elements is", add)
print("avg of all the elements is",add/avg)

#Method-2
numbers = [1,4,6,7,3,8,4]

add = 0
for i in numbers:
    add+= i

print(add)

count = 0
for i in numbers:
    count+=1

print(count)

print("sum of all the elements is", add)
print("avg of all the elements is",add/count)

#Method-3
import statistics
numbers = [1,4,6,7,3,8,4]

add = sum(numbers)
avg = statistics.mean(numbers)
print("sum of all the elements is", add)
print("avg of all the elements is", avg)
