# List Report

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# Print each item with a number
print("Shopping List:")

number = 1

for item in items:
    print(f"{number}. {item}")
    number = number + 1

# Count items with more than 4 letters
count = 0

for item in items:
    if len(item) > 4:
        count = count + 1

print("\nItems with more than 4 letters:", count)

# Find the longest item using a loop
longest = items[0]

for item in items:
    if len(item) > len(longest):
        longest = item

print("Longest item:", longest)