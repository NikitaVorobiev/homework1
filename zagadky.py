answers=0
print('1. Какой язык программирования мы начали учить в этом семестре?')
answer1=input()
if answer1=='Python' or answer1=='python':
    answers+=1
	print('Правильно')
else:
    print('Не правильно')
print('2. Каким образом в python тело функции отделяется от заголовка?')
answer2=input()
if answer2=='4 пробела' or answer2=='    ' or answer2=='четыре пробела' or answer2=='пробелами':
    answers+=1
	print('Правильно')
else:
    print('Не правильно')
print('3. Каким знаком в языке python должен заканчиваться заголовок функции?')
answer3=input()
if answer3==':' or answer3=='двоеточие' or answer3=='двоеточием':
    answers+=1
	print('Правильно')
else:
    print('Не правильно')
print('4. Какое ключевое слово обозначает функцию ввода из консоли в python?')
answer4=input()
if answer4=='input':
    answers+=1
	print('Правильно')
else:
    print('Не правильно')
print('5. Какое ключевое слово обозначает принудительное окончание функции?')
answer5=input()
if answer5=='break':
    answers+=1
	print('Правильно')
else:
    print('Не правильно')
print('6. Какое главное отличие кодировки UTF-32 от UTF-8?')
answer6=input()
if answer6=='количество бит на символ':
    answers+=1
	print('Правильно')
else:
    print('Не правильно')
print('7. Какова типизация языка python 2?')
answer7=input()
if answer7=='не строгая':
    answers+=1
	print('Правильно')
else:
    print('Не правильно')
print('8. Какое ключевое слово обозначает функцию вывода текста в консоли в python?')
answer8=input()
if answer8=='print':
    answers+=1
	print('Правильно')
else:
    print('Не правильно')
print('9. Каким типом данных обозначают пустые переменные в языке python?')
answer9=input()
if answer9=='null':
    answers+=1
	print('Правильно')
else:
    print('Не правильно')
print('10. Какое ключевое слово используется для объявления функции в python?')
answer10=input()
if answer10=='def':
    answers+=1
	print('Правильно')
else:
    print('Не правильно')

print('правильных ответо', answers)