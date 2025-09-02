# Write your solution here
list = []

while True:
    user = int(input("New item: "))
    if user == 0:
        print("Bye!")
        break
    list.append(user)
    print(f"The list now: {list}")
    print(f"The list in order: {sorted(list)}")
    

