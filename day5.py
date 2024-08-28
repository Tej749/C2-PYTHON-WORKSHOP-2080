# Python Loops :
'''
for loop : number of iteration is fixed; list tupble, dict, strings
while loop / infinite loop :
'''
'''
range function() : range function return a sequence of numbers, start from 0, by default, increment by 1 (by default) and 
stop before specified numbers.
Method 
range(stard, end) 
range(start, end, step)


'''
# for loop
# for i in range(5):
#     print(i, end=" ")
# print()

# for x in range(0, 50, 5):
#     print(x, end=" ")

# string
# college = "Nepalgunj Campus of Management & Technology"
#
# for y in college:
#     print(y, end="  ")
# list
# item = [2, 4, 6, 8, 10]
#
# for j in item:
#     print(j + 200)

# for m in range(50):
#     print(m, end=" ")

# for h in range(20, 40, 5):
#     print(h, end=" ")

# while loop / infinite loop

# i = 0
# while i < 100:
#     print("Nepalgunj Campus", i)
#     i = i + 1

# nested loop
# break & continue
# break
# for i in range(20):
#     print(i)
#     if i == 17:
#         break

# continue

for x in range(20):
    if x == 10:
        continue
    print(x)

