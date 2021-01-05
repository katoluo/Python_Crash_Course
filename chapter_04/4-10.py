numbers = list(range(1,11))
print(numbers)
message = "The first three items in the list are:"
# 编译器报错之后，突然想起，不同类型能拼接使用str()转换 
print(message + str(numbers[:3]))
message = "Three items from the middle of the list are:"
print(message + str(numbers[3:6]))
message = "The last three items in the list are:"
print(message + str(numbers[-3:]))
