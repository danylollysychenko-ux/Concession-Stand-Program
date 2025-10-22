menu = {"pizza": 5.40,
        "nachos": 4.75,
        "popcorn": 6.25,
        "fries": 3.50,
        "chips": 2.00,
        "pretzel": 3.50,
        "soda": 2.75,
        "lemonade": 3.00}

print("------ MENU ------")
for key, value in menu.items():
    print(key.ljust(10), str(f"${value:.2f}").rjust(6))
print("------------------")

total = 0
order = []
while True:
    item = input("Select an item (Q to quit): ").strip().lower()
    if item.strip().lower() == "q":
        break
    elif item in menu:
        order.append(item)
        total += menu[item]
    else:
        print("The item is not in the menu.")

print("----- YOUR ORDER -----")
for i in order:
    print(f"{i}", end=" ")
print()
print("---------------")
print(f"Total: ${total:.2f}")