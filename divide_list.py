# this script will divide list into smaller pieces as equal as possible
my_list = ['apple', 'orange', 'cherry', 'strawberry', 'banana', 'grape', 'peach', 'peear', 'pineapple', 'melon', 'watermelon']

for i in range(0, len(my_list), 3):
	print(my_list[i:i + 3])
