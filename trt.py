# def expressions(*data):
#     numb = 0
#     for value in data:
#         numb = numb + value
#     print(numb)
#
# expressions(34, 67, 89, 23)

# def add(*data):
#     numb = 0
#     for x in data:
#         numb = numb + 1
#     return numb
#
# result = add(23, 45, 24, 56)
# print(result)

# def details(name, age, add):
#     print(name, age, add)
#
# details(name="Ram", age=17, add="ktm")
#
def details(**data):
    for key, value in data.items():
        print(key, value)

details(name="tej", age=10, add="kohalpur")