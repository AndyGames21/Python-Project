# Project 1

num1 = int(input("Enter The First Number: \n"))
num2 = int(input("Enter The Second Number: \n"))
num3 = int(input("Enter The Third Number: \n"))

def average (num1,num2,num3):
    avg = (num1 + num2 + num3)/3
    return avg


average = (f"The Average Between {num1},{num2},{num3} is {average(num1,num2,num3)}")

print(average)


