print('введите первое число')
first=int(input())
print('введите второе число')
second=int(input())
print('введите операцию')
action=input()
if action=='+':
    result=first+second
elif action=='-':
	result=first-second
else:
	print('Введите "+", или "-"')
print(result)