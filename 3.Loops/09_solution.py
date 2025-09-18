#List Uniqueness Checker
#Check if all element in a list are unique.If a duplication is founded, exit the loop and print the duplicate

items = ["apple","banana", "orange","apple","mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("duplicate:",item)
        break

unique_item.add(item)