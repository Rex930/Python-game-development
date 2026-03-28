sample={
    "Name":"Bob",
    "Age":17,
    "City":"New York"
}
print(sample)
print(sample["Name"])
print(sample.keys())
print(sample.values())
if "country" in sample:
    print(sample["country"])
else:
    print("key does not exist")
sample["Profesion"]="software engineer"
print(sample)
del sample["City"]
print(sample)
sample["Age"]=20
print(sample)