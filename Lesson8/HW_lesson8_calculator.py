firstNum = int(input ("Enter first number:"))
secondNum = int(input("Enter second number:"))
action = input("What should I do: +, -, *, /")

if action is "+":
    print (firstNum+secondNum)
elif action is "-":
    print (firstNum-secondNum)
elif action is "*":
    print (firstNum*secondNum)
elif action is "/":
    print (firstNum/secondNum)
else:
    print ("What do you mean?")