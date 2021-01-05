my_pizzas = [ 'one', 'two', 'three' ]
print("my_pizzas: " + str(my_pizzas))

friend_pizzas = my_pizzas[:]
print("friend_pizzas: " + str(friend_pizzas))

my_pizzas.append('my_four')
friend_pizzas.append('friend_four')

print("My favorite pizzas are:")
for value in my_pizzas:
    print(value)

print("My friend's favorite pizzas are:")
for value in friend_pizzas:
    print(value)

