# Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
# While loops  

# for loops exec8utes a block a code a fixed amouint of times
# you can iterate over a range, string, sequence, etc. 

for x in reversed(range(1, 11, 2)):
    print(x)


for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)


name =  input("What is your name?: ")

while name == "":
    print("You did not enter your name.")
    name = input("Enter your name: ")

print(f"Hello {name}!")