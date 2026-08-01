cart = ("Rex", ["Milk", "Eggs", "Bread"])

print("initial Cart:")
print(cart)


cart[1].append("Apples")
print("\nAfter adding Apples:")
print(cart)

cart[1].remove("Bread")
print("\nAfter removing Bread:")
print(cart)

cart[1][1] = "Cheese"
print("\nAfter replacing Eggs with Cheese:")
print(cart)

print("\nFinal Cart Summary")
print("Owner:", cart[0])
print("Items:", cart[1])