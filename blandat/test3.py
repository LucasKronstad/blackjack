numberslist = []
howmany = int(input("How many numbers do you want to add? "))
for i in range(howmany):
    numbers = input("Type a number ")
    numberslist.append(numbers)
average = 0
for items in numberslist:
    average += int(items)
print(average / len(numberslist))