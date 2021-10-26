import json

# Небольшое развитие программы Приввет, мир!

def Hellofunc(name):
	print('Hello, {0}!'.format(name))

def dicttotulp():
	protonames = (open('visitors.json','r'))
	namesjson = json.load(protonames)
	i = len(namesjson)
	namelist = []
	while i !=0:
		nn = namesjson['name{0}'.format(i)]		
		namelist.append(nn)
		i = i - 1
	namelist.sort()
	return(namelist)


names = dicttotulp()

for i in names:
	Hellofunc(i)
else:
	print('Thank you, everybody!')
