names = [ 'Davie', 'Aragne', 'James' ]
print("I have found a big table.")
# 使用 insert() 将一位新嘉宾添加到名单开头
names.insert(0, 'kaly')
# 使用 insert() 将另一位新嘉宾添加到名单中间
names.insert(2, 'mike')
# 使用 append() 将最后一位新嘉宾添加到名单末尾
names.append('yarl')
print(names)
print("I just can invite two guest.")
message = "I'm so sorry, "
print(message + names.pop())
print(message + names.pop())
print(message + names.pop())
print(message + names.pop())
message = ", I'm inviting you."
print(names[0].title() + message)
print(names[1].title() + message)
del names[0]
del names[0]
print(names)
