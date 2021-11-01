from platform import platform
import sys, os
import hello_logs
import traceback

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
hello_logs.make_log_hello('start program', 'info')

try:
    requesthello = input('Введите номер варианта ---> ')
    numberofhello = int(requesthello)
    if numberofhello > count or numberofhello <= 0:
    	print('Ошибка! Нет такого варианта!')
    	hello_logs.make_log_hello('Wrong number!', 'error')
    	hello_logs.make_log_hello('end program', 'info')
    	sys.exit()
except EOFError: 
	print('Ошибка! Внезапный конец файла!')
	hello_logs.make_log_hello('Error!', 'error')
except KeyboardInterrupt:
	print('Ошибка! Вы отменили операцию!')
	hello_logs.make_log_hello(traceback.format_exc(), 'error')
except ValueError:
	print('Ошибка! Введено неправильное значение!')
	hello_logs.make_log_hello('Error!', 'error')
else:
	logs_temp = 'Chosen ' + str(numberofhello)
	hello_logs.make_log_hello(logs_temp, 'info')
	startthehello(numberofhello, listofprograms)

hello_logs.make_log_hello('end program', 'info')
