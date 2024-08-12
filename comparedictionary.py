dictionary_1 = {
    "College name": "King's College",
    "Location" : "Babarmahal, Kathmandu",

}

dictionary_2 = {
    "College name" : "King's College",
    "Location" : "Babarmahal, Kathamndu",
    "Courses" :"BSIT, BSCS, BBA, MBA",
    "Established" : 2008
}

keys_not_present = dictionary_2.keys() - dictionary_1.keys()

print(dictionary_1)
print(dictionary_2)
print(keys_not_present)