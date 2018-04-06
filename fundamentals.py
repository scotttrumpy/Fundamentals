
#number of classes to calculate GPA
classnumber = input('How many classes are you in?')
mylist = []

# while number of values in array is less than number of classes
# add new entries to list
while len(mylist) < classnumber:
	grade = input('Enter your grade on a 4.0 scale: ')
	if grade >= 0 and grade <= 4:
		mylist.append(grade)
		print(mylist)

	elif grade > 4:
		print(error)
	elif grade < 0:
		print(error)

if len(mylist) == classnumber:
	print("Your final GPA is", sum(mylist) / classnumber)