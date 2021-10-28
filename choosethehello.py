from platform import platform
import sys, os

def checkforhellos(listofprograms):
    global count
    count = 0
    listofhelloslower = []
    value = 'helloworld'
    for i in range(len(listofhellos)):
        listofhelloslower.append(listofhellos[i].lower())
        if value in listofhelloslower[i]:
            count = count + 1
            listitem = listofhellos[i]
            listofprograms.append(listofhellos[i])
            listitemsplit = listitem.partition('.')
            print('{0}.'.format(count) + listitemsplit[0])
    return listofprograms
    
def startthehello(numberofhello, listofprograms):
    i = numberofhello - 1
    os.system('py {0}'.format(listofprograms[i])) 

print('Выберите, пожалуйста, "Hello, world", который вы хотели бы запустить:')

listofhellos = os.listdir()
listofprograms = []
checkforhellos(listofprograms)

try:
    requesthello = input('Введите номер варианта ---> ')
    numberofhello = int(requesthello)
    if numberofhello > count or numberofhello <= 0:
        print('Ошибка! Нет такого варианта!')
        sys.exit()
except EOFError: 
    print('Ошибка! Внезапный конец файла!')
except KeyboardInterrupt:
    print('Ошибка! Вы отменили операцию!')
except ValueError:
    print('Ошибка! Введено неправильное значение!')
else:
    startthehello(numberofhello, listofprograms)
