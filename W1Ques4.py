word = str(input("Enter any word: "))
index = int(input("Enter the starting index: "))

sub_string = word[index:]

print(f"Substring from index {index}: {sub_string}")