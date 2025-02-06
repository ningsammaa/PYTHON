word = str(input("Enter any word: "))
swapped_word = word[-1] + word[1:-1] + word[0]
print(f"Swapped word: {swapped_word}")