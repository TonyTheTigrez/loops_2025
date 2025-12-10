# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]

print(len(fruits))
# Challenge:
# Use a for loop to print each fruit on a new line.
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
for fruit in fruits:
    print(fruit)
# I just worked with loops
#loool
# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    if subject == "History":
        break
    print(subject)
# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"

list1000 = list(range(1,1001))

for number in list1000:
    if number > 300 and number < 500:
        continue
    print(number)
# Given:
numbers = [5, 10, 15, 20]




# Challenge:
# Use a for loop to add all the numbers and print the total.


apc = ["Alice", "Bob", "Charlie", "David", "Eve"]
credit_scores = [720, 680, 590, 610 , 750]

for applicant, score in zip(apc, credit_scores):
    # zip function combines two lists into pairs
    if score < 600:
        continue
    print(f"{applicant} is approved for credit with a score of {score}")
    

# for index in range(len(subject)-1):
#     print("Subject " + str(index) +": " + subjects[index])


numbers = [5, 10, 15, 20]

total = 0
for number in numbers:
    total += number # total = total + number
print("total: ", total)



new_num = list(range(1, 261))

total2 = 0


for num in new_num:
    total2 += num
print(f"Total: {total2}")

new_n = list(range(1, 260001))

total3 = 0

for number in new_n:
    total3 += number
print(f"Total: {total3}")