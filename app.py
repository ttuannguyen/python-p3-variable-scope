name = "Joe"

# def greeting():
#     print(f"Hello, {name}")

def greeting(name):
    print(f"Hello, {name}")

# greeting("Sophie")



change_the_world = "change yourself"

# using global keyword is a rare case, do not use unless absolutely necessary
def change_yourself():
    global change_the_world
    change_the_world = "world changed"

change_yourself()
print(change_the_world)

