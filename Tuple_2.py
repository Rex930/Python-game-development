Travel_data = (
    ("Paris", ("Eiffel Tower", "Croissant", "Spring")),
    ("Tokyo", ("Tokyo Tower", "Sushi", "Autumn")),
    ("New York", ("Statue of Liberty", "Pizza", "Fall")),
    ("Dubai", ("Burj Khalifa", "Shawarma", "Winter"))
)

print("Welcome to Travel Planner Game")
print("choose a city to explore:\n")

for i in range(len(Travel_data)):
    print(i + 1, ".", Travel_data[i][0])

choice = int(input("\nEnter your choice number: "))
index = choice - 1

selected_city = Travel_data[index]

print("\n✈️ Travel Details")
print("City:", selected_city[0])
print("Must Visit:", selected_city[1][0])
print("Try Food:", selected_city[1][1])
print("Best Season:", selected_city[1][2])