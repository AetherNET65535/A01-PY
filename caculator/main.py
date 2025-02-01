while (1):
    numberA = int((input ("第一数字：") ))
    numberB = int((input ("第二数字：") )) 

    sign = (input ("请输入运算符：") )

    if sign == '+':
        sum = numberA + numberB
    elif sign == '-':
        sum = numberA - numberB
    elif sign == '*':
        sum = numberA * numberB
    elif sign == '/':
        sum = numberA / numberB
    else:
        sum = 0

    print (sum)