print ("===simple calculator ===")


print("1.addition + ")
print("2.substraction -")
print("3.multiplication *")
print("4. division /")

choice = input("enter your choice :")

num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))


if choice == "1":
    print(num1 ,  "+" , num2 ," =", num1 + num2 )
elif choice == "2" :
    print(num1 , "-" , num2 , "=" ,num1 - num2)
elif choice == "3":
    print(num1 , "*" , num2 ,"=", num1 * num2)
elif choice == "4" :
    if num2 != "0":
        print(num1 , "/" , num2 ,"=", num1/num2 )
    else:
        print("error ! division by 0 not allowed ")
else:
    print("invalid choice")

