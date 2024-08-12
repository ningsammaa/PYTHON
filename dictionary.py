dictionary= {
    "Name": "Ningsamma Thebe",
    "Age": 20,
    "Address": "Nakhipot",
}

print(dictionary)

dictionary["Hobby"] = "Swimming"

dictionary["Name"] = "Samniba Limbu"

print(dictionary)

del dictionary["Age"]

print(dictionary)

key = "Age"

if key in dictionary:
    print(f"The key {key} is present in the dictionary.")
else:
    print("The key {key} is not present in the dictionary.")


dictionary.clear()