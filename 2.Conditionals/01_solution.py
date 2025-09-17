#Age Group Categorization
#Classify person's age group: Child(<13), Teenager(13-19), Adult(20-59), Senior(60+)

# age = input("Provide me an age")
# age_in_int = int(age)

age=25

if age<13:
    print("Child")
elif age<20:
    print("Teenager")
elif age <60:
    print("Adult")
else:
    print("Senior")