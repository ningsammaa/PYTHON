full_name = str(input("Enter full name: "))
names = full_name.split()

initial_one = names[0][0].upper()
initial_two = names[-1][0].upper()
print(f"Your initials are: {initial_one}.Nayom {initial_two}")