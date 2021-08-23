# exercise 1 doubler
numbers = [1, 2, 4, 6, 11, 20]
sq = 0
for val in numbers:
    sq = val * val
    print(sq)

#exercise 2 goodbye
users = input("Enter your name: ")
print("Goodbye" + users)



# exercise 3 Average of three
def average_of_three(num1, num2, num3):
    print((num1 + num2 + num3)/3)
average_of_three(9, 2, 3)

#exercise 4 palindrome

user = input("Enter the value or name")
reverse =user[:: -1]

if (user == reverse):
    print("yes it is a palindrome")
else:
    print("No its not a palindrome")

#exercise 5 fizz buzz
def fizz_buzz(max):
    nums=[]
    for i in range(0,max):
        if ((i%4==0 or i % 6 ==0) and (i % 4 !=0 or i%6 !=0)):
            nums.append(i)
            i+=1
            return nums
print(fizz_buzz(30))