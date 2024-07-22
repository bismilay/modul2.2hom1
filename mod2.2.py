first=int(input('Введите первое число:'))
second=int(input('Введите второе число'))
third=int(input('Введите третье число'))
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
elif first != second or second != third or third != first:
    print(0)
    #Написал такие условия, также понимаю,что можно было использовать в конце else, ради интереса попробовал так
    

