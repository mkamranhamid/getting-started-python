text = 'Hi Guys'
text += '\nThis is Adder Calculator' #where "\n" will move the other sentence in next line
print(text)

num1 = input('Enter any number')
opr = input('please enter the operatioin you wanna do with first number')
num2 = input('Enter any number')
if opr == '+':
    result = int(num1) + int(num2)
    print(result)
elif opr == '-':
    result = int(num1) - int(num2)
    print(result)
elif opr == '/':
    result = int(num1) + int(num2)
    print(result)
elif opr == '*':
    result = int(num1) * int(num2)
    print(result)
else:
    print('Sorry this operator is not yet implemented')
